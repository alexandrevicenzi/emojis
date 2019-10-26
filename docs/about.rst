About
-----

This library allows you to emojify content such as:

``This is a message with emojis :smiling-face: :snake:``

See the `Emoji cheat sheet <http://unicode.org/emoji/charts/full-emoji-list.html>`__ for a
full list of emojis.

.. code:: python

    >>> import emojis

    >>> emojis.encode('This is a message with emojis :smiling-face: :snake:')
    'This is a message with emojis 😄 🐍'
