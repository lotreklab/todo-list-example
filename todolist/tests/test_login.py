import os

from django.test import TestCase
from django.test import override_settings

from account.models import Profile
from django.contrib.auth.models import User

class ProfileTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
    def testProfileModel(self):
        user = User.objects.create(
            first_name='testciccio',
            password = 'andreapuzza'
        )