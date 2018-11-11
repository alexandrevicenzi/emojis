import unittest

from emojis import emojis
from emojis.db import utils

class TestEmoji(unittest.TestCase):

    def test_encode(self):
        msg = emojis.encode('This is a message with emojis :smile: :heart:')
        self.assertEqual(msg, 'This is a message with emojis 😄 ❤️')

    def test_decode(self):
        msg = emojis.decode('This is a message with emojis 😄 ❤️')
        self.assertEqual(msg, 'This is a message with emojis :smile: :heart:')

    def test_get(self):
        em = emojis.get('Prefix 😄 ❤️ 😄 ❤️ Sufix')
        self.assertEqual(em, {'😄', '❤️'})

    def test_count(self):
        count = emojis.count('😄 ❤️ 😄 ❤️')
        self.assertEqual(count, 4)

    def test_count_uniques(self):
        count = emojis.count('😄 ❤️ 😄 ❤️', True)
        self.assertEqual(count, 2)


class TestDBUtils(unittest.TestCase):

    def test_get_emoji_alias(self):
        aliases = utils.get_emoji_aliases()
        self.assertIsInstance(aliases, dict)
        self.assertTrue(len(aliases) > 0)

    def test_get_emoji_by_code(self):
        em = utils.get_emoji_by_code('😄')
        self.assertEqual(em.aliases[0], 'smile')

    def test_get_emoji_by_alias(self):
        em = utils.get_emoji_by_alias('smile')
        self.assertEqual(em.emoji, '😄')

    def test_get_emojis_by_tag(self):
        emojis = list(utils.get_emojis_by_tag('happy'))
        self.assertTrue(len(emojis) > 0)

    def test_get_emojis_by_invalid_tag(self):
        emojis = list(utils.get_emojis_by_tag('invalid'))
        self.assertEqual(len(emojis), 0)

    def test_get_emojis_by_category(self):
        emojis = list(utils.get_emojis_by_category('People'))
        self.assertTrue(len(emojis) > 0)

    def test_get_emojis_by_category_case_insensitive(self):
        emojis = list(utils.get_emojis_by_category('people'))
        self.assertTrue(len(emojis) > 0)

    def test_get_emojis_by_invalid_category(self):
        emojis = list(utils.get_emojis_by_category('Invalid'))
        self.assertEqual(len(emojis), 0)

    def test_get_tags(self):
        tags = list(utils.get_tags())
        self.assertTrue(len(tags) > 0)

    def test_get_categories(self):
        categories = list(utils.get_categories())
        self.assertTrue(len(categories) > 0)


if __name__ == '__main__':
    unittest.main()
