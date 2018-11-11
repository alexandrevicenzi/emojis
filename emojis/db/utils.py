from . import db

def get_emoji_aliases():
    emoji_aliases = {}

    for emoji in db.EMOJI_DB:
        for alias in emoji.aliases:
            alias = ':{0}:'.format(alias)
            emoji_aliases[alias] = emoji.emoji

    return emoji_aliases


def get_emoji_by_code(code):
    try:
        return next(filter(lambda emoji: code == emoji.emoji, db.EMOJI_DB))
    except StopIteration:
        return None


def get_emoji_by_alias(alias):
    try:
        return next(filter(lambda emoji: alias in emoji.aliases, db.EMOJI_DB))
    except StopIteration:
        return None


def get_emojis_by_tag(tag):
    return filter(lambda emoji: tag in emoji.tags, db.EMOJI_DB)


def get_emojis_by_category(category):
    return filter(lambda emoji: category.lower() == emoji.category.lower(), db.EMOJI_DB)


def get_tags():
    return sorted({tag for emoji in db.EMOJI_DB for tag in emoji.tags})

def get_categories():
    return sorted({emoji.category for emoji in db.EMOJI_DB})
