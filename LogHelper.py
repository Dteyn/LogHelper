import logging

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Set the default logging level

# Create a file handler
file_handler = logging.FileHandler('logfile.log')
file_handler.setLevel(logging.DEBUG)  # Set the logging level for the file

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)  # Set the logging level for the console

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Create formatters
info_file_formatter = logging.Formatter('%(asctime)s - %(message)s')
debug_file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

info_console_formatter = logging.Formatter('%(message)s')
debug_console_formatter = logging.Formatter('%(levelname)s - %(message)s')

# Log level to formatter mapping
log_formatter_map = {
    'INFO': (info_file_formatter, info_console_formatter),
    'WARNING': (debug_file_formatter, debug_console_formatter),
    'ERROR': (debug_file_formatter, debug_console_formatter),
    'DEBUG': (debug_file_formatter, debug_console_formatter),
}

def log(message: str, level: str = 'INFO'):
    if message == '-':  # Separator line
        message = '-' * 80

    # Select the appropriate formatter based on the level
    file_formatter, console_formatter = log_formatter_map.get(level.upper(), (info_file_formatter, info_console_formatter))
    file_handler.setFormatter(file_formatter)
    console_handler.setFormatter(console_formatter)

    level_func_map = {
    'INFO': logger.info,
    'WARNING': logger.warning,
    'ERROR': logger.error,
    'DEBUG': logger.debug,
    }

    log_func = level_func_map.get(level.upper(), logger.info)
    log_func(message)
