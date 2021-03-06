import unittest
from app.models import User

class UserModelTest(unittest.TestCase):
    '''
    test model class to run tests for user class objects
    '''

    def setUp(self):
        self.new_user = User(username='milly', email='milly@email.com', password_hash = 'emobird')

    def test_password_setter(self):
        self.assertTrue(self.new_user.password_hash is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('emobird'))