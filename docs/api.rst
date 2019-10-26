.. _api:

Emojis Library
===================

This part of the documentation covers all Emojis library functions.

Sample Code
-----------

.. code:: python

    >>> import emojis

    >>> emojis.encode('This is a message with emojis :smiling-face: :snake:')
    'This is a message with emojis 😄 🐍'

    >>> emojis.decode('This is a message with emojis 😄 🐍')
    'This is a message with emojis :smile: :snake:'

    >>> emojis.get('Prefix 😄 🐍 😄 🐍 Sufix')
    {'😄', '🐍'}

    >>> emojis.count('😄 🐍 😄 🐍')
    4

    >>> emojis.count('😄 🐍 😄 🐍', unique=True)
    2

    >>> emojis.db.get_emoji_by_alias('snake')
    Emoji(aliases=['snake'], emoji='🐍', tags=[], category='Animals & Nature')

    >>> emojis.db.get_categories()
    {'Activities', 'Travel & Places', 'Smileys & Emotion', 'Symbols', 'Food & Drink', 'Animals & Nature', 'People & Body', 'Objects', 'Flags'}


Main Functions
--------------

.. module:: emojis

.. autofunction:: encode
.. autofunction:: decode
.. autofunction:: get
.. autofunction:: count

Database Functions
------------------

.. module:: emojis.db

.. autofunction:: get_emoji_aliases
.. autofunction:: get_emoji_by_code
.. autofunction:: get_emoji_by_alias
.. autofunction:: get_emojis_by_tag
.. autofunction:: get_emojis_by_category
.. autofunction:: get_tags
.. autofunction:: get_categories
