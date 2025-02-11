import pandas as pd
import port.api.props as props

def create_table(
    name: str,
    title: props.Translations,
    df: pd.DataFrame,
    description: props.Translations | None = None,
    visualizations: list | None = None
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
    return props.PropsUIPromptConsentFormTable(
        name,
        title = props.Translatable(title),
        data_frame = df,
        description = props.Translatable(description) if description else None,
        visualizations = visualizations
    )
