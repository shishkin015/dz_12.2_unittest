import unittest


from utils.dicts import get_val


class TestGetVal(unittest.TestCase):
    def test_get_val_normal(self):
        self.assertEqual(get_val({"vcs": "mercurial"}, "vcs"), "mercurial")
        self.assertEqual(get_val({}, "vcs"), "git")
        self.assertEqual(get_val({}, "vcs", "bazaar"), "bazaar")
        self.assertEqual(get_val({}, "vcs", None), None)
        self.assertEqual(get_val({1: "one"}, 1), "one")
