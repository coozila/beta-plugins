import os
import unittest

import requests

from . import BetaWolframBetaSearch


class TestBetaWolframBetaSearch(unittest.TestCase):
    def setUp(self):
        os.environ["WOLFRAMALPHA_APPID"] = "test_appid"
        self.plugin = BetaWolframBetaSearch()

    def tearDown(self):
        os.environ.pop("WOLFRAMALPHA_APPID", None)

    def test_wolframbeta_search(self):
        query = "2+2"
        try:
            from .wolframbeta_search import _wolframbeta_search
            _wolframbeta_search(query)
        except requests.exceptions.HTTPError as e:
            self.assertEqual(e.response.status_code, 401)


if __name__ == "__main__":
    unittest.main()
