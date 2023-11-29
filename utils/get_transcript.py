from youtube_transcript_api import YouTubeTranscriptApi
import os


def get_transcript(video_url):
    try:
        video_id = video_url.split("watch?v=")[1]
    except:
        return {"Status":"Error","Message":"Invalid URL"}
    
    try:
        srt = YouTubeTranscriptApi.get_transcript(video_id)
    except:
        return {"Status": "Error", "Message": "Transcript not found"}
        # implement audio to text generation here

    
    transcript = {}

    with open(f"api/db/{video_id}.txt", "w") as file:
        for i in srt:
            file.write(i["text"] + "\n")

    return {"Status":"OK", "Message": "Transcript created", "VideoID" : video_id}