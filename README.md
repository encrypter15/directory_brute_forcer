# Directory Brute Forcer

## Overview
The Directory Brute Forcer is a Python tool that tests for the existence of directories on a web server by appending words from a wordlist to a base URL. It uses the `requests` library to send HTTP GET requests and identifies accessible directories based on a 200 status code.

## Author
Rick Hayes

## License
MIT

## Version
2.73

## Requirements
- Python 3.x
- `requests` library (`pip install requests`)
- Internet access

## Usage
Run the script from the command line with the following arguments:

```bash
python3 directory_brute_forcer.py --url <BASE_URL> --wordlist <WORDLIST_FILE> [--config <CONFIG_FILE>]
