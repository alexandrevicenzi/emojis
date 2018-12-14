About
-----

This library allows you to emojify content such as:

``This is a message with emojis :smile: :snake:``

See the `Emoji cheat sheet <http://www.emoji-cheat-sheet.com/>`__ for
a complete list of aliases.

.. code:: python

    >>> import emojis

    >>> emojis.encode('This is a message with emojis :smile: :snake:')
    'This is a message with emojis 😄 🐍'
