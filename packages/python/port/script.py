import logging
import zipfile
from typing import Any, Generator, TypedDict

import pandas as pd
import port.api.props as props
import port.donation_flows.facebook as facebook
import port.donation_flows.instagram as instagram
import port.donation_flows.tiktok as tiktok
import port.donation_flows.twitter as twitter
import port.helpers.port_helpers as ph

logger = logging.getLogger(__name__)


def process(session_id: int):
    platform = None
    if platform is None:
        p = yield ask_platform()
        platform = p.value

    while True:
        logger.info("Prompt for file for %s", platform)

        file_prompt = ph.generate_file_prompt("application/zip")
        file_result = yield ph.render_page(platform_file_header(platform), file_prompt)

        if file_result.__type__ == "PayloadString":
            review_data_prompt = donation_flow([file_result.value], platform)
            print(review_data_prompt)
            yield ph.render_page(platform_data_header(platform), review_data_prompt)

        else:
            logger.info("Skipped at file selection ending flow")
            break

    yield ph.exit(0, "Success")
    yield ph.render_end_page()


def donation_flow(file_input: list[str], platform: str) -> props.PropsUIPromptConsentForm:
    if platform == "Instagram":
        return instagram.create_donation_flow(file_input)
    if platform == "Facebook":
        return facebook.create_donation_flow(file_input)
    if platform == "Twitter":
        return twitter.create_donation_flow(file_input)
    if platform == "Tiktok":
        return tiktok.create_donation_flow(file_input)
    raise ValueError(f"Unknown platform: {platform}")


def platform_file_header(platform: str):
    return props.Translatable({"en": f"Select the {platform} data file", "nl": f"Selecteer het {platform} databestand"})


def platform_data_header(platform: str):
    return props.Translatable({"en": f"Review the {platform} data", "nl": f"Controleer de {platform} data"})


def ask_platform():
    title = props.Translatable(
        {"en": "Select import script to test", "nl": "Selecteer het import script dat je wilt testen"}
    )

    platform_buttons = props.PropsUIPromptRadioInput(
        title=props.Translatable({"en": "Platform", "nl": "Platform"}),
        description=props.Translatable({"en": "", "nl": ""}),
        items=[
            props.RadioItem(id=4, value="Instagram"),
            props.RadioItem(id=2, value="Tiktok"),
            props.RadioItem(id=3, value="Facebook"),
            props.RadioItem(id=1, value="Twitter"),
        ],
    )

    return ph.render_page(title, platform_buttons)
