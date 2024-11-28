import zipfile

import pandas as pd
from typing import Any, Generator, TypedDict

import port.api.props as props
import port.helpers.port_helpers as ph

import port.platforms.instagram as instagram
import port.platforms.tiktok as tiktok
import port.platforms.facebook as facebook


def process(session_id: int):
    platform = "Facebook"
    if platform is None:
        p = yield ask_platform()
        platform = p.value

    if platform == 'Instagram':
        yield from instagram.process(session_id)
    if platform == 'Tiktok':
        yield from tiktok.process(session_id)
    if platform == 'Facebook':
        yield from facebook.process(session_id)

    yield ph.exit(0, "Success")
    yield ph.render_end_page()


def ask_platform():
    title = props.Translatable({
       "en": "Select import script to test",
       "nl": "Selecteer het import script dat je wilt testen"
    })

    platform_buttons = props.PropsUIPromptRadioInput(
        title= props.Translatable({"en": "Platform", "nl": "Platform"}),
        description= props.Translatable({"en": "", "nl": ""}),
        items= [
           props.RadioItem(id=1, value='Instagram'),
           props.RadioItem(id=2, value='Tiktok'),
           props.RadioItem(id=3, value='Facebook')
        ])

    return ph.render_page(title, platform_buttons)
