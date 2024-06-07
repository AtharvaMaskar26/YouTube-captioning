import re

def is_youtube_channel_url(url):
    """
    desription: Check if the given URL is a custom YouTube channel URL in the format: https://www.youtube.com/@{channel_name}/videos
    
    parameters:
    - url (str): The URL to check.
    
    Returns:
    - bool: True if the URL is a custom YouTube channel URL, False otherwise.
    """
    custom_youtube_channel_regex = (
        r"https://www\.youtube\.com/@[a-zA-Z0-9_]+/videos"
    )
    match = re.match(custom_youtube_channel_regex, url)
    return match is not None
