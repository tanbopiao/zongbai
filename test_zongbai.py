"""宗伯（ZONGBAI）算子骨架单测：名帖完整、桩位齐整、只增不覆盖。"""
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

    def test_final_review_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.final_review(None)

    def test_amend_guili_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.amend_guili(None)


if __name__ == "__main__":
    unittest.main()
