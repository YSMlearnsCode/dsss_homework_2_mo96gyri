import unittest
from math_quiz import GenerateRandomInteger, ChooseOperator, ProblemAndSolution


class TestMathGame(unittest.TestCase):

    def test_GenerateRandomInteger(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = GenerateRandomInteger(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_ChooseOperator(self):
        # TODO

        for _ in range(1000):
             operator = ChooseOperator()
             self.assertIn(operator, ['+', '-', '*'], "Invalid operator generated")


    def test_ProblemAndSolution(self):
        # Test cases for ProblemAndSolution function
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (10, 3, '-', '10 - 3', 7),
            (4, 6, '*', '4 * 6', 24),
            (7, 0, '+', '7 + 0', 7),
            (9, 1, '-', '9 - 1', 8),
            (3, 3, '*', '3 * 3', 9),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = ProblemAndSolution(num1, num2, operator)
            self.assertEqual(problem, expected_problem, "Generated problem is incorrect")
            self.assertEqual(answer, expected_answer, "Calculated answer is incorrect")

if __name__ == "__main__":
    unittest.main()
