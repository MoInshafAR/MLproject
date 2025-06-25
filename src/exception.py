import sys
import logging

def error_message_detail(error,error_detail:sys):
    """
    This function returns a detailed error message.
    """
    _,_,exc_tb = error_detail.exc_info()  # Extract the exception traceback
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get the file name where the exception occurred
    error_message = f"Error occurred in script: [{file_name}] at line number: [{exc_tb.tb_lineno}] error message: [{str(error)}]"
    return error_message

class CustomException(Exception):
    """
    Custom exception class that inherits from the built-in Exception class.
    It provides a detailed error message when an exception occurs.
    """
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)  # Call the base class constructor with the error
        self.error_message = error_message_detail(error_message, error_detail=error_detail)  # Get the detailed error message

    def __str__(self):
        return self.error_message  # Return the detailed error message as a string
    
        