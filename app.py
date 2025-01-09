import streamlit as st
from youtube_transcript import YoutubeTranscript

# Título da página
st.title("Youtube Video Summarizer")

# Campo de texto
user_input = st.text_input("Video Link:")

# Botão Enviar
if st.button("Send"):
    if user_input:
        yt_transcript = YoutubeTranscript(video_link=user_input)
        
        st.write(f"Transcript: {yt_transcript.get_transcript()}")
    else:
        st.write("Please paste the video link")