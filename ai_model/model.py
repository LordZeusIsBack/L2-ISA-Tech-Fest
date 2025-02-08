import google.generativeai as genai
from config.settings import Config
from ast import literal_eval
import os

c = Config()

class AIModel:
    def __init__(self):
        genai.configure(api_key=c.API_KEY)
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=c.GENERATION_CONFIGURATION,
        )
        self.attempts = self._load_attempts()  # Load attempts count from file

    def _load_chat_history(self, file_path='history.txt'):
        """Load previous chat history from a file."""
        history = []
        if os.path.exists(file_path):
            with open(file_path, 'r') as fp:
                for line in fp:
                    history.append(literal_eval(line.strip()))
        return history

    def _load_attempts(self, file_path='attempts.txt'):
        """Load attempts count from a file."""
        if os.path.exists(file_path):
            with open(file_path, 'r') as fp:
                try:
                    return int(fp.read().strip())
                except ValueError:
                    return 0
        return 0  # Default to 0 if file doesn't exist

    def _save_attempts(self, file_path='attempts.txt'):
        """Save the current attempts count to a file."""
        with open(file_path, 'w') as fp:
            fp.write(str(self.attempts))

    def start_chat_session(self):
        """Start a chat session while maintaining the attempt count."""
        self.chat_history = self._load_chat_history()
        print('*' * 50)
        print(self.chat_history)
        print('*' * 50)
        return self.model.start_chat(history=self.chat_history)

    def increment_attempts(self, file_path='attempts.txt'):
        """Increment attempts and reset when the game ends."""
        if self.attempts >= 5:
            self.attempts = 0  # Reset after game ends
        else:
            self.attempts += 1

        self._save_attempts()  # Save new value