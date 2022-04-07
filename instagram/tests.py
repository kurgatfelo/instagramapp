from django.test import TestCase
from .models import Comment, Profile, Image
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestCase(TestCase):
    """Test for the profile model class"""
    def setUp(self):
        self.user = User(username='')
        self.user.save()

        self.profile = Profile(id=20 ,profile_pic='profile-pic.jpg', bio='this is a setup to test profile',
                                    user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_profile(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    def test_update_profile(self):
        self.profile.save_profile()
        self.profile.update_profile(self.profile.user_id)
        self.profile.save_profile()
        self.assertTrue(Profile,self.profile.user)

class ImageTestClass(TestCase):
    """
    test class for Image model unit tests.
    """
    def setUp(self):
        self.user = User.objects.create_user("username", "password")
        self.new_profile = Profile(id =20,profile_pic='profile-pic.png',bio='this is a setup to test Image class',user=self.user)
        self.new_profile.save()
        self.newImage = Image(image='profile-pic.png',caption="image", profile=self.new_profile)

    def test_instance_true(self):
        self.assertTrue(isinstance(self.newImage, Image))

    def test_save_post(self):
        self.newImage.save_post()
        img = Image.objects.all()
        self.assertTrue(len(img) == 1)

    def test_delete_post(self):
        self.newImage.save_post()
        img = Profile.objects.all()
        self.assertTrue(len(img) <= 1)

    def test_get_image_by_id(self):
        self.newImage.save_post()
        img = self.newImage.get_image_by_id(self.newImage.id)
        images = Image.objects.filter(id=self.newImage.id)
        self.assertTrue(img, images)  

class CommentTestCase(TestCase):
    def setUp(self):
        self.user = User(username='vitalis')
        self.user.save()

        self.new_profile = Profile(profile_pic='profile-pic.png',bio='this is a test for comments class',user=self.user)
        self.new_profile.save()
        self.newImage = Image(image='profile-pic.png',caption="image", profile=self.new_profile)
        self.comment = Comment(comment='I am testing this class', user=self.new_profile, post = self.newImage, date="14-03-1998")

    def test_instance(self):
        self.assertTrue(isinstance(self.comment, Comment))

    def test_save_comment(self):
        self.comment.save_comment()
        comment = Comment.objects.all()
        self.assertFalse(len(comment) > 1)

    def test_delete_comment(self):
        self.comment.save_comment()
        comment = Comment.objects.all()
        self.assertTrue(len(comment)  <= 1)