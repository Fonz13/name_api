import fastapi
from api.utils.get_transcript import get_transcript
import time
from pydantic import BaseModel
from typing import Optional


class videoURL(BaseModel):
    URL: str
    
class urlResponse(BaseModel):
    Status: str
    Message: str
    VideoID: Optional[str] = None


router = fastapi.APIRouter()


@router.post("/create-summary/")
def create_summary(video_url: videoURL):
    time.sleep(1)
    return_message = get_transcript(video_url.URL)
    return urlResponse(**return_message)
