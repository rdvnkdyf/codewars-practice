def decode(message):
    return ''.join(
        chr(219 - ord(c)) if c.isalpha() else c
        for c in message
    )