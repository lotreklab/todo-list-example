from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from todolist.models import Todo

class TodoTests(APITestCase):

    def setUp(self):
        url = reverse('todo_rest-list')
        data = { "title" : "Todo Placeholder",
                 "text"  : "Lorem ipsum dolor sit amet"
                }
        response = self.client.post(url, data, format='json')


    def test_todo_doned(self):
        url = reverse('todo_rest-list')+"1/done/"
        response = self.client.get(url)
        self.assertEqual(Todo.objects.get().status, True)
        self.assertNotEqual(Todo.objects.get().status, False)



    def test_todo_undoned(self):
        url = reverse('todo_rest-list')+"1/"
        data = {"status" : True}
        response = self.client.patch(url, data, format='json')

        url = reverse('todo_rest-list')+"1/undone/"
        response = self.client.get(url)
        self.assertEqual(Todo.objects.get().status, False)
        self.assertNotEqual(Todo.objects.get().status, True)
