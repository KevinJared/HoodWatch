from django.test import TestCase
from .models import *
from django.contrib.auth.models import User


# Create your tests here.
class ProfileTest(TestCase):
    def setUp(self):
        self.user = User(username = 'kevin_sniper', email = 'kevin@kevin.com', password = 'passwadd')
        self.user.save()
        self.kevin = Profile(bio = 'A python Programmer',contact = '054234444', user = self.user)

    def tearDown(self):
        Profile.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.kevin,Profile))

    def test_save(self):
        self.kevin.create_user_profile(self.user,True)
        self.kevin.save_user_profile(self.user)
        users = Profile.objects.all()
        self.assertTrue(len(users)>0)


class HoodTest(TestCase):
    def setUp(self):
        self.user = User(username='kevin_sniper', email='kevin@kevin.com', password='passwadd')
        self.user.save()
        self.kevin = Profile(bio='A python Programmer', contact='054234444', user=self.user)
        self.hood = Hood(name = 'Ngong',bio = "Milimani",admin = self.user)

    def tearDown(self):
        Profile.objects.all().delete()
        self.hood.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.hood,Hood))

    def test_save(self):
        self.hood.save_hood()
        hoods = Hood.objects.all()
        self.assertTrue(len(hoods) == 1)



class PostTest(TestCase):
    def setUp(self):
        self.user = User(username='kevin_sniper', email='kevin@kevin.com', password='passwadd')
        self.user.save()
        self.kevin = Profile(bio='A python Programmer', contact='054234444', user=self.user)
        self.hood = Hood(name='Ngong', bio="Milimani", admin=self.user)
        self.business = Business(name="brian", owner = self.user, business_description= 'langat',
                                 locale = self.hood,business_number = 4322323)
        self.post = Post(title='Postings',post = 'This is the post',
                         hood = self.hood, poster = self.user)

    def tearDown(self):
        Profile.objects.all().delete()
        self.hood.delete()
        self.business.delete()
        self.post.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post))

    def test_save(self):
        self.post.save_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts) == 1)
