from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class AbstractDateTimeModel(models.Model):
    """Абстрактная модель реализует время и дату создание сущностей"""
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    modified = models.DateTimeField('Дата редактирования', auto_now_add=True)

    class Meta:
        abstract = True


class SectionForum(AbstractDateTimeModel):
    """Модель реализует разделы на форуме"""
    title = models.CharField(
        'Укажите название раздела на форуме',
        max_length=250)

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ('-created',)
        db_table = 'sectionforum'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('forum_topic_all', args=[str(self.id)])


class TopicForum(AbstractDateTimeModel):
    """Модель реализует темы на форуме"""
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        related_name='topic_forum',
        on_delete=models.CASCADE)

    section = models.ForeignKey(
        SectionForum,
        verbose_name='Укажите к какому разделу относиться тема',
        related_name='section_forum',
        on_delete=models.CASCADE)

    title = models.CharField('Укажите название темы на форуме', max_length=250)
    text = models.TextField('Текст, описание темы')

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
        ordering = ('-created',)
        db_table = 'topicforum'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('forum_topic_one', args=[str(self.id)])


class MessageForum(AbstractDateTimeModel):
    """Модель сообщений которые оставляют пользователи на форуме"""
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        related_name='message_forum',
        on_delete=models.CASCADE)

    topic = models.ForeignKey(
        TopicForum,
        verbose_name='Укажите к какой теме относиться сообщение',
        related_name='message_topic',
        on_delete=models.CASCADE)

    text = models.TextField('Текст сообщения')

    class Meta:
        verbose_name = 'Сообщение на форуме'
        verbose_name_plural = 'Сообщения на форуме'
        ordering = ('-created',)
        db_table = 'messageforum'

    def __str__(self):
        return self.text[:20]

    def get_absolute_url(self):
        return reverse('forum_topic_one', args=[str(self.id)])


class UserForum(AbstractDateTimeModel):
    """Профиль юзера на форуме"""
    user = models.ForeignKey(
        User,
        verbose_name='Профиль пользователя на форуме',
        related_name='user_forum',
        on_delete=models.CASCADE)

    name = models.CharField(
        verbose_name='Имя пользователя',
        max_length=50,
        blank=True)
    views = models.PositiveIntegerField(
        verbose_name='Счетчик сообщений пользователя',
        default=0)

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = verbose_name
        ordering = ('-created',)
        db_table = 'userforum'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.name:
            self.name = self.user
        super(UserForum, self).save()

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('forum_user_one', args=[str(self.id)])


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserForum.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
