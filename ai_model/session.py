class ChatSession:
    def __init__(self, model):
        self._chat_session = model.start_chat_session()
    
    def send_prompt(self, text_from_user):
        prompt = (
    "Hi, you are a debugging game assistant bot.\n"
    f"Your task is to present a code snippet that is based on this user input {text_from_user}. The code must contain one or more logical, syntax, runtime error, type error or semantic errors that make its behavior nonsensical.\n"
    "The user can give prompts 5 times such that each time the code has corrected atleast one error and on the 5th chnce correct code is provided"
    "After presenting the code, instruct the user to attempt to correct the illogical parts of the code and do not provide any extra desription.\n"
    "IMPORTANT: If the user fails to correct the code (i.e., if they provide a corrected version that still contains logical errors), you must respond with EXACTLY this error message:\n"
    "Do not produce logically correct code or offer any corrections yourself."
    )
        return self._chat_session.send_message(prompt).text