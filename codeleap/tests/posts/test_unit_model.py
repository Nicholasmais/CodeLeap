from django.test import TestCase
from posts.models.post import Post
from django.core.exceptions import ValidationError

class PostModelTest(TestCase):
    def test_create_post_successfully(self):
        post = Post.objects.create(
            username="testuser",
            title="First Post",
            content="This is the content of the first post."
        )
        self.assertEqual(post.username, "testuser")
        self.assertEqual(post.title, "First Post")
        self.assertEqual(post.content, "This is the content of the first post.")

    def test_username_must_be_unique(self):
        Post.objects.create(
            username="testuser",
            title="First Post",
            content="Content of the first post."
        )
        with self.assertRaises(Exception):
            Post.objects.create(
                username="testuser",
                title="Another Post",
                content="Content of another post."
            )

    def test_title_min_length(self):
        with self.assertRaises(ValidationError):
            post = Post(
                username="testuser",
                title="Hi",
                content="Short title test."
            )
            post.full_clean()

    def test_username_min_length(self):
        with self.assertRaises(ValidationError):
            post = Post(
                username="ab",
                title="Valid Title",
                content="Valid content."
            )
            post.full_clean()
