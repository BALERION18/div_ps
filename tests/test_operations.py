import os
import re
import unittest

try:
    from tests.testcases import VALID_DUMMY_CASES, INVALID_DUMMY_CASES, ACTIVE_DUMMY_CASE, validate_niet_email
except ImportError:
    from testcases import VALID_DUMMY_CASES, INVALID_DUMMY_CASES, ACTIVE_DUMMY_CASE, validate_niet_email

class TestStudentFeedbackApp(unittest.TestCase):
    def setUp(self):
        self.base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        self.src_dir = os.path.join(self.base_dir, 'src')
        self.html_file = os.path.join(self.src_dir, 'index.html')
        self.css_file = os.path.join(self.src_dir, 'style.css')
        self.js_file = os.path.join(self.src_dir, 'script.js')

    def test_frontend_files_exist(self):
        self.assertTrue(os.path.exists(self.html_file), "index.html should exist in src/")
        self.assertTrue(os.path.exists(self.css_file), "style.css should exist in src/")
        self.assertTrue(os.path.exists(self.js_file), "script.js should exist in src/")

    def test_html_form_elements_present(self):
        with open(self.html_file, 'r', encoding='utf-8') as f:
            content = f.read()

        self.assertIn('id="feedbackForm"', content, "Feedback form must have id 'feedbackForm'")
        self.assertIn('id="studentName"', content, "Form must have an input with id 'studentName'")
        self.assertIn('id="studentEmail"', content, "Form must have an input with id 'studentEmail'")
        self.assertIn('id="courseName"', content, "Form must have an input with id 'courseName'")
        self.assertIn('id="feedbackText"', content, "Form must have a textarea with id 'feedbackText'")
        self.assertIn('id="submitBtn"', content, "Form must have a submit button with id 'submitBtn'")

    def test_html_display_section_present(self):
        with open(self.html_file, 'r', encoding='utf-8') as f:
            content = f.read()

        self.assertIn('id="feedbackList"', content, "Webpage must have a container with id 'feedbackList' to display feedback")
        self.assertIn('id="feedbackCount"', content, "Webpage must have an element to display feedback count")

    def test_css_content(self):
        with open(self.css_file, 'r', encoding='utf-8') as f:
            css_content = f.read()

        self.assertGreater(len(css_content.strip()), 100, "style.css should not be empty")
        self.assertIn('.card', css_content, "style.css should style cards")
        self.assertIn('.btn-primary', css_content, "style.css should have primary button styling")
        self.assertIn('.user-email', css_content, "style.css should have user-email styling")

    def test_js_feedback_logic(self):
        with open(self.js_file, 'r', encoding='utf-8') as f:
            js_content = f.read()

        self.assertIn('handleFormSubmit', js_content, "script.js must contain form submission handler")
        self.assertIn('renderFeedbacks', js_content, "script.js must contain dynamic feedback rendering logic")
        self.assertIn('validateForm', js_content, "script.js must contain input validation logic")
        self.assertIn('studentEmail', js_content, "script.js must handle studentEmail parameter")
        self.assertIn('NIET_EMAIL_REGEX', js_content, "script.js must enforce NIET email regex")

    def test_valid_dummy_cases_pass(self):
        for email in VALID_DUMMY_CASES:
            with self.subTest(email=email):
                self.assertTrue(validate_niet_email(email), f"Valid case '{email}' should pass")

    def test_invalid_dummy_cases_fail_validation(self):
        for email in INVALID_DUMMY_CASES:
            with self.subTest(email=email):
                self.assertFalse(validate_niet_email(email), f"Invalid case '{email}' should fail validation")

    def test_active_dummy_case_verification(self):
        self.assertTrue(
            validate_niet_email(ACTIVE_DUMMY_CASE),
            f"\n[TEST FAILED] Active dummy case '{ACTIVE_DUMMY_CASE}' failed! Only @niet.co.in is allowed."
        )


if __name__ == '__main__':
    unittest.main()
