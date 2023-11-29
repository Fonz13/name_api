import fastapi
import time
from pydantic import BaseModel

class chatRequest(BaseModel):
    VideoID: str
    Message: str
    
class chatResponse(BaseModel):
    Status: str
    Message: str
    
router = fastapi.APIRouter()
    
@router.post("/chat/")
def chat(chat_request: chatRequest):
    return_message = "Chat request received"
    time.sleep(1)
    return chatResponse(**{"Status": "OK", "Message": return_message})
