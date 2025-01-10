import streamlit as st
from youtube_transcript import YoutubeTranscript
from ollama import chat
from ollama import ChatResponse

# Título da página
st.title("Youtube Video Summarizer")

# Campo de texto
user_input = st.text_input("Video Link:")

# Botão Enviar
if st.button("Send"):
    if user_input:
        yt_transcript = YoutubeTranscript(video_link=user_input)
        text = yt_transcript.get_transcript()

        prompt = f"""You are an assistant specialized in summarizing YouTube video content clearly and concisely. Whenever you receive a text or transcript of a video, follow these instructions:
                    Language: The summary must always be in English.
                    Format: Use bullet points (-) to list the key points.
                    Content: Extract only the most relevant information, keeping the summary objective and easy to understand.
                    Structure: If the video has clear sections (such as introduction, development, and conclusion), organize the summary according to these parts.
                    Details: Include examples, data, or important quotes if applicable.
                    Length: The summary should have a maximum of 10 bullet points, unless the content is very extensive.
                    Now, summarize the following video content: {text}."""
        
        response: ChatResponse = chat(model='llama3.2', messages=[
            {
                'role': 'user',
                'content': prompt,
            },
        ])
                
        st.write(f"{response.message.content}")
    else:
        st.write("Please paste the video link")