import streamlit as st
from youtube_transcript import YoutubeTranscript
from langchain_ollama import ChatOllama
from prompts import prompt

st.title("Youtube Video Summarizer")

user_input = st.text_input("Video Link:")

if st.button("Send"):
    if user_input:
        llm = ChatOllama(model = "qwen2.5")
        yt_transcript = YoutubeTranscript(video_link=user_input)
        text = yt_transcript.get_transcript()
        video_name = yt_transcript.get_youtube_video_title()
        
        messages = [
            ("system", prompt),
            ("human", text),
        ]
        res = llm.invoke(messages)
        st.markdown(f"# {video_name}")
        st.markdown(f"{res.content}")
        st.download_button(
            label="Download Notes",
            data=res.content, 
            file_name=f"{video_name}.txt", 
            mime="text/plain"         
        )
    else:
        st.write("Please paste the video link")