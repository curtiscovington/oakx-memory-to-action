import unittest

from oakx_study.ablation import evaluate_expression


class CalculatorTests(unittest.TestCase):
    def test_scaled_numeric_formulas(self):
        self.assertEqual(87, evaluate_expression("ceil(83 / 12) * 12 + 3"))
        self.assertEqual(89, evaluate_expression("(31 * 9 + 5 + 7) % 101"))
        self.assertEqual(75, evaluate_expression("44 + 2 * 13 + 5"))
        self.assertEqual(12, evaluate_expression("17 - 5"))
        self.assertEqual(9, evaluate_expression("ceil(221 / 32) + 2"))
        self.assertEqual(34, evaluate_expression("14 + 3 * 6 + 2"))
        self.assertEqual(73, evaluate_expression("min(73, 9 * 10 - 8)"))
        self.assertEqual(10, evaluate_expression("ceil(43 / 6) + 2"))
        self.assertEqual(48, evaluate_expression("max(28, 41) + 7"))

    def test_rejects_code_and_names(self):
        for expression in ("__import__('os')", "open('/etc/passwd')", "answer", "2 ** 100"):
            with self.assertRaises((SyntaxError, TypeError, ValueError)):
                evaluate_expression(expression)

    def test_rejects_excessive_result_and_zero_division(self):
        with self.assertRaises(ValueError):
            evaluate_expression("999999999999999 * 999999999999999")
        with self.assertRaises(ZeroDivisionError):
            evaluate_expression("1 / 0")


if __name__ == "__main__":
    unittest.main()
