import google.generativeai as genai
from config.settings import Config

c = Config()

class AIModel:
    def __init__(self):
        genai.configure(api_key=c.API_KEY)
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=c.GENERATION_CONFIGURATION,
        )
        self.chat_history = []
    
    def start_chat_session(self):
        return self.model.start_chat(history=[self.chat_history])

    def add_to_history(self, prompt, response):
        self.chat_history.append({"role": "user", "parts": [prompt]})
        self.chat_history.append({"role": "model", "parts": [response]})