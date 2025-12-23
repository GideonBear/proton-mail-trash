# proton-mail-trash

`proton-mail-trash` will permanently delete all messages in your Proton Mail trash that are older than 30 days. Note
that **this is not the same as deleting messages that have been in the trash for more than 30 days**.

Works on Linux and Windows!

## Installation

Requires `git` to be installed

```bash
# Using uv (will automatically install Python if necessary):
uv tool install proton-mail-trash
# Using pipx:
pipx install proton-mail-trash
# Using pip:
pip install proton-mail-trash
```

## Usage

```bash
proton-mail-trash
```

## Python version support

This project will only ever support the latest released minor version of python, but will most likely work on older
versions as well. Change `requires-python` manually in `pyproject.toml` if necessary.

## Disclaimer

Use this software only at your own risk, and review the code if you want to.

This software uses Hydroxide's IMAP support, which is experimental.

This software permanently deletes messages from your Proton Mail account.

This software might not be an allowed use of Proton's products.

## Credits

Only possible thanks
to [Hydroxide, a third-party, open-source ProtonMail CardDAV, IMAP and SMTP bridge](https://github.com/emersion/hydroxide)!
