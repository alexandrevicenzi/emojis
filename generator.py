import argparse
import os

from datetime import datetime

import requests

GEMOJI_RELEASE_URL = 'https://api.github.com/repos/github/gemoji/releases'
GEMOJI_JSON_DB_URL = 'https://raw.githubusercontent.com/github/gemoji/{tag}/db/emoji.json'


def get_lastest_release():
    req = requests.get(GEMOJI_RELEASE_URL)
    req.raise_for_status()

    data = req.json()

    latest = data[0]

    return latest['tag_name'], latest['name']


def generate(path, dbname):
    tag, name = get_lastest_release()

    req = requests.get(GEMOJI_JSON_DB_URL.format(tag=tag))
    req.raise_for_status()

    data = req.json()

    path = os.path.join(path, dbname)

    with open(path, 'w', encoding='utf-8') as file:
        file.write('### This is a generated file.\n')
        file.write('### Do not edit this file.\n')
        file.write('### Date: {0}\n'.format(datetime.now().isoformat()[:-7]))
        file.write('### This file is based on {0}.\n'.format(name))
        file.write('\n')
        file.write('from collections import namedtuple\n')
        file.write('\n')
        file.write('Emoji = namedtuple("Emoji", ["aliases", "emoji", "tags", "category", "unicode_version"])\n')
        file.write('\n')
        file.write('EMOJI_DB = [\n')

        for emoji in data:
            if 'emoji' in emoji:
                file.write('    Emoji({aliases}, "{emoji}", {tags}, "{category}", "{unicode_version}"),\n'.format(**{
                    'aliases': emoji['aliases'],
                    'emoji': emoji['emoji'],
                    'tags': emoji['tags'],
                    'category': emoji['category'],
                    'unicode_version': emoji['unicode_version'],
                }))

        file.write(']\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generates the Emoji database')
    parser.add_argument('--dir', default='./emojis', help='Database location')
    parser.add_argument('--dbname', default='emojidb.py', help='Database location')
    args = parser.parse_args()

    generate(args.dir, args.dbname)