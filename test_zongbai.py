"""宗伯（ZONGBAI）算子单测：名帖完整、行为达标、只增不覆盖。"""
import unittest

from zongbai import Zongbai


class TestZongbai(unittest.TestCase):
    def setUp(self):
        self.op = Zongbai()

    def test_describe(self):
        d = self.op.describe()
        self.assertEqual(d["repo"], "zongbai")
        self.assertEqual(d["code"], "ZONGBAI")
        self.assertTrue(d["anchor"].startswith("Ω₀⊂⊙∞⊂Ω"))
        self.assertTrue(d["mingwen"])

    def test_final_review(self):
        out = self.op.final_review("笺稿一")
        self.assertEqual(out["verdict"], "confirmed")
        self.assertTrue(out["review_id"].startswith("ZB-"))

    def test_amend_guili(self):
        aid = self.op.amend_guili({"rule": "两步写须同务"})
        self.assertTrue(aid.startswith("AMEND-"))


if __name__ == "__main__":
    unittest.main()
