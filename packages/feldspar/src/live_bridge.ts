import { CommandSystem, isCommandSystem, isCommandSystemDonate } from './framework/types/commands'
import { Bridge, ResponseSystemDonate } from './framework/types/modules'

// Response types from the parent (feldspar_app.js)
export interface DonateSuccess {
  __type__: 'DonateSuccess'
  key: string
  status: number
}

export interface DonateError {
  __type__: 'DonateError'
  key: string
  status: number
  error: string
}

export type DonateResponse = DonateSuccess | DonateError

export function isDonateResponse(data: any): data is DonateResponse {
  return data && (data.__type__ === 'DonateSuccess' || data.__type__ === 'DonateError')
}

interface PendingDonation {
  resolve: (result: ResponseSystemDonate) => void
}

export class LiveBridge implements Bridge {
  port: MessagePort
  private pendingDonations: Map<string, PendingDonation> = new Map()

  // Tracks the single active bridge so we can update its port when the host
  // re-initializes the MessageChannel. This replaces the old `static initialized`
  // boolean, which was correct for preventing double-init but prevented the port
  // update needed to fix the Firefox channel-mismatch bug (see updatePort below).
  static currentBridge: LiveBridge | null = null

  constructor(port: MessagePort) {
    this.port = port
    this.setupResponseListener()
  }

  private setupResponseListener(): void {
    this.port.onmessage = (event) => {
      if (isDonateResponse(event.data)) {
        this.handleDonateResponse(event.data)
      } else {
        this.log('info', 'received unknown message', event.data)
      }
    }
  }

  // feldspar_app.js calls setupChannel() for both the iframe `onload` event and
  // the `app-loaded` postMessage. The guard there only blocks `onload` from
  // replacing an existing channel — `app-loaded` has no guard. In Firefox,
  // `onload` fires (creating Channel A, which LiveBridge receives) BEFORE
  // `app-loaded` is delivered to the host. When `app-loaded` then arrives it
  // replaces `this.channel` with Channel B and sends a second `live-init` with
  // port2_B. With the old `static initialized` flag that message was ignored,
  // leaving LiveBridge on port2_A while the host used Channel B. Every call to
  // sendDonateResponse() then posted to port1_B → port2_B (no listener) → hang.
  //
  // Fix: accept the new port when a subsequent `live-init` arrives and update
  // the response listener. Any donations waiting on the old port are failed
  // immediately — they would have hung forever anyway.
  updatePort(newPort: MessagePort): void {
    this.log('info', 'Host re-initialized MessageChannel — updating port')
    this.port = newPort
    this.setupResponseListener()
    for (const [key, pending] of this.pendingDonations) {
      this.log('error', `Failing pending donation ${key}: channel replaced by host`)
      pending.resolve({ success: false, key, status: 0, error: 'Channel re-initialized by host' })
    }
    this.pendingDonations.clear()
  }

  private handleDonateResponse(response: DonateResponse): void {
    const pending = this.pendingDonations.get(response.key)

    if (response.__type__ === 'DonateSuccess') {
      console.log('[LiveBridge] DonateSuccess:', {
        key: response.key,
        status: response.status
      })
      if (pending) {
        pending.resolve({
          success: true,
          key: response.key,
          status: response.status
        })
      }
    } else {
      console.error('[LiveBridge] DonateError:', {
        key: response.key,
        status: response.status,
        error: response.error
      })
      if (pending) {
        pending.resolve({
          success: false,
          key: response.key,
          status: response.status,
          error: response.error
        })
      }
    }

    this.pendingDonations.delete(response.key)
    this.log('info', `Donation completed, pending: ${this.pendingDonations.size}`)
  }

  static create(window: Window, callback: (bridge: Bridge, locale: string) => void): void {
    window.addEventListener('message', (event) => {
      console.log('MESSAGE RECEIVED', event)
      if (event.data.action === 'live-init') {
        const newPort = event.ports[0]
        const locale = event.data.locale

        if (LiveBridge.currentBridge === null) {
          // First live-init: create the bridge and start the application.
          console.log('LOCALE', locale)
          const bridge = new LiveBridge(newPort)
          LiveBridge.currentBridge = bridge
          callback(bridge, locale)
        } else {
          // Subsequent live-init: host replaced its MessageChannel.
          // Update the existing bridge's port instead of ignoring the message.
          LiveBridge.currentBridge.updatePort(newPort)
        }
      }
    })
  }

  async send(command: CommandSystem): Promise<ResponseSystemDonate | void> {
    if (!isCommandSystem(command)) {
      this.log('error', 'received unknown command', command)
      return
    }

    // Track pending donations and return promise
    if (isCommandSystemDonate(command)) {
      return new Promise<ResponseSystemDonate>((resolve) => {
        this.pendingDonations.set(command.key, { resolve })
        this.log('info', `Donation started, pending: ${this.pendingDonations.size}`, command)
        this.port.postMessage(command)
      })
    }

    this.log('info', 'send', command)
    this.port.postMessage(command)
  }


  private log(level: 'info' | 'error', ...message: any[]): void {
    const logger = level === 'info' ? console.log : console.error
    logger('[LiveBridge]', ...message)
  }
}
