# imessage
Python tools for sending iMessage/SMS message from a Mac. Check out the blog post on medium related to this repository: [Medium](https://medium.com/@jameskabbes/sending-imessages-with-python-on-a-mac-b77b7dd6e371)

[PyPI](https://pypi.org/project/kabbes-imessage)

<br> 

# Installation
`pip install pyimessage`

<br>

# Running main

```
python -m pyimessage
```

<br>

# Usage


```python
import kabbes_imessage
```

## Basic Usage
Check out `utils.py` for the most basic functionality

```python
kabbes_imessage.send( 'This is a test message', '123-555-5555','iMessage' )
```
```python
kabbes_imessage.send_SMS( 'This is a test message', '123-555-5555' )
```

```python
kabbes_imessage.send_iMessage( 'This is a test message', '123-555-5555' )
```

<br>

# Author
James Kabbes

