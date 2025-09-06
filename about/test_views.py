from django.test import TestCase
from django.urls import reverse
from .models import About
from .forms import CollaborateForm


class TestAboutView(TestCase):
    def setUp(self):
        self.about = About(
            title="iliana",
            content="this text describes me",
        )
        self.about.save()
    
    def test_render_about_page_with_collaborate_form(self):
        response = self.client.get(reverse(
            'about'
        ))
        print(response.context)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"iliana", response.content)
        self.assertIn(b"this text describes me", response.content)
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm)