import google.generativeai as genai
from config.settings import Config
from ast import literal_eval

c = Config()

class AIModel:
    def __init__(self):
        genai.configure(api_key=c.API_KEY)
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=c.GENERATION_CONFIGURATION,
        )
    
    def _load_chat_history(file_path='history.txt'):
        history = []
        with open('history.txt') as fp:
            for line in fp: history = [literal_eval(line.strip()) for line in fp]
        return history

    def start_chat_session(self):
        self.chat_history = self._load_chat_history()
        print('*' * 50)
        print(self.chat_history)
        print('*' * 50)
        return self.model.start_chat(history=self.chat_history)