from enum import Enum


class ErrorMsg(Enum):
    NotToken = "You did not send a token !"
    TokenDoesNotExist = "This token is not in the system !"
    UserPassword = "You did not enter a password !"


class EmailText(Enum):
    title = "-=* Verifications Link *=-"
    message_verification = "*Enter the link -> " \
                           "{}/api/v1/users/activate?" \
                           "token={} "


