
class MyException(Exception):
    def __init__(self, arg = ""):
        self.arg = arg

class InvalidXGetUserIdException(MyException):
    def __str__(self):
        return (
            f"REQUEST was FAILED: GETTING USER_ID: {self.arg}"
        )

class InvalidXGetTweetsException(MyException):
    def __str__(self):
        return (
            f"REQUEST was FAILED: GETTING Tweets: {self.arg}"
        )

class InvalidRequestTooManyRequestsException(MyException):
    def __str__(self):
        msg = "REQUEST was FAILED: TOO MANY Tweets: {self.arg}\n"
        msg += "you should wait 15 min to request."
        return msg
