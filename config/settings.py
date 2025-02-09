import os

class Config:
    def __init__(self):
        self.API_KEY = os.getenv('AIzaSyC4XsIDXOhn6SPi2tWu57XWBdxvw9cDfCc')
        self.GENERATION_CONFIGURATION = {
            "temperature": 0.75,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }