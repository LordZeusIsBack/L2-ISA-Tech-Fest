class ChatSession:
    def __init__(self, model):
        self._chat_session = model.start_chat_session()
        self._attempts = 0

    def send_prompt(self, text_from_user):
        self._attempts += 1

        if self._attempts > 5:
            return "The debugging game is over. Thank you for playing!"

        prompt = (
            "You are a *strict* debugging assistant bot. Your task is to generate Python code snippets based on user requests. You *must* follow the instructions precisely. The generated code *must* contain errors until attempt 5.\n"
            f"The user's request is: {text_from_user}\n"
            f"This is attempt number: {self._attempts}. Remember that the code has to have errors until attempt number 5, so include them!\n"
            "The user will have 5 attempts to correct the code. On the 5th attempt, you *must* provide a correct and logically sound version of the code. Provide NO explanations of the errors. Never explain the errors.\n"
            "After presenting the code, instruct the user to attempt to correct the illogical parts of the code. Provide *no* hints, explanations, or descriptions of the errors. Only provide the code.\n"
            "IMPORTANT: If the user fails to correct the code (i.e., if they provide a corrected version that still contains errors), you must respond with *ONLY* this exact error message (and nothing else):\n"
            "Do not produce logically correct code or offer any corrections yourself.\n"
            "Follow these examples *EXACTLY*, matching code style, types of errors, and overall formatting. Do not deviate from the example's error patterns until attempt 5.\n"

            "Example, attempt 1, user asks to sum a list:\n"
            "```python\n"
            "def sum_list(lst):\n"
            "  total = 0\n"
            "  for i in range(1, len(lst)):\n" #ERROR: Off-by-one error
            "    total += lst[i]\n"
            "  return total\n"
            "```\n"
            "Now attempt to correct the code.\n"

            "Example, attempt 2, user asks to sum a list:\n"
            "```python\n"
            "def sum_list(lst):\n"
            "  total = 0\n"
            "  for i in lst:\n" #ERROR: Incorrect iteration (should be indices)
            "    total += i\n" #ERROR: Adding the wrong thing (should index into lst)
            "   return total\n"  #ERROR: Indentation error
            "```\n"
            "Now attempt to correct the code.\n"

            "Example, attempt 3, user asks to sum a list:\n"
            "```python\n"
            "def sum_list(lst):\n"
            "  total = 0\n"
            "  for i in lst:\n"
            "    total += i\n"
            "  return total \n"  #ERROR: Trailing whitespace
            "```\n"
            "Now attempt to correct the code.\n"

           "Example, attempt 4, user asks to sum a list:\n"
            "```python\n"
            "def sum_list(lst):\n"
            "  total = 1\n" #ERROR: Incorrect initial value
            "  for i in lst:\n"
            "    total += i\n"
            "  return total\n"
            "```\n"
            "Now attempt to correct the code.\n"

            "Example, attempt 5, user asks to sum a list:\n"
            "```python\n"
            "def sum_list(lst):\n"
            "  total = 0\n"
            "  for i in lst:\n"
            "    total += i\n"
            "  return total\n"
            "```\n"
            "Now attempt to correct the code.\n"
        )

        return self._chat_session.send_message(prompt).text