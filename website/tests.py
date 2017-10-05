import os
import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import override_settings
from django.urls import reverse
from mock import Mock, patch
from rest_framework.response import Response
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class FakeTodoViewset():
    def __new__(cls, *args, **kwargs):
        pass

    def list(self, request):
        return Response([{'id': 1, 'title': 'ciaomock'}])


@override_settings(DEBUG=True)
class ListElementTestCase(StaticLiveServerTestCase):
    def setUp(self):
        print('start')
        self.selenium = webdriver.PhantomJS()
        super(ListElementTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(ListElementTestCase, self).tearDown()

    def test_list_contaier_laod(self):
        """
        Check if container of Todos is loaded on page
        """
        selenium = self.selenium
        selenium.set_window_size(1500, 768)
        selenium.maximize_window()
        selenium.get(self.live_server_url)

        time.sleep(3)
        htmlsource = selenium.find_element_by_id('todo-list')

    @patch('todolist.urls.TodoViewSet', FakeTodoViewset)
    def test_ajax_creates_li(self):
        """
        Mocking a todo-list API url and check that mocked todo is in list
        """
        selenium = self.selenium
        selenium.set_window_size(1500, 768)
        selenium.maximize_window()
        selenium.get(self.live_server_url)

        time.sleep(2)
        htmlli = selenium.find_element_by_tag_name('li')
