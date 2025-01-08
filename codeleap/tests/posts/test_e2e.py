from rest_framework.test import APITestCase
from rest_framework import status
from posts.models.post import Post

class PostAPITest(APITestCase):
    def setUp(self):
        self.post = Post.objects.create(
            username="testuser",
            title="First Post",
            content="This is the content of the first post."
        )
        self.create_url = "/posts/"
        self.detail_url = f"/posts/{self.post.id}"

    def test_create_post(self):
        data = {
            "username": "newuser",
            "title": "New Post",
            "content": "Content of the new post."
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["username"], "newuser")

    def test_list_posts(self):
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_patch_post(self):
        data = {
            "title": "Updated Title",
            "content": "Updated content."
        }
        response = self.client.patch(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Title")
        self.assertEqual(response.data["content"], "Updated content.")

    def test_delete_post(self):
        response = self.client.delete(self.detail_url)  
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Post.objects.filter(id=self.post.id).exists())

    def test_create_post_username_duplicate(self):
        payload = {
            "username": "unique_user",
            "title": "Title of post",
            "content": "Test post content"
        }
        response = self.client.post("/posts/", payload)        
        self.assertEqual(response.status_code, 201)

        response = self.client.post("/posts/", payload)
        self.assertEqual(response.status_code, 409)
        self.assertIn("duplicated", response.json()["erro"])

    def test_create_post_invalid_username_length(self):
        payload = {
            "username": "ab",
            "title": "Valid Title",
            "content": "This is valid content."
        }
        response = self.client.post("/posts/", payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn("Username must not have less than 3 characters.", str(response.json()["erro"]))

    def test_create_post_invalid_title_length(self):
        payload = {
            "username": "valid_user",
            "title": "ab",
            "content": "This is valid content."
        }
        response = self.client.post("/posts/", payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn("Title must not have less than 3 characters.", str(response.json()["erro"]))

    def test_create_post_missing_fields(self):
        payload = {"username": "valid_user"}
        response = self.client.post("/posts/", payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn("title", response.json()["erro"])
        self.assertIn("content", response.json()["erro"])

    def test_get_post_not_found(self):
        response = self.client.get("/posts/999")
        self.assertEqual(response.status_code, 404)
        self.assertIn("Post not found", response.json()["erro"])

    def test_patch_post_not_found(self):
        payload = {"title": "Updated Title"}
        response = self.client.patch("/posts/999", payload)
        self.assertEqual(response.status_code, 404)
        self.assertIn("Post not found", response.json()["erro"])

    def test_delete_post_not_found(self):
        response = self.client.delete("/posts/999")
        self.assertEqual(response.status_code, 404)
        self.assertIn("Post not found", response.json()["erro"])
