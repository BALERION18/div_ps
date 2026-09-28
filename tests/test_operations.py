import os
import unittest

class TestStudentFeedbackApp(unittest.TestCase):
    """
    Test suite for validating the Student Feedback Web Application structure,
    required form components, and frontend logic.
    """

    def setUp(self):
        # Base directory of the project
        self.base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        self.src_dir = os.path.join(self.base_dir, 'src')
        self.html_file = os.path.join(self.src_dir, 'index.html')
        self.css_file = os.path.join(self.src_dir, 'style.css')
        self.js_file = os.path.join(self.src_dir, 'script.js')

    def test_frontend_files_exist(self):
        """Verify that all core frontend files (HTML, CSS, JS) exist."""
        self.assertTrue(os.path.exists(self.html_file), "index.html should exist in src/")
        self.assertTrue(os.path.exists(self.css_file), "style.css should exist in src/")
        self.assertTrue(os.path.exists(self.js_file), "script.js should exist in src/")

    def test_html_form_elements_present(self):
        """Verify that the feedback form has all required input fields."""
        with open(self.html_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check form tag
        self.assertIn('id="feedbackForm"', content, "Feedback form must have id 'feedbackForm'")

        # Check Student Name input
        self.assertIn('id="studentName"', content, "Form must have an input with id 'studentName'")

        # Check Course input
        self.assertIn('id="courseName"', content, "Form must have an input with id 'courseName'")

        # Check Feedback textarea
        self.assertIn('id="feedbackText"', content, "Form must have a textarea with id 'feedbackText'")

        # Check Submit button
        self.assertIn('id="submitBtn"', content, "Form must have a submit button with id 'submitBtn'")

    def test_html_display_section_present(self):
        """Verify that a container to display submitted feedback exists."""
        with open(self.html_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check feedback list container
        self.assertIn('id="feedbackList"', content, "Webpage must have a container with id 'feedbackList' to display feedback")
        # Check feedback count badge
        self.assertIn('id="feedbackCount"', content, "Webpage must have an element to display feedback count")

    def test_css_content(self):
        """Verify that the stylesheet is populated and contains essential styling rules."""
        with open(self.css_file, 'r', encoding='utf-8') as f:
            css_content = f.read()

        self.assertGreater(len(css_content.strip()), 100, "style.css should not be empty")
        self.assertIn('.card', css_content, "style.css should style cards")
        self.assertIn('.btn-primary', css_content, "style.css should have primary button styling")

    def test_js_feedback_logic(self):
        """Verify that script.js contains functions for handling submissions and rendering feedback."""
        with open(self.js_file, 'r', encoding='utf-8') as f:
            js_content = f.read()

        self.assertIn('handleFormSubmit', js_content, "script.js must contain form submission handler")
        self.assertIn('renderFeedbacks', js_content, "script.js must contain dynamic feedback rendering logic")
        self.assertIn('validateForm', js_content, "script.js must contain input validation logic")


if __name__ == '__main__':
    unittest.main()
