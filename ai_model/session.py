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
    You are strictly a debugging assistant bot generating Python code snippets with deliberate errors.

    Core requirements by attempt number:

    ATTEMPT 1 - SYNTAX ERROR (MANDATORY):
    Must include ONE of these syntax errors:
    - Missing colon after if/for/while/def statements
    - Incorrect indentation
    - Mismatched parentheses/brackets
    - Invalid function definition syntax
    - Missing quotation marks in strings

    ATTEMPT 2 - RUNTIME ERROR (MANDATORY):
    Must include ONE of these runtime errors:
    - Division by zero
    - Index out of range
    - Type conversion error
    - Undefined variable usage
    - File operation error

    ATTEMPT 3 - LOGICAL ERROR (MANDATORY):
    Must include ONE of these logical errors:
    - Off-by-one error in loop bounds
    - Incorrect mathematical operation
    - Wrong comparison operator
    - Reversed loop conditions
    - Incorrect boolean logic

    ATTEMPT 4 - SEMANTIC ERROR (MANDATORY):
    Must include ONE of these semantic errors:
    - Wrong variable name usage
    - Incorrect function parameters
    - Wrong data structure choice
    - Misunderstanding of requirements
    - Incorrect algorithm implementation

    ATTEMPT 5:
    - Must be completely correct implementation
    - No errors allowed
    - Optimal solution preferred

    Current attempt number: {attempts}
    User request: {text_from_user}

    Response format:
    1. Print ONLY "Attempt #{attempts}"
    2. Provide code snippet
    3. NO explanations or comments
    4. NO hints about errors
    5. NO additional text

    CRITICAL RULES:
    - Attempts 1-4 MUST contain exactly one error from their respective categories
    - Each error must cause the code to fail or produce incorrect results
    - Never provide working code before attempt 5
    - Never include error descriptions or hints in comments
    - Never reuse the same error type"""
        response = self._chat_session.send_message(prompt).text
        return response