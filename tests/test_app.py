#test_app.py

import unittest
from app import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        result = self.app.get('/', follow_redirects=True)
        self.assertEqual(result.status_code, 200)

    def test_register(self):
        result = self.app.post('/register', data=dict(name="Test User", email="test@example.com", password="test123"))
        self.assertIn(b'response', result.data)

    def test_login(self):
        result = self.app.post('/login', data=dict(email="test@example.com", password="test123"))
        self.assertIn(b'response', result.data)

    def test_chatbot(self):
        result = self.app.post('/chatbot', data=dict(question="What are the symptoms of flu?"))
        self.assertIn(b'response', result.data)

if __name__ == '__main__':
    unittest.main()
