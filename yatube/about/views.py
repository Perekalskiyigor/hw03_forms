# Импорт класса TemplateView, чтобы унаследоваться от него
from django.views.generic.base import TemplateView


# Страница об авторе
class AboutAuthorView(TemplateView):
    template_name = 'about/author.html'


# Страница технологии
class AboutTechView(TemplateView):
    # В переменной template_name обязательно указывается имя шаблона,
    # на основе которого будет создана возвращаемая страница
    template_name = 'about/tech.html'
