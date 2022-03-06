
from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Post, Group
User = get_user_model()


class PaginatorViewsTest(TestCase):
    @classmethod
    def seUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create(username='usertest')
        cls.client = Client()
        cls.group = Group.objects.create(
            title='Test group',
            slug='testgroup',
            description='Description of test group'
        )
        # создадим 14 постов
        for i in range(1, 14):
            cls.post = Post.objects.create(
                text=f'Text n {i}',
                author=cls.user,
                group=cls.group
            )


# Проверяем, палжинатор
def test_first_page_contains_ten_records(self):
    # Проверка: на второй странице должно быть три поста.
    response = self.client.get(reverse('posts:index'))
    self.assertEqual(len(response.context['page_obj']), 10)


def test_second_page_contains_three_records(self):
    # Проверка: на второй странице должно быть три поста.
    response = self.client.get(reverse('posts:index') + '?page=2')
    self.assertEqual(len(response.context['page_obj']), 3)


def test_first_page_contains_ten_records(self):
    # Проверка: на второй странице должно быть три поста.
    response = self.client.get(reverse('posts:profile'))
    self.assertEqual(len(response.context['page_obj']), 10)


def test_second_page_contains_three_records(self):
    # Проверка: на второй странице должно быть три поста.
    response = self.client.get(reverse('posts:profile') + '?page=2')
    self.assertEqual(len(response.context['page_obj']), 3)


def test_first_page_contains_ten_records(self):
    # Проверка: на второй странице должно быть три поста.
    response = self.client.get(reverse('posts:group_list'))
    self.assertEqual(len(response.context['page_obj']), 10)


def test_second_page_contains_three_records(self):
    # Проверка: на второй странице должно быть три поста.
    response = self.client.get(reverse('posts:group_list') + '?page=2')
    self.assertEqual(len(response.context['page_obj']), 3)
