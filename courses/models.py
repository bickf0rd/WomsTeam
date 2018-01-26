from django.db import models
from django.conf import settings


class Category(models.Model):
    """
        Класс модели категорий
    """
    title = models.CharField("Категория", max_length=50)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title


class Courses(models.Model):
    """
        Класс модели курсы
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Автор курса', null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, verbose_name="Категория", null=True, on_delete=models.SET_NULL)
    title = models.CharField('Название', max_length=50)
    price = models.IntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.title


class Task(models.Model):
    """
        Класс модели задания курса
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Пользователь', null=True,
                             on_delete=models.SET_NULL)
    courses = models.ForeignKey(Courses, verbose_name="Курс", null=True, on_delete=models.SET_NULL)
    title = models.CharField('Тема', max_length=50)
    text = models.TextField("Теория")
    code = models.TextField("Задания")
    correct_answer = models.TextField("Ответ")
    answer = models.TextField("Ответ учителя")

    class Meta:
        verbose_name = "Задачу"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.title
