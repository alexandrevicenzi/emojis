import re

from .db import utils

ALIAS_TO_EMOJI = utils.get_emoji_aliases()
EMOJI_TO_ALIAS = dict((v, k) for k, v in ALIAS_TO_EMOJI.items())

RE_TEXT_TO_EMOJI_GROUP = '|'.join(['({0})'.format(alias) for alias in ALIAS_TO_EMOJI])
RE_TEXT_TO_EMOJI = re.compile(RE_TEXT_TO_EMOJI_GROUP)

RE_EMOJI_TO_TEXT_GROUP = '|'.join(['({0})'.format(re.escape(emoji)) for emoji in EMOJI_TO_ALIAS])
RE_EMOJI_TO_TEXT = re.compile(RE_EMOJI_TO_TEXT_GROUP)


def encode(msg):
    msg = RE_TEXT_TO_EMOJI.sub(lambda match: ALIAS_TO_EMOJI[match.group(0)], msg)
    return msg


def decode(msg):
    msg = RE_EMOJI_TO_TEXT.sub(lambda match: EMOJI_TO_ALIAS[match.group(0)], msg)
    return msg


def get(msg):
    return {match.group() for match in  RE_EMOJI_TO_TEXT.finditer(msg)}


def count(msg, unique=False):
    if unique:
        return len({match.group() for match in  RE_EMOJI_TO_TEXT.finditer(msg)})
    return len([match.group() for match in  RE_EMOJI_TO_TEXT.finditer(msg)])
