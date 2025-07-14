import io
import pandas as pd
import port.api.props as props
import port.api.d3i_props as d3i_props
from typing import Optional


def as_translatable(value: str | props.Translations) -> props.Translatable:
    translations = value if isinstance(value, dict) else props.Translations(en=value)
    return props.Translatable(translations)


def donation_table(
    name: str,
    title: props.Translations | str,
    df: pd.DataFrame,
    description: props.Translations | str | None = None,
    visualizations: list | None = None,
):
    """
    Creates a table for the UI prompt consent form.

    Parameters:
    name (str): The name of the table.
    title (props.Translations): The title of the table in multiple languages.
    df (pd.DataFrame): The DataFrame containing the table data.
    description (props.Translations | None): The description of the table in multiple languages. Default is None.
    visualizations (list | None): List of visualizations to be included in the table. Default is None.

    Returns:
    props.PropsUIPromptConsentFormTable: The created table object.
    """

    return d3i_props.PropsUIPromptConsentFormTableViz(
        name,
        title=as_translatable(title),
        data_frame=df,
        description=as_translatable(description) if description else None,
        visualizations=visualizations,
    )


def donation_flow(
    id: str,
    tables: list[d3i_props.PropsUIPromptConsentFormTableViz],
    meta_tables: Optional[list[props.PropsUIPromptConsentFormTable]] = None,
    description: Optional[props.Translations | str] = None,
    donate_question: Optional[props.Translations | str] = None,
    donate_button: Optional[props.Translations | str] = None,
):
    """
    Creates a donation flow for the UI prompt consent form.

    Parameters:
    id (str): The ID of the donation flow.
    description (props.Translations | str | None): The description of the donation flow in multiple languages. Default is None.
    donateQuestion (props.Translations | str | None): The donation question in multiple languages. Default is None.
    donateButton (props.Translations | str | None): The donation button text in multiple languages. Default is None.
    tables (list[props.PropsUIPromptConsentFormTable]): List of tables to be included in the donation flow.
    metaTables (list[props.PropsUIPromptConsentFormTable]): List of meta tables to be included in the donation flow.

    Returns:
    props.PropsUIPromptConsentForm: The created donation flow object.
    """

    tables = [t for t in tables if t is not None]

    return d3i_props.PropsUIPromptConsentFormViz(
        description=as_translatable(description) if description else None,
        donate_question=as_translatable(donate_question) if donate_question else None,
        donate_button=as_translatable(donate_button) if donate_button else None,
        tables=tables,
        # meta_tables = meta_tables if meta_tables else []
    )
