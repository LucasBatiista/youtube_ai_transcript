from youtube_transcript import YoutubeTranscript

yt_transcript = YoutubeTranscript(video_link='https://www.youtube.com/watch?v=iJv25jws7qo&t')

print(yt_transcript.get_transcript())