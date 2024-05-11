from decorations import *
class InvalidUsernameError(Exception):
    def __str__(self):
        return f"{red_in}\nInvalid Username!\U0001F615 Enter Username & Password Carefully...{out}"
    
class InvalidPasswordError(Exception):
    def __str__(self):
        return f"{red_in}\nInvalid Password!\U0001F615 Enter Username & Password Carefully...{out}"
    
class InvalidChoiceError(Exception):
    def __str__(self):
        return f"{red_in}\nPlease enter valid choice{out}"

class InsufficientPaymentError(Exception):
    def __str__(self):
        return f"{red_in}\nPlease pay total billing amount to recieve Movie tickes \U0001F3AB{out}"
      
        