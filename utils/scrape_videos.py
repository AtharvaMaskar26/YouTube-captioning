import youtube_dl

def get_channel_videos(channel_url):
    """
    description: This function takes the channel url and returns all video ids. 
    parameters:
        channel_url (str): YouTube channel url
    returns: 
        video_urls (arr): Array of YouTube ids
    """

    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'force_generic_extractor': True,
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(channel_url, download=False)
    
    if 'entries' in result:
        video_urls = [entry['url'] for entry in result['entries']]
        return video_urls
    else:
        return []
