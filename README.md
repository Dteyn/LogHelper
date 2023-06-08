# LogHelper

LogHelper is a Python utility for logging, designed to enhance the debugging and monitoring process. It can output logs to both the console and a file, with formats that can be customized based on log levels. The utility is contained in a single script, `LogHelper.py`.

## Features

- INFO, WARNING, ERROR, and DEBUG log levels.
- Outputs to both console and file (`logfile.log`).
- Customizable message format based on log level.
- Console output does not include timestamps to keep logs clean, while file output does for precise logging.
- Uses Python's built-in logging module, ensuring compatibility and reliability.

## Usage

1. Download [LogHelper.py](LogHelper.py) and place it in the same directory as your Python script.

2. Import the `log` function from `LogHelper.py` in your Python script:

```python
from LogHelper import log
```

3. You can now use the log function to log messages at different levels. The level should be passed as a string and can be 'INFO', 'WARNING', 'ERROR', or 'DEBUG'. If no level is specified, 'INFO' is used by default.

```python
log('This is an info message')
log('This is a warning message', 'WARNING')
log('This is an error message', 'ERROR')
log('This is a debug message', 'DEBUG')
```

The `log` function will output the message to both the console and the `logfile.log` file with the appropriate format. You can change the name of `logfile.log` by editing the Python script.

### Seperator line shortcut

You can also print an 80-character seperator line by using:

```python
log('-')
```

## Example Output

Console output:
```
This is an info message
WARNING - This is a warning message
ERROR - This is an error message
DEBUG - This is a debug message
```

File output:
```
2023-06-08 12:04:48,227 - This is an info message
2023-06-08 12:04:48,227 - WARNING - This is a warning message
2023-06-08 12:04:48,228 - ERROR - This is an error message
2023-06-08 12:04:48,228 - DEBUG - This is a debug message
```


## Requirements
* Python 3.6 or later.

## Importing and Conflict Avoidance

The `math` module in Python also includes a `log()` function. If you import the math module, there could be a conflict with LogHelper's `log()` function if both are used in the same namespace.

To avoid such conflicts, it is recommended to import modules in a way that keeps their functions within their own namespace. For example, the `log()` function from the `math` module can be imported and used as follows:

```python
import math
math.log(10)
```

Similarly, LogHelper's log() function can be imported in the following way:

```python
import LogHelper
LogHelper.log('This is a message')
```

If you want to use LogHelper's log() function directly, you can use an alias to avoid any potential conflicts:

```python
from LogHelper import log as log_helper
log_helper('This is a message')
```

With this approach, even if there is another log() function in the same namespace from another import, LogHelper's log() function will not conflict because it has been aliased to log_helper. You should be mindful of how you import and use the log() function to avoid any potential conflicts.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributions

Contributions are very welcome! If you'd like to contribute, feel free to open an issue or create a pull request. 

When you're creating a pull request, please:

- Ensure your code is commented, tested, and includes any relevant documentation updates.
- Provide a brief explanation of the changes you've made.
- Reference any related issues in your pull request message.

Thank you in advance for your contributions!
