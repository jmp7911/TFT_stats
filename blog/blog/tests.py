import json
from django.contrib.auth import get_user_model
from django.test import TestCase, Client

User = get_user_model()
class UserTest(TestCase):
    def setUp(self):
        self.base_url = "http://localhost:8000"
        self.client = Client(
            'Content-Type: application/json',
        )

        print("---------user---------")
        self.registration_user = {
            "email": "test@example.com",
            "password1": "test1234!",
            "password2": "test1234!",
        }
        self.user = {
            "email": "test@example.com",
            "password": "test1234!",
        }
        self.test_register()
        
        
    def test_register(self):
        """
        회원가입테스트
        """

        response = self.client.post(self.base_url + "/api/accounts/registration/", data=self.registration_user)
        print("---------register-----response.status_code---------")
        if response.status_code != 201:
            print("---------register-----response.data---------")
            print(response.data)
        self.assertEqual(response.status_code, 201)
        self.token = response.data["access"]
        self.user = response.data["user"]
        self.headers = {}
        self.headers["Authorization"] = "Bearer " + self.token
        
    def test_login(self):
        """
        로그인 테스트
        """
        print("---------test_login---------")
        self.test_register()
        response = self.client.post(self.base_url + "/api/accounts/login/", data=self.user)
        print("---------login-----response.status_code---------")
        if response.status_code != 200:
            print("---------register-----response.data---------")
            print(response.data)
        self.assertEqual(response.status_code, 200)
    
class PostTest(UserTest):
  def test_post(self):
    """
    모든 페이지 접속 가능 확인
    """
    self.post0001 = {
      'title': 'test',
      'content': 'test',
      'user': self.user["pk"]
    }
    print("---------test_post_list---------")
    res = self.client.get('http://localhost:8000/blog/', headers=self.headers)
    self.assertEquals(res.status_code, 200)

    print("---------test_post_create---------")
    res = self.client.post('http://localhost:8000/blog/', headers=self.headers, data=self.post0001)
    if res.status_code != 201:
      print("---------test_post_create-----response.data---------")
      print(res.data)
    self.assertEquals(res.status_code, 201)
    self.post0001["id"] = res.data["id"]

    print("---------test_post_detail---------")
    res = self.client.get(f'http://localhost:8000/blog/{self.post0001["id"]}/',headers=self.headers)
    if res.status_code != 200:
      print("---------test_post_detail-----response.data---------")
      print(res.data)
    self.assertEquals(res.status_code, 200)

    print("---------test_post_update---------")
    self.headers["Content-Type"] = "application/json"
    res = self.client.patch(f'http://localhost:8000/blog/{self.post0001["id"]}/',headers=self.headers, data=json.dumps({"title": "test2"}))
    if res.status_code != 200:
      print("---------test_post_update-----response.data---------")
      print(res.data)
    self.assertEquals(res.status_code, 200)
    
    print("---------test_post_delete---------")
    res = self.client.delete(f'http://localhost:8000/blog/{self.post0001["id"]}/',headers=self.headers)
    if res.status_code != 204:
      print("---------test_post_delete-----response.data---------")
      print(res.data)
    self.assertEquals(res.status_code, 204)
