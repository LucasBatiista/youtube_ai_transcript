from youtube_transcript_api import YouTubeTranscriptApi


class YoutubeTranscript():
    def __init__(self, video_link):
        self.video_link = video_link
        self.video_code = self.get_youtube_video_code()
    
    def get_youtube_video_code(self):
        try:
            video_code = self.video_link.split("v=")[1].split("&")[0]
            return video_code
        except IndexError:
            return None
        
    def get_transcript(self):
        try:
            result = YouTubeTranscriptApi.get_transcript(self.video_code)
            full_text = " ".join([entry['text'] for entry in result])
            return full_text
        except Exception as e:
            raise(e)