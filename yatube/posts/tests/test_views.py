from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Post, Group
from django import forms

User = get_user_model()


class PaginatorViewsTest(TestCase):
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
            text='Тестовая пост',
            group=cls.group)


def setUp(self):
    # Создаем авторизованный клиент
    self.user = User.objects.create_user(username='StasBasov')
    self.authorized_client = Client()
    self.authorized_client.force_login(self.user)


# тесты, проверяющие, что во view-функциях
# используются правильные html-шаблоны.
def test_pages_uses_correct_template(self):
    """URL-адрес использует соответствующий шаблон."""
    # Собираем в словарь пары "имя_html_шаблона: reverse(name)"
    templates_pages_names = {
        'posts/index.html': reverse('posts:index'),
        'posts/group_list.html': reverse('posts:group_list',
                                         kwargs={'slug': self.slug}),
        'posts/profile.html': reverse('username',
                                      kwargs={'slug': self.user}),
        'posts/post_detail.html': reverse('pk',
                                          kwargs={'slug': self.post.pk}),
        'posts/create_post.html': reverse('posts:post_create'), }
    # Проверяем, что при обращении к name вызывается соответствующий HTML-шаб
    for template, reverse_name in templates_pages_names.items():
        with self.subTest(template=template):
            response = self.authorized_client.get(template)
            self.assertTemplateUsed(response, reverse_name)


def test_context_index_page(self):
    """Шаблон home сформирован с правильным контекстом."""
    response = self.authorized_client.get(reverse('posts:index'))
    post_obj = response.context['page_obj'][0]
    post_text = post_obj.text
    self.assertEqual(post_text, self.text)


def test_context_group_list_page(self):
    """Шаблон home сформирован с правильным контекстом."""
    response = self.authorized_client.get(reverse('posts:group_list',
                                                  kwargs={'slug': self.slug}))
    group_object = response.context['group']
    self.assertEqual(group_object, self.group)
    post_obj = response.context['page_obj']
    post_text = post_obj.text
    self.assertEqual(post_text, self.text)


def test_context_group_list_page(self):
    """Шаблон home сформирован с правильным контекстом."""
    response = self.authorized_client.get(reverse('username',
                                                  kwargs={'slug': self.user}))
    user = response.context['author']
    self.assertEqual(user, self.author)
    post_obj = response.context['page_obj']
    post_text = post_obj.text
    self.assertEqual(post_text, self.text)


def test_context_group_list_page(self):
    """Шаблон home сформирован с правильным контекстом."""
    response = self.authorized_client.get(reverse('pk',
                                          kwargs={'slug': self.post.pk}))
    post = response.context['post'], 1
    self.assertEqual(post, self.post)
    post_obj = response.context['page_obj']
    post_text = post_obj.text
    self.assertEqual(post_text, self.text)


def test_edit_post_form(self):
    """Шаблон home сформирован с правильным контекстом."""
    response = self.authorized_client.get(reverse('posts:create_post'))
    form_fields = {
        'text': forms.fields.CharField,
        'group': forms.fields.CharField, }
    for value, expected in form_fields.items():
        with self.subTest(value=value):
            form_field = response.context.get('form').fields.get(value)
            self.assertIsInstance(form_field, expected)


def test_create_post_form(self):
    """Шаблон home сформирован с правильным контекстом."""
    response = self.authorized_client.get(reverse('posts:create_post'))
    form_fields = {
        'text': forms.fields.CharField,
        'group': forms.fields.CharField, }
    for value, expected in form_fields.items():
        with self.subTest(value=value):
            form_field = response.context.get('form').fields.get(value)
            self.assertIsInstance(form_field, expected)
