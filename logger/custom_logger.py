import logging
import os
from datetime import datetime

class CustomLogger:
    def __init__(self,log_dir="logs"):
        # Ensure logs directory exists
        self.logs_dir = os.path.join(os.getcwd(), log_dir)
        os.makedirs(self.logs_dir, exist_ok=True)

        # Create timestamped log file name
        log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
        log_file_path = os.path.join(self.logs_dir, log_file)

        # Configure logging
        logging.basicConfig(
            filename=log_file_path,
            format="[ %(asctime)s ] %(levelname)s %(name)s (line:%(lineno)d) - %(message)s",
            level=logging.INFO,
        )
        
    def get_logger(self,name=__file__):
        return logging.getLogger(os.path.basename(name))
    
if __name__ == "__main__":
    logger=CustomLogger()
    logger=logger.get_logger(__file__)
    logger.info("Custom logger initialized.")

# class CustomLogger:
#     def __init__(self, log_dir="logs"):
#         # Ensure logs directory exists
#         self.logs_dir = os.path.join(os.getcwd(), log_dir)
#         os.makedirs(self.logs_dir, exist_ok=True)

#         # Create timestamped log file
#         log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
#         self.log_file_path = os.path.join(self.logs_dir, log_file)

#     def get_logger(self, name=__file__):
#         """
#         Returns a logger instance with file + console handlers.
#         Default name is the current file name (without path).
#         """
#         logger_name = os.path.basename(name)
#         logger = logging.getLogger(logger_name)
#         logger.setLevel(logging.INFO)

#         # Formatter for both handlers
#         file_formatter = logging.Formatter(
#             "[ %(asctime)s ] %(levelname)s %(name)s (line:%(lineno)d) - %(message)s"
#         )
#         console_formatter = logging.Formatter(
#             "[ %(levelname)s ] %(message)s"
#         )

#         # File handler (logs saved to file)
#         file_handler = logging.FileHandler(self.log_file_path)
#         file_handler.setFormatter(file_formatter)

#         # Console handler (logs printed on terminal)
#         console_handler = logging.StreamHandler()
#         console_handler.setFormatter(console_formatter)

#         # Avoid duplicate handlers if logger is reused
#         if not logger.handlers:
#             logger.addHandler(file_handler)
#             logger.addHandler(console_handler)

#         return logger


# # --- Usage Example ---
# if __name__ == "__main__":
#     logger = CustomLogger().get_logger(__file__)  # Logger will use file name as its name
#     logger.info("Logger initialized successfully.")
        