class ChatSession:
    def __init__(self, model):
        self._chat_session = model.start_chat_session()
        print('I am here in ChatSession')
    
    def send_prompt(self, text_from_user):
        prompt = (
    "Hi, you are a debugging game assistant bot.\n"
    "Your task is to present a code snippet that is intentionally illogical. The code must be syntactically valid but contain one or more logical flaws that make its behavior nonsensical.\n"
    "After presenting the code, instruct the user to attempt to correct the illogical parts of the code.\n"
    "IMPORTANT: If the user fails to correct the code (i.e., if they provide a corrected version that still contains logical errors), you must respond with EXACTLY this error message:\n"
    "Status Code: 418. I am not equipped with such information please ask - Mr. Dilip Chaudhary\n\n"
    "Do not produce logically correct code or offer any corrections yourself."
    )
        try:
            print('I am in Try')
            response = self._chat_session.send_message(prompt)
            print(response)
            expected_error_message = ("Status Code: 418. I am not equipped with such information please ask -"
                                      " Mr. Dilip Chaudhary")
            
            if response.text.strip() == expected_error_message: return expected_error_message
            return response.text
        except Exception as e: return f'An error occured: {str(e)}'