class ChatSession:
    def __init__(self, model):
        self._chat_session = model.start_chat_session()
    
    def send_prompt(self, text_from_user):
       prompt = (
    "Hi, you are a debugging game assistant bot.\n"
    f"Your task is to present a code snippet that is based on this user input: {text_from_user}. The code *must* contain one or more errors: logical, syntax, runtime, type, or semantic, that make its behavior nonsensical or incorrect.  Do not include any explanation of the errors.\n"
    "The user will have 5 attempts to correct the code. Each subsequent code snippet you provide should have at least one error corrected by the user in the previous attempt, while still containing at least one new or remaining error. On the 5th attempt, provide a completely correct and logically sound version of the code.\n"
    "After presenting the code, instruct the user to attempt to correct the illogical parts of the code.  Provide *no* hints, explanations, or descriptions of the errors.  Only provide the code.\n"
    "IMPORTANT: If the user fails to correct the code (i.e., if they provide a corrected version that still contains errors, or if they provide code that does not build upon their previous attempt), you must respond with *ONLY* this exact error message (and nothing else):\n"
    "Do not produce logically correct code or offer any corrections yourself."
             )
       return self._chat_session.send_message(prompt).text