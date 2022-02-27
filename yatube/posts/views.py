from django.shortcuts import render, redirect, get_object_or_404
# Импортируем модель, чтобы обратиться к ней
from .models import Post, Group, User
from django.core.paginator import Paginator
# Добавляем Paginator
from django.contrib.auth.models import User
from django.template.defaultfilters import truncatechars
from .forms import PostForm

POSTS_PER_PAGE = 10  # кол-во выводимых постов используется в index(request)


# Главная страница
def index(request):
    template = 'posts/index.html'
    # posts = Post.objects.all()[:POSTS_PER_PAGE]
    post_list = Post.objects.all()
    # Показывать по 10 записей на странице.
    paginator = Paginator(post_list, POSTS_PER_PAGE)
    # Из URL извлекаем номер запрошенной страницы - это значение параметра page
    page_number = request.GET.get('page')
    # Получаем набор записей для страницы с запрошенным номером
    page_obj = paginator.get_page(page_number)
    # .order_by('-pub_date') вынесено в мета модели
    # title = 'Это главная страница проекта Yatube' прошлое задание для тест
    # Словарь с данными принято называть context
    context = {
        #  В словарь можно передать переменную
        # 'posts': posts,  заменили на pegenator
        'page_obj': page_obj,
    }
    return render(request, template, context)


def group_posts(request, slug):
    print("начало функции")
    # Функция get_object_or_404 получает по заданным критериям объект
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug=slug)
    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    template = 'posts/group_list.html'
    posts = (Post.objects.filter(group=group)[:POSTS_PER_PAGE]
             # .order_by('-pub_date') вынесено в мета модели,
             )
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)


# Персональная страница пользователя и страница записи
def profile(request, username):
    # Здесь код запроса к модели и создание словаря контекста
    user = get_object_or_404(User, username=username)
    title = f"Профайл пользователя {user.username}"
    posts = user.posts.all()
    paginator = Paginator(posts, POSTS_PER_PAGE)
    page_number = request.GET.get('page')
    # Получаем набор записей для страницы с запрошенным номером
    page_obj = paginator.get_page(page_number)
    # .order_by('-pub_date') вынесено в мета модели
    # title = 'Это главная страница проекта Yatube' прошлое задание для тест
    # Словарь с данными принято называть context
    template = 'posts/profile.html'

    context = {
        'title': title,
        'user': user,
        'username': username,
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, template, context)


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    post_count = Post.objects.filter(author=post.author).count()
    # detail = Post.objects.filter(id=post_id)
    title = f"Первые 30 символов поста { post.text|truncatechars:30 }"
    template = 'posts/post_detail.html'
    # Здесь код запроса к модели и создание словаря контекста
    context = {
        'post': post,
        'post_count': post_count,
        'title': title,
        # 'detail': detail,
    }
    return render(request, template, context)


# Форма регистрации нового поста
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('posts:profile', username=request.user)
    return render(request, 'posts/create_post.html', {'form': form})


# Форма редактирования поста
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    is_edit = True
    form = PostForm(
        request.POST or None, instance=post)
    if request.user != post.author:
        return redirect('posts:post_detail', pk=post.pk)
    if form.is_valid():
        form.save()
        return redirect('posts:post_detail', post_id=post.pk)

    context = {
        'form': form,
        'is_edit': is_edit,
        'post': post,
    }
    return render(request, 'posts/create_post.html', context)
