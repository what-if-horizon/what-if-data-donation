import json
import logging
import zipfile
from typing import Any, Generator, TypedDict

import pandas as pd
import port.api.props as props
import port.donation_flows.facebook as facebook
import port.donation_flows.instagram as instagram
import port.donation_flows.tiktok as tiktok
import port.donation_flows.twitter as twitter
import port.donation_flows.youtube as youtube
import port.helpers.port_helpers as ph
from port.api import d3i_props

logger = logging.getLogger(__name__)


def process(session_id: int, platform: str | None):
    if platform is None or platform == "":
        p = yield ask_platform()
        platform = p.value
        assert isinstance(platform, str)

    while True:
        logger.info("Prompt for file for %s", platform)

        if platform.lower() in ("tiktok", "tt"):
            extensions_arg = "application/json"
        else:
            extensions_arg = "application/zip"

        file_prompt = ph.generate_file_prompt(extensions_arg)
        file_result = yield ph.render_page(platform_file_header(platform), file_prompt)

        if file_result.__type__ == "PayloadString":
            # TODO: Validate the file and ask to retry if needed!

            review_data_prompt = donation_flow([file_result.value], platform)
            # WvA I think donation flow should just never return None instead?
            if not review_data_prompt:
                logger.info("No donation flow received")
                break
            result = yield ph.render_page(platform_data_header(platform), review_data_prompt)
            if result.__type__ == "PayloadJSON":
                reviewed_data = result.value
                yield ph.donate(f"{session_id}", reviewed_data)
            elif result.__type__ == "PayloadFalse":
                value = json.dumps('{"status" : "data_submission declined"}')
                yield ph.donate(f"{session_id}", value)

            break
        else:
            logger.info("Skipped at file selection ending flow")
            break

    yield ph.exit(0, "Success")
    # WvA This doesn't seem to exist and the example script doesn't have it anymore, so I commented it out
    # yield ph.render_end_page()


def donation_flow(file_input: list[str], platform: str) -> d3i_props.PropsUIPromptConsentFormViz | None:
    if platform == "Instagram":
        return instagram.create_donation_flow(file_input)
    if platform == "Facebook":
        return facebook.create_donation_flow(file_input)
    if platform == "Twitter":
        return twitter.create_donation_flow(file_input)
    if platform == "Tiktok":
        return tiktok.create_donation_flow(file_input)
    if platform == "Youtube":
        return youtube.create_donation_flow(file_input)
    raise ValueError(f"Unknown platform: {platform}")


def platform_file_header(platform: str):
    return props.Translatable(
        {
            "en": f"Select the {platform} data file",
            "nl": f"Selecteer het {platform} databestand",
            "es": f"Selecciona el archivo de datos de {platform}",
        }
    )


def platform_data_header(platform: str):
    return props.Translatable(
        {
            "en": f"Review the {platform} data",
            "nl": f"Controleer de {platform} data",
            "es": f"Revisa los datos de {platform}",
        }
    )


def ask_platform():
    title = props.Translatable(
        {
            "en": "Select import script to test",
            "nl": "Selecteer het import script dat je wilt testen",
            "es": "Selecciona el script de importación para probar",
        }
    )

    platform_buttons = props.PropsUIPromptRadioInput(
        title=props.Translatable({"en": "Platform", "nl": "Platform", "es": "Platform"}),
        description=props.Translatable({"en": "", "nl": "", "es": ""}),
        items=[
            props.RadioItem(id=5, value="Youtube"),
            props.RadioItem(id=4, value="Instagram"),
            props.RadioItem(id=2, value="Tiktok"),
            props.RadioItem(id=3, value="Facebook"),
            props.RadioItem(id=1, value="Twitter"),
        ],
    )

    return ph.render_page(title, platform_buttons)
