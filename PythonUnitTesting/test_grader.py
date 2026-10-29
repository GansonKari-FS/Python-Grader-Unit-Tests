
import unittest
from GraderClass import GraderClass


class TestGraderClass(unittest.TestCase):

    def setUp(self):
        self.grader = GraderClass()

    # Test calculate_average()
    def test_average(self):
        self.assertEqual(
            self.grader.calculate_average([80, 90, 100]), 90
        )
        self.assertNotEqual(
            self.grader.calculate_average([70, 80]), 80
        )

    def test_empty_grades(self):
        with self.assertRaises(ValueError):
            self.grader.calculate_average([])

    # Test every letter grade
    def test_letter_grades(self):
        self.assertEqual(self.grader.get_letter_grade(95), "A")
        self.assertEqual(self.grader.get_letter_grade(85), "B")
        self.assertEqual(self.grader.get_letter_grade(75), "C")
        self.assertEqual(self.grader.get_letter_grade(65), "D")
        self.assertEqual(self.grader.get_letter_grade(55), "F")

    # Test boundary values
    def test_grade_boundaries(self):
        self.assertEqual(self.grader.get_letter_grade(90), "A")
        self.assertEqual(self.grader.get_letter_grade(89), "B")
        self.assertEqual(self.grader.get_letter_grade(80), "B")
        self.assertEqual(self.grader.get_letter_grade(79), "C")
        self.assertEqual(self.grader.get_letter_grade(70), "C")
        self.assertEqual(self.grader.get_letter_grade(69), "D")
        self.assertEqual(self.grader.get_letter_grade(60), "D")
        self.assertEqual(self.grader.get_letter_grade(59), "F")

    # Test invalid scores and both sides of the OR condition
    def test_invalid_scores(self):
        with self.assertRaises(ValueError):
            self.grader.get_letter_grade(-1)

        with self.assertRaises(ValueError):
            self.grader.get_letter_grade(101)

    # Test passing and failing
    def test_passing(self):
        self.assertTrue(self.grader.is_passing(75))
        self.assertTrue(self.grader.is_passing(60))
        self.assertFalse(self.grader.is_passing(59))
        self.assertFalse(self.grader.is_passing(30))


if __name__ == "__main__":
    unittest.main()
