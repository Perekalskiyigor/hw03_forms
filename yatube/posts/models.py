from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Group(models.Model):
    title = models.CharField("group name", max_length=200,)
    slug = models.SlugField(unique=True, verbose_name="URL", max_length=20)
    description = models. TextField("Description")

    # Metadata
    def __str__(self):
        # выводим имя группы
        return self.title


class Post(models.Model):
    text = models.TextField("PostText")
    pub_date = models.DateTimeField("Publication_date", auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Author"
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='groups',
        blank=True,
        null=True)
# Metadata

    def __str__(self):
        # выводим текст поста
        return self.text

    class Meta:
        ordering = ['-pub_date']
