from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        collaborate_form = CollaborateForm(
            {
                'name': 'alex',
                'email': 'alex@me.com',
                'message': 'hi!'
            },
        )
        self.assertTrue(collaborate_form.is_valid(), msg="Collaborate Form is not valid")

    def test_form_name_validation(self):
        collaborate_form = CollaborateForm(
            {
                'name': '',
                'email': 'alex@me.com',
                'message': 'hi!'
            },
        )
        self.assertFalse(collaborate_form.is_valid(), msg="Collaborate Form doesn't validate name")

    def test_form_email_validation(self):
        collaborate_form = CollaborateForm(
            {
                'name': 'alex',
                'email': '',
                'message': 'hi!'
            },
        )
        self.assertFalse(collaborate_form.is_valid(), msg="Collaborate doesn't validate email")

    def test_form_message_validation(self):
        collaborate_form = CollaborateForm(
            {
                'name': 'alex',
                'email': 'alex@me.com',
                'message': ''
            },
        )
        self.assertFalse(collaborate_form.is_valid(), msg="Collaborate doesn't validate message")