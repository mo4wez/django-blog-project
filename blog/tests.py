from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Post

class BlogPostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='Test Author 1')
        cls.post1 = Post.objects.create(
            title='Test Post 1',
            author=cls.user,
            text='This is the description of Post Test 1.',
            status=Post.STATUS_CHOICES[0][0] # published
        )
        cls.post2 = Post.objects.create(
            title='Test Post 2',
            author=cls.user,
            text='This is the description of Post Test 2.',
            status=Post.STATUS_CHOICES[1][0] # draft
        )

    def test_post_list_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
    
    def test_post_list_url_by_name(self):
        response = self.client.get(reverse('posts_list'))
        self.assertEqual(response.status_code, 200)

    def test_blog_post_title_on_blog_list_page(self):
        response = self.client.get('/blog/')
        self.assertContains(response, self.post1.title)

    def test_post_detail_url(self):
        response = self.client.get(f'/blog/{self.post1.id}/')
        self.assertEqual(response.status_code, 200)

    def test_post_detail_url_by_name(self):
        response = self.client.get(reverse('post_detail', args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)

    def test_post_details_on_post_detail_page(self):
        response = self.client.get(reverse('post_detail', args=[self.post1.id]))
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)

    def test_status_404_if_post_not_exists(self):
        response = self.client.get(reverse('post_detail', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_dont_show_draft_post_on_post_list(self):
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, self.post1.title)
        self.assertNotContains(response, self.post2.title)