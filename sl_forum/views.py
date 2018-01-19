from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, View, FormView
from .models import TopicForum, SectionForum, MessageForum
from .forms import TopicForm, MessageForm
import markdown


class ForumView(ListView):
    """Главная страница форума выводим Разделы на страницу"""
    template_name = 'sl_forum/forum_start.html'
    model = SectionForum
    context_object_name = 'section'


class TopicAllView(ListView):
    """Выводим темы отсортированные по данному разделу"""
    template_name = 'sl_forum/forum_topic_all.html'
    context_object_name = 'topic'

    def get_queryset(self):
        topic = TopicForum.objects.filter(section=self.kwargs['pk'])
        for t in topic:
            t.text = markdown.markdown(t.text,)
        return topic


class TopicOneView(DetailView, FormView):
    """Выводим одну тему с описанием"""
    template_name = 'sl_forum/forum_topic_one.html'
    context_object_name = 'topic'
    model = TopicForum
    form_class = MessageForm

    def get_context_data(self, **kwargs):
        kwargs['message'] = MessageForum.objects.filter(topic=self.kwargs['pk'])
        return super(TopicOneView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse('forum_topic_one', args=[str(obj.pk)]))


class TopicCreateView(CreateView):
    """Создание темы на форуме"""
    template_name = 'sl_forum/forum_topic_create.html'
    model = TopicForum
    form_class = TopicForm
    context_object_name = 'topic'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse('forum_topic_one', args=[str(obj.pk)]))
