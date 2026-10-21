"""标准库 unittest：无需安装测试框架。"""

import unittest

from ai_test_lab.summary import summarize_results


class SummaryTests(unittest.TestCase):
    def test_mixed_results(self):
        self.assertEqual(
            summarize_results(["PASS", "FAIL", "PASS", "PASS", "FAIL"]),
            {"total": 5, "passed": 3, "failed": 2, "pass_rate": 0.6},
        )

    def test_empty_results(self):
        self.assertEqual(
            summarize_results([]),
            {"total": 0, "passed": 0, "failed": 0, "pass_rate": 0.0},
        )

    def test_normalizes_case_and_spaces(self):
        self.assertEqual(summarize_results([" pass ", "fail"])['passed'], 1)

    def test_all_pass_and_all_fail(self):
        self.assertEqual(summarize_results(["PASS"])['pass_rate'], 1.0)
        self.assertEqual(summarize_results(["FAIL"])['pass_rate'], 0.0)

    def test_rejects_unknown_and_non_string_results(self):
        for value in ["SKIP", "", None, 1]:
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    summarize_results([value])


if __name__ == "__main__":
    unittest.main()
