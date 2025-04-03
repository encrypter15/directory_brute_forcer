#!/usr/bin/env python3
# Directory Brute Forcer
# Author: Rick Hayes
# License: MIT
# Version: 2.73
# README: Requires internet. Tests directories against a base URL using a wordlist.

import requests
import argparse
import logging
import json
from typing import List

def setup_logging():
    """Configure logging to file."""
    logging.basicConfig(filename='directory_brute_forcer.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def load_config(config_file: str) -> dict:
    """Load configuration from JSON file."""
    try:
        with open(config_file, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logging.error(f"Config loading failed: {e}")
        return {"timeout": 5.0}

def load_wordlist(wordlist_file: str) -> List[str]:
    """Load words from the wordlist file."""
    try:
        with open(wordlist_file, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except (FileNotFoundError, IOError) as e:
        logging.error(f"Wordlist loading failed: {e}")
        return []

def test_directory(base_url: str, directory: str, timeout: float) -> bool:
    """Test if a directory exists."""
    url = f"{base_url.rstrip('/')}/{directory}"
    try:
        response = requests.get(url, timeout=timeout)
        return response.status_code == 200
    except requests.RequestException as e:
        logging.error(f"Request failed for {url}: {e}")
        return False

def main():
    """Main function to parse args and brute force directories."""
    parser = argparse.ArgumentParser(description="Directory Brute Forcer")
    parser.add_argument("--url", required=True, help="Base URL to test (e.g., http://example.com)")
    parser.add_argument("--wordlist", required=True, help="Path to wordlist file")
    parser.add_argument("--config", default="config.json", help="Config file path")
    args = parser.parse_args()

    setup_logging()
    config = load_config(args.config)
    wordlist = load_wordlist(args.wordlist)

    if not wordlist:
        print("Error: Could not load wordlist")
        return

    logging.info(f"Starting directory brute force on {args.url}")
    for directory in wordlist:
        if test_directory(args.url, directory, config["timeout"]):
            logging.info(f"Found directory: {args.url}/{directory}")
            print(f"Found: {args.url}/{directory}")
        else:
            logging.debug(f"Directory not found: {directory}")

if __name__ == "__main__":
    main()
