import "./fonts.css";
import "./framework/styles.css";
import Assembly from "./framework/assembly";
import { Bridge } from "./framework/types/modules";
import { LiveBridge } from "./live_bridge";
import FakeBridge from "./fake_bridge";
import { createRoot } from "react-dom/client";
import DevApp from "./dev/App";

const rootElement = document.getElementById("root") as HTMLElement;

let standalone = process.env?.REACT_APP_BUILD === "standalone" ?? false;
let production = process.env?.NODE_ENV === "production" ?? false;

const workerFile = new URL(
  "./framework/processing/py_worker.js",
  import.meta.url,
);
const worker = new Worker(workerFile);

let assembly: Assembly;
const run = (bridge: Bridge, locale: string): void => {
  assembly = new Assembly(worker, bridge);
  assembly.visualisationEngine.start(rootElement, locale);
  assembly.processingEngine.start();
  console.log(assembly);
};

if (production && !standalone) {
  // Setup embedded mode (requires to be embedded in iFrame)
  console.log("Initializing bridge system");
  LiveBridge.create(window, run);
} else {
  // Setup local development mode
  const devmode = import.meta.env.VITE_DEVMODE;
  if (devmode) {
    const root = createRoot(rootElement);
    root.render(<DevApp />);
  } else {
    console.log(import.meta.env);
    console.log("Running with fake bridge");
    run(new FakeBridge(), "en");
  }
}

const observer = new ResizeObserver(() => {
  const height = window.document.body.scrollHeight;
  const action = "resize";
  window.parent.postMessage({ action, height }, "*");
});

observer.observe(window.document.body);
