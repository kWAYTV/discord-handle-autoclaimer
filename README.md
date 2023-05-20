# Discord handle autoclaimer

Python script designed to autoclaim discord handles.

## ⚠️ Disclaimer

This script may put your account at risk for temporary (or possibly permanent) terminations. It is recommended to use an alt account to stay safe.

## Requirements

- Python 3.6+
- Required Python libraries: `requests`, `json`, `threading`, `colorama`, `urllib3`
- The following text files with each entry on a new line:
  - `tokens.txt`: A list of your Discord token(s).
  - `words.txt`: A list of usernames to be claimed.
  - `proxies.txt`: A list of proxies to use for requests.

## Usage

1. Ensure you have Python 3.6+ installed and the necessary libraries. You can install the libraries with pip:

```shell
pip install -r requirements.txt
```

2. Create `tokens.txt`, `words.txt`, and `proxies.txt` in the same directory as the script, and fill them with your data.
3. Run the script with Python:

```shell
python main.py
```

The script will run indefinitely, making requests to the specified endpoint using the provided tokens, usernames, and proxies.
