class ChatSession:
    def __init__(self, model):
        self._chat_session = model.start_chat_session()
        self.model = model  # Store the AIModel instance

    def send_prompt(self, text_from_user):
        self.model.increment_attempts()  # Update attempts
        attempts = self.model.attempts  # Get updated count

        if attempts == 0:
            return "The debugging game is over. Thank you for playing!"

        prompt = f"""
        You are *strictly* a debugging assistant bot. Your task is to generate Python code snippets based on user requests. 
        You *must* follow the instructions precisely. The generated code *must* contain errors until attempt 4.
        Provide correct code on 5th attempt.
        The code *must* contain one or more errors: logical, syntax, runtime, type, or semantic, that make its behavior nonsensical or incorrect.
        The user's request is: {text_from_user}
        This is attempt number: {attempts}.Each time print the attempt number to let the user know. Remember that the code has to have errors until attempt number 5.
        Do not give comments describing the error in the code snippet.
        """

        response = self._chat_session.send_message(prompt).text
        return response
