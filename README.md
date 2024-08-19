# imessage

Python tools for sending iMessage/SMS message from a Mac. Check out the blog post on medium related to this repository: [Medium](https://medium.com/@jameskabbes/sending-imessages-with-python-on-a-mac-b77b7dd6e371)

[Documentation](https://jameskabbes.github.io/imessage) <br>
[PyPI](https://pypi.org/project/pyimessage)

<br>

# Installation

`pip install mac_imessage`

<br>

# Running main

```
python -m mac_imessage
```

<br>

# Usage

```python
import mac_imessage
```

## Basic Usage

Check out `utils.py` for the most basic functionality

```python
mac_imessage.send(
    message='This is a test message',
    phone_number='123-555-5555',
    medium='iMessage'
    )
```

```python
mac_imessage.send_sms(
    message='This is a test message',
    phone_number='123-555-5555',
    )
```

```python
mac_imessage.send_imessage(
    message='This is a test message',
    phone_number='123-555-5555',
    )
```

<br>

# Author

James Kabbes
