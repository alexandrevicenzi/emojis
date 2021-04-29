import unittest

from emojis import emojidb, text, utils

class TestEmoji(unittest.TestCase):

    def test_encode(self):
        msg = text.encode('This is a message with emojis :smile: :heart:')
        self.assertEqual(msg, 'This is a message with emojis 😄 ❤️')

    def test_encode_aliases(self):
        msg1 = text.encode(':+1:')
        msg2 = text.encode(':thumbsup:')
        self.assertEqual(msg1, msg2)

    def test_decode(self):
        msg = text.decode('This is a message with emojis 😄 ❤️')
        self.assertEqual(msg, 'This is a message with emojis :smile: :heart:')

    def test_decode_aliases(self):
        msg = text.decode('👍')
        self.assertTrue(msg in [':+1:', ':thumbsup:'])

    def test_get(self):
        emoji = text.get('Prefix 😄 ❤️ 😄 ❤️ Sufix')
        self.assertEqual(emoji, {'😄', '❤️'})

    def test_get_multi_character(self):
        emoji = text.get('Prefix 👨‍🎓 👨‍🎓 Sufix')
        self.assertEqual(emoji, {'👨‍🎓'})

    def test_count(self):
        count = text.count('😄 ❤️ 😄 ❤️')
        self.assertEqual(count, 4)

    def test_count_uniques(self):
        count = text.count('😄 ❤️ 😄 ❤️', True)
        self.assertEqual(count, 2)


class TestDBUtils(unittest.TestCase):

    def test_get_emoji_alias(self):
        aliases = utils.get_emoji_aliases()
        self.assertIsInstance(aliases, dict)
        self.assertTrue(len(aliases) > 0)

    def test_get_emoji_by_code(self):
        emoji = utils.get_emoji_by_code('😄')
        self.assertIsInstance(emoji, emojidb.Emoji)
        self.assertEqual(emoji.aliases[0], 'smile')

    def test_get_emoji_by_alias(self):
        emoji = utils.get_emoji_by_alias('smile')
        self.assertIsInstance(emoji, emojidb.Emoji)
        self.assertEqual(emoji.emoji, '😄')

    def test_get_emojis_by_tag(self):
        emoji_list = list(utils.get_emojis_by_tag('happy'))
        self.assertTrue(len(emoji_list) > 0)

    def test_get_emojis_by_invalid_tag(self):
        emoji_list = list(utils.get_emojis_by_tag('invalid'))
        self.assertEqual(len(emoji_list), 0)

    def test_get_emojis_by_category(self):
        emoji_list = list(utils.get_emojis_by_category('People & Body'))
        self.assertTrue(len(emoji_list) > 0)

    def test_get_emojis_by_category_case_insensitive(self):
        emoji_list = list(utils.get_emojis_by_category('people & body'))
        self.assertTrue(len(emoji_list) > 0)

    def test_get_emojis_by_invalid_category(self):
        emoji_list = list(utils.get_emojis_by_category('Invalid'))
        self.assertEqual(len(emoji_list), 0)

    def test_get_tags(self):
        tags = list(utils.get_tags())
        self.assertTrue(len(tags) > 0)

    def test_get_categories(self):
        categories = list(utils.get_categories())
        self.assertTrue(len(categories) > 0)


if __name__ == '__main__':
    unittest.main()
