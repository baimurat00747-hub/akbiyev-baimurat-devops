import os
import unittest
from unittest.mock import patch

from app import get_student_info


class TestStudentApp(unittest.TestCase):

    def test_default_information(self):
        with patch.dict(os.environ, {}, clear=True):
            result = get_student_info()

        self.assertIn("Baimurat", result)
        self.assertIn("Akbiyev", result)
        self.assertIn("IT2-2306", result)
        self.assertIn("38150", result)

    def test_environment_variables(self):
        variables = {
            "STUDENT_NAME": "TestName",
            "STUDENT_SURNAME": "TestSurname",
            "STUDENT_GROUP": "TEST-GROUP",
            "STUDENT_ID": "123456"
        }

        with patch.dict(os.environ, variables):
            result = get_student_info()

        self.assertIn("TestName", result)
        self.assertIn("TestSurname", result)
        self.assertIn("TEST-GROUP", result)
        self.assertIn("123456", result)


if __name__ == "__main__":
    unittest.main()
