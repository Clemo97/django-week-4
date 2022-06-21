from django.test import TestCase
from .models import Profile,Neighbourhood, Business,Post
from django.contrib.auth.models import User
# Create your tests here.


class ProfileTest(TestCase):
    def setUp(self):
        self.clemo = User(username = 'Clemo',email = 'clemo@gmail.com')
        self.clemo = Profile(user = Self.clemo,user_id = 1,bio = 'my hood', email='test@gmail.com',profile_pic = 'image.jpg',location='Nairobi', neighbourhood='caren')

    def test_instance(self):
        self.assertTrue(isinstance(self.clemo,Profile))

    def test_save_profile(self):
        self.save_profile()
        all_profiles = Profile.objects.all()
        self.assertTrue(len(all_profiles),0)

    def test_delete_profile(self):
        self.clemo.delete_profile()
        all_profiles = Profile.objects.all()
        self.assertEqual(len(all_profiles),0)