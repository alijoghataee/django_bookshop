from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model


class SignUpTest(TestCase):
    username = 'testusername'
    email = 'testusername@gmail.com'

    def test_sign_up_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_sign_up_url(self):
        response = self.client.get('/account/signup/')
        self.assertEqual(response.status_code, 200)

    def test_sign_up_form(self):
        user_model = get_user_model()
        user = user_model.objects.create_user(
            self.username,
            self.email,
        )
        self.assertEqual(user_model.objects.all().count(), 1)
        self.assertEqual(user_model.objects.all()[0].username, self.username)
        self.assertEqual(user_model.objects.all()[0].email, self.email)

    def test_csrf_token(self):
        Client(enforce_csrf_checks=True)
