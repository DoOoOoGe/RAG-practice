from langchain_community.chat_message_histories import FileChatMessageHistory
import os

class ChatHistoryManager:
    def __init__(self, dir: str, session_id: str):
        self.dir = dir
        self.session_id = session_id
        self.path = os.path.join(dir, session_id)

        os.makedirs(self.dir, exist_ok=True)
    
        self.file_history = FileChatMessageHistory(self.path, encoding="utf-8")
    
    def clear(self):
        os.remove(self.path)