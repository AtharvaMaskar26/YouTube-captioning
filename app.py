import streamlit as st

# Importing util tools 
from utils import get_channel_videos
from utils import is_youtube_channel_url

st.title("YouTube caption translator")
st.write("📹 Get translated transcripts for any YouTube channel, just enter the channel's url and get started")
st.markdown("Eg: https://www.youtube.com/@<channel_name>/videos")

with st.form("my_form"):

    # 1. Fetch channel URL
    channel_url = st.text_input("Enter YouTube Channel URL: \n")
    
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        # 2. Verify if the channel url is valid
        is_valid_channel_url = is_youtube_channel_url(channel_url)

        if is_valid_channel_url:
            # 3.  Fetch video_ids of all videos
            video_urls = get_channel_videos(channel_url)

            # 4. For each video, get transcripts
            for video in video_urls: 
                
            st.write(f"Fetched {len(video_urls)} videos!")
        else:
            st.warning("Enter a valid channel url")