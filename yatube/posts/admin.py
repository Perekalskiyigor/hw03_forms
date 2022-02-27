from django.contrib import admin

from .models import Post, Group  # добавить модель Post в инт адм


class PostAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'text', 'pub_date', 'author', 'group',)
    # добавьте настройку list_editable, это позволит
    # изменять поле group в любом посте
    list_editable = ('group',)
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('text',)
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date',)
    # если поле пустое заполняем -пусто-
    empty_value_display = '-пусто-'
# При регистрации модели Post источником конфигурации для неё назначаем
# класс PostAdmin


class GroupAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'title', 'slug', 'description')
    # Добавляем интерфейс для поиска по названию
    search_fields = ('title',)
    empty_value_display = '-пусто-'
# При регистрации модели Post источником конфигурации для неё назначаем
# класс GroupAdmin


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
