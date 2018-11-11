# Emojis

Emojis for Python

## About

This library allows you to emojify content such as: _This is a message with emojis :smile: :heart:_

See the [Emoji cheat sheet](http://www.emoji-cheat-sheet.com/) for more aliases.

Emoji database based on [gemoji](https://github.com/github/gemoji).

## Example

```python
>>> import emojis

>>>  emojis.encode('This is a message with emojis :smile: :heart:')
'This is a message with emojis 😄 ❤️'

>>> emojis.decode('This is a message with emojis 😄 ❤️')
'This is a message with emojis :smile: :heart:'

>>> emojis.get('Prefix 😄 ❤️ 😄 ❤️ Sufix')
{'😄', '❤️'}

>> emojis.count('😄 ❤️ 😄 ❤️')
4

>>> emojis.count('😄 ❤️ 😄 ❤️', unique=True)
2
```

## Installation

Install `emojis` with `pip`.

`pip3 install -U emojis`

## License

MIT
