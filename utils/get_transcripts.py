from youtube_transcript_api import YouTubeTranscriptApi

def get_video_transcripts(video_id):
    """
    description:
        Takes a youtube id and returns transcripts translated to english
    parameters: 
        video_id (str): youtube video id
    returns: 
        translated_transcripts (array): Array of all transcripts translated to english
    """
    # retrieve the available transcripts
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

    translated_transcripts = []
    # iterate over all available transcripts
    for transcript in transcript_list:
        # translating the transcript will return another transcript object
        translated_transcripts.append(transcript.translate('en').fetch())

    return translated_transcripts
