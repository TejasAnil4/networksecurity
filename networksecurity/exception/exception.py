import sys
from networksecurity.logging import logger

# class NetworkSecurityException(Exception):
#     def __init__(self,error_message,error_details:sys):
#         self.error_message = error_message
#         _,_,exc_tb = error_details.exc_info()
        
#         self.lineno=exc_tb.tb_lineno
#         self.file_name=exc_tb.tb_frame.f_code.co_filename 
    
#     def __str__(self):
#         return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
#         self.file_name, self.lineno, str(self.error_message))
    
class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details):
        """
        Custom exception class for Network Security errors.

        Args:
            error_message (str): A descriptive message about the error.
            error_details (Exception or str): The exception object or error details.
        """
        self.error_message = error_message
        self.error_details = error_details
        super().__init__(self.error_message)

    def __str__(self):
        """
        Format the error message for display.
        """
        return f"{self.error_message}: {self.error_details}"