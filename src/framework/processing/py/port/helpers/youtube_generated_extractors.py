# Auto-generated YouTube extractors

import pandas as pd
import json
from typing import List
from port.helpers.donation_flow import donation_table, donation_flow
import zipfile
import fnmatch

def read_csv_from_file_input(file_input: list[str], csv_filename: str) -> pd.DataFrame:
    """
    Reads a CSV file from a zip inside file_input.

    Args:
        file_input (list[str]): List of file paths, including the zip file.
        csv_filename (str): Name of the CSV file inside the zip.

    Returns:
        pd.DataFrame: The loaded DataFrame.
    """
    for path in file_input:
        if path.endswith('.zip'):
            with zipfile.ZipFile(path, 'r') as zip_ref:
                # Find matching file (e.g., endswith 'channel.csv')
                for name in zip_ref.namelist():
                    if name.endswith(csv_filename):
                        with zip_ref.open(name) as f:
                            try:
                                return pd.read_csv(f, encoding='utf-8')
                            except UnicodeDecodeError:
                                f.seek(0)
                                return pd.read_csv(f, encoding='latin1')  # fallback
    raise FileNotFoundError(f"{csv_filename} not found in ZIP files: {file_input}")

def get_in(d: dict, *keys):
    for key in keys:
        if isinstance(d, dict):
            d = d.get(key)
        elif isinstance(d, list) and isinstance(key, int) and len(d) > key:
            d = d[key]
        else:
            return None
    return d

def get_list(d: dict, *keys):
    val = get_in(d, *keys)
    return val if isinstance(val, list) else []

def snake_case(name: str) -> str:
    return name.lower().replace("-", "_").replace(".json", "").replace(".js", "").replace(" ", "_")

def read_json(file_input: List[str], pattern: List[str]) -> List[dict]:
    zip_path = file_input[0]
    matched_data = []

    with zipfile.ZipFile(zip_path, 'r') as zipf:
        for pat in pattern:
            for name in zipf.namelist():
                if fnmatch.fnmatch(name, pat):
                    with zipf.open(name) as f:
                        content = json.load(f)
                        if isinstance(content, list):
                            matched_data.extend(content)
                        else:
                            matched_data.append(content)
    return matched_data



def search_history_df(file_input: List[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/search-history.json"])

    records = []
    for entry in data:
        records.append({
            "activityControls": ", ".join(get_list(entry, 'activityControls')),
            "header": entry.get('header'),
            "products": ", ".join(get_list(entry, 'products')),
            "time": entry.get('time'),
            "title": entry.get('title'),
            "titleUrl": entry.get('titleUrl'),
        })
    df = pd.DataFrame(records)
    return df


def watch_history_df(file_input: List[str]) -> pd.DataFrame:
    data = read_json(file_input, ["*/watch-history.json"])

    records = []
    for entry in data:
        records.append({
            "activityControls": ", ".join(get_list(entry, 'activityControls')),
            "header": entry.get('header'),
            "products": ", ".join(get_list(entry, 'products')),
            "subtitles_name": get_in(entry, 'subtitles', 'name'),
            "subtitles_url": get_in(entry, 'subtitles', 'url'),
            "time": entry.get('time'),
            "title": entry.get('title'),
            "titleUrl": entry.get('titleUrl'),
            "activityControls": ", ".join(get_list(entry, 'activityControls')),
            "details_name": get_in(entry, 'details', 'name'),
            "header": entry.get('header'),
            "products": ", ".join(get_list(entry, 'products')),
            "time": entry.get('time'),
            "title": entry.get('title'),
        })
    df = pd.DataFrame(records)
    return df


def create_donation_flow(file_input: List[str]):
    """Create donation flow from YouTube ZIP."""
    tables = []

    try:
        df = search_history_df(file_input)
        if not df.empty:
            tables.append(donation_table(name='search_history', df=df, title={'en': 'search_history'}))
    except Exception as e:
        print(f'Error in search_history_df:', e)

    try:
        df = watch_history_df(file_input)
        if not df.empty:
            tables.append(donation_table(name='watch_history', df=df, title={'en': 'watch_history'}))
    except Exception as e:
        print(f'Error in watch_history_df:', e)

    try:
        df = read_csv_from_file_input(file_input, 'HPC-videos.csv')
        df = df[['Video ID', 'Playlist Video Creation Timestamp']]  # select expected columns
        if not df.empty:
            tables.append(donation_table(name='HPC-videos', df=df, title={'en': 'HPC-videos'}))
    except Exception as e:
        print(f'Error reading HPC-videos.csv:', e)

    try:
        df = read_csv_from_file_input(file_input, 'Tryal-videos.csv')
        df = df[['Video ID', 'Playlist Video Creation Timestamp']]  # select expected columns
        if not df.empty:
            tables.append(donation_table(name='Tryal-videos', df=df, title={'en': 'Tryal-videos'}))
    except Exception as e:
        print(f'Error reading Tryal-videos.csv:', e)

    try:
        df = read_csv_from_file_input(file_input, 'URL-configuraties van kanaal.csv')
        df = df[['Kanaal-ID', 'Naam van vanity-URL 1 voor kanaal', 'Naam van vanity-URL 2 voor kanaal']]  # select expected columns
        if not df.empty:
            tables.append(donation_table(name='URL-configuraties van kanaal', df=df, title={'en': 'URL-configuraties van kanaal'}))
    except Exception as e:
        print(f'Error reading URL-configuraties van kanaal.csv:', e)

    try:
        df = read_csv_from_file_input(file_input, 'Video_s in Music.csv')
        df = df[['Video-ID', 'Tijdstempel voor het maken van een playlistvideo']]  # select expected columns
        if not df.empty:
            tables.append(donation_table(name='Video_s in Music', df=df, title={'en': 'Video_s in Music'}))
    except Exception as e:
        print(f'Error reading Video_s in Music.csv:', e)

    try:
        df = read_csv_from_file_input(file_input, 'Video_s in TFL.csv')
        df = df[['Video-ID', 'Tijdstempel voor het maken van een playlistvideo']]  # select expected columns
        if not df.empty:
            tables.append(donation_table(name='Video_s in TFL', df=df, title={'en': 'Video_s in TFL'}))
    except Exception as e:
        print(f'Error reading Video_s in TFL.csv:', e)

    try:
        df = read_csv_from_file_input(file_input, 'Video_s in Watch later.csv')
        df = df[['Video-ID', 'Tijdstempel voor het maken van een playlistvideo']]  # select expected columns
        if not df.empty:
            tables.append(donation_table(name='Video_s in Watch later', df=df, title={'en': 'Video_s in Watch later'}))
    except Exception as e:
        print(f'Error reading Video_s in Watch later.csv:', e)

    try:
        df = read_csv_from_file_input(file_input, 'Watch later-videos.csv')
        df = df[['Video ID', 'Playlist Video Creation Timestamp']]  # select expected columns
        if not df.empty:
            tables.append(donation_table(name='Watch later-videos', df=df, title={'en': 'Watch later-videos'}))
    except Exception as e:
        print(f'Error reading Watch later-videos.csv:', e)

    try:
        df = read_csv_from_file_input(file_input, 'abonnementen.csv')
        df = df[['Kanaal-ID', 'Kanaal-URL', 'Kanaaltitel']]  # select expected columns
        if not df.empty:
            tables.append(donation_table(name='abonnementen', df=df, title={'en': 'abonnementen'}))
    except Exception as e:
        print(f'Error reading abonnementen.csv:', e)

    try:
        df = read_csv_from_file_input(file_input, 'channel URL configs.csv')
        df = df[['Channel ID', 'Channel Vanity URL 1 Name']]  # select expected columns
        if not df.empty:
            tables.append(donation_table(name='channel URL configs', df=df, title={'en': 'channel URL configs'}))
    except Exception as e:
        print(f'Error reading channel URL configs.csv:', e)

    try:
        df = read_csv_from_file_input(file_input, 'channel community moderation settings.csv')
        df = df[['Channel ID']]  # select expected columns
        if not df.empty:
            tables.append(donation_table(name='channel community moderation settings', df=df, title={'en': 'channel community moderation settings'}))
    except Exception as e:
        print(f'Error reading channel community moderation settings.csv:', e)

    try:
        df = read_csv_from_file_input(file_input, 'channel feature data.csv')
        df = df[['Channel ID', 'Channel Auto Moderation in Live Chat', 'Video Default Allowed Comments Type', 'Video Default Targeted Audience', 'Video Default License', 'Video Default Location Latitude', 'Video Default Location Longitude']]  # select expected columns
        if not df.empty:
            tables.append(donation_table(name='channel feature data', df=df, title={'en': 'channel feature data'}))
    except Exception as e:
        print(f'Error reading channel feature data.csv:', e)

    try:
        df = read_csv_from_file_input(file_input, 'channel page settings.csv')
        df = df[['Channel ID']]  # select expected columns
        if not df.empty:
            tables.append(donation_table(name='channel page settings', df=df, title={'en': 'channel page settings'}))
    except Exception as e:
        print(f'Error reading channel page settings.csv:', e)

    try:
        df = read_csv_from_file_input(file_input, 'channel.csv')
        df = df[['Channel ID', 'Channel Title (Original)', 'Channel Visibility']]  # select expected columns
        if not df.empty:
            tables.append(donation_table(name='channel', df=df, title={'en': 'channel'}))
    except Exception as e:
        print(f'Error reading channel.csv:', e)

    try:
        df = read_csv_from_file_input(file_input, 'comments.csv')
        df = df[['Comment ID', 'Channel ID', 'Comment Create Timestamp', 'Price', 'Video ID', 'Comment Text']]  # select expected columns
        if not df.empty:
            tables.append(donation_table(name='comments', df=df, title={'en': 'comments'}))
    except Exception as e:
        print(f'Error reading comments.csv:', e)

    try:
        df = read_csv_from_file_input(file_input, 'gegevens voor kanaalfunctie.csv')
        df = df[['Kanaal-ID', 'Automatische moderatie in live chat van kanaal', 'Standaard toegestane reactietype van video', 'Standaard doelgroep van video', 'Standaardlicentie van video', 'Standaardbreedtegraad van videolocatie', 'Standaardlengtegraad van videolocatie']]  # select expected columns
        if not df.empty:
            tables.append(donation_table(name='gegevens voor kanaalfunctie', df=df, title={'en': 'gegevens voor kanaalfunctie'}))
    except Exception as e:
        print(f'Error reading gegevens voor kanaalfunctie.csv:', e)

    try:
        df = read_csv_from_file_input(file_input, 'instellingen voor het beheer van je kanaalcommu.csv')
        df = df[['Kanaal-ID']]  # select expected columns
        if not df.empty:
            tables.append(donation_table(name='instellingen voor het beheer van je kanaalcommu', df=df, title={'en': 'instellingen voor het beheer van je kanaalcommu'}))
    except Exception as e:
        print(f'Error reading instellingen voor het beheer van je kanaalcommu.csv:', e)

    try:
        df = read_csv_from_file_input(file_input, 'instellingen voor kanaalpagina.csv')
        df = df[['Kanaal-ID']]  # select expected columns
        if not df.empty:
            tables.append(donation_table(name='instellingen voor kanaalpagina', df=df, title={'en': 'instellingen voor kanaalpagina'}))
    except Exception as e:
        print(f'Error reading instellingen voor kanaalpagina.csv:', e)

    try:
        df = read_csv_from_file_input(file_input, 'kanaal.csv')
        df = df[['Kanaal-ID', '(Originele) kanaaltitel', 'Kanaalzichtbaarheid']]  # select expected columns
        if not df.empty:
            tables.append(donation_table(name='kanaal', df=df, title={'en': 'kanaal'}))
    except Exception as e:
        print(f'Error reading kanaal.csv:', e)

    try:
        df = read_csv_from_file_input(file_input, 'playlists.csv')
        df = df[['Playlist ID', 'Add new videos to top', 'Playlist Title (Original)', 'Playlist Title (Original) Language', 'Playlist Create Timestamp', 'Playlist Update Timestamp', 'Playlist Video Order', 'Playlist Visibility', 'Playlist-ID', "Nieuwe video's bovenaan toevoegen", 'Playlist-titel (Origineel)', '(Originele) taal van playlist-titel', 'Playlist tijdstempel maken', 'Playlist tijdstempel updaten', 'Videovolgorde playlist', 'Zichtbaarheid van playlist']]  # select expected columns
        if not df.empty:
            tables.append(donation_table(name='playlists', df=df, title={'en': 'playlists'}))
    except Exception as e:
        print(f'Error reading playlists.csv:', e)

    try:
        df = read_csv_from_file_input(file_input, 'reacties.csv')
        df = df[['Reactie-ID', 'Kanaal-ID', 'Aanmaaktijdstempel reactie', 'Prijs', 'Video-ID', 'Reactietekst']]  # select expected columns
        if not df.empty:
            tables.append(donation_table(name='reacties', df=df, title={'en': 'reacties'}))
    except Exception as e:
        print(f'Error reading reacties.csv:', e)

    try:
        df = read_csv_from_file_input(file_input, 'subscriptions.csv')
        df = df[['Channel Id', 'Channel Url', 'Channel Title']]  # select expected columns
        if not df.empty:
            tables.append(donation_table(name='subscriptions', df=df, title={'en': 'subscriptions'}))
    except Exception as e:
        print(f'Error reading subscriptions.csv:', e)

    try:
        df = read_csv_from_file_input(file_input, 'video-opnamen.csv')
        df = df[['Video-ID', 'Hoogte van video-opname', 'Latitude van video-opname', 'Longitude van video-opname']]  # select expected columns
        if not df.empty:
            tables.append(donation_table(name='video-opnamen', df=df, title={'en': 'video-opnamen'}))
    except Exception as e:
        print(f'Error reading video-opnamen.csv:', e)

    try:
        df = read_csv_from_file_input(file_input, 'video_s.csv')
        df = df[['Video-ID', 'Geschatte duur (ms)', 'Videocategorie', 'Videobeschrijving (origineel)', 'Kanaal-ID', 'Tag 1', 'Videotitel (origineel)', 'Privacy', 'Videostatus', 'Tijdstempel aanmaaktijd video', 'Tijdstempel publicatietijd video']]  # select expected columns
        if not df.empty:
            tables.append(donation_table(name='video_s', df=df, title={'en': 'video_s'}))
    except Exception as e:
        print(f'Error reading video_s.csv:', e)

    if tables:
        return donation_flow(id='youtube', tables=tables)
    else:
        return None