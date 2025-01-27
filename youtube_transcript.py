from youtube_transcript_api import YouTubeTranscriptApi
import urllib.request
import re

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
        
    def get_transcript_json(self):
        try:
            data = YouTubeTranscriptApi.get_transcript(self.video_code)
            return data
        except Exception as e:
            raise(e)
        
    def get_youtube_video_title(self):
        try:
            response = urllib.request.urlopen(self.video_link)
            html = response.read().decode("utf-8")
            title_match = re.search(r'"title":"(.*?)"', html)
            if not title_match:
                title_match = re.search(r'<title>(.*?) - YouTube</title>', html)

            if title_match:
                title = title_match.group(1)
                title = bytes(title, "utf-8").decode("unicode_escape")
                return title.strip()
            else:
                return "Title not found"

        except Exception as e:
            return f"Error: {str(e)}"
        