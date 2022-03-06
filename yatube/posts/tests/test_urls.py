from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from ..models import Group, Post
from http import HTTPStatus
User = get_user_model()


class PostModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='Тестовый слаг',
            description='Тестовое описание',)
        cls.post = Post.objects.create(
            author=cls.user,
            text='Система обучения от Яндекса построена очень плохо',
            group=cls.group)


def setUp(self):
    Testr = User.objects.create_user(username='client_authorized_another')
    self.guest_client = Client()
    self.authorized_client = Client()
    self.client_authorized_another = Client()
    self.authorized_client.force_login(self.user)
    self.client_authorized_another.force_login(Testr)

def test_unauthorized_user_urls_status_code(self):
    """Проверка доступности страниц для неавторизованного пользователя."""
    status = HTTPStatus.OK
    url_status_code = {
        '/': status,
        f'/group/{self.group.slug}/': status,
        f'/profile/{self.user_author.username}/': status,
        f'/posts/{self.post.id}/': status,
        '/unexisting_page/': HTTPStatus.NOT_FOUND,
    }

    for url, response_code in url_status_code.items():
        with self.subTest(url=url):
            status_code = self.unauthorized_user.get(url).status_code
            self.assertEqual(status_code, response_code)


def test_urls_uses_correct_template(self):
    """URL-адрес использует соответствующий шаблон."""
    # Шаблоны по адресам
    templates_url_names = {
        'post/index.html': '/',
        'post/group_list.html': '/group/test-slug/',
        'post/profile.html': '/profile/auth/',
        'post/post_detail.html': f'/posts/{self.post.pk}/',
    }
    for template, address in templates_url_names.items():
        with self.subTest(address=address):
            response = self.authorized_client.get(address)
            self.assertTemplateUsed(response, template)


# Авторизованные
def test_edit_url_uses_correct_template(self):
    """Страница /'posts/<int:pk>/edit/ использует
        шаблон post/create_post.html"""
    response = self.authorized_client.get(f'/posts/{self.post.pk}/edit')
    self.assertTemplateUsed(response, 'posts/create_post.html')


def test_create_url_uses_correct_template(self):
    """Страница /create/ использует
        шаблон post/create_post.html"""
    response = self.authorized_client.get('/create/')
    self.assertTemplateUsed(response, 'posts/create_post.html')


def test_edit_url_uses_correct_template_for_noauthor(self):
    """Переадресует не автора"""
    self.authorized_client = Client()
    # Создаем третий клиент
    response = self.client_authorized_another(f'/posts/{self.post.pk}/edit')
    self.assertEqual(response.status_code, 302)
