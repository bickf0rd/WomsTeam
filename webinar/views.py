from django.shortcuts import render
from .forms import ClientForm
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError


def save_client(request):
    """Сохранение клиента в базу и отправка ему сообщения на мейл
    """
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            subject = ['Запись на вебинар DjangoSchool']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            message = [first_name + ' ' + last_name +
                       ', Вы успешно записались на наш вебинар,'
                       '\tперед началом мы пришлем вам ссылку.']
            recipients = form.cleaned_data['email']
            try:
                send_mail(subject, message, 'e-mail отправителя', recipients)
            except BadHeaderError:  # Защита от уязвимости
                return HttpResponse('Invalid header found')
            form.save()
            return render(request, "webinar/thanks.html",
                          {"first_name": first_name, "last_name": last_name})
    else:
        form = ClientForm()
    return render(request, "webinar/registration.html", {"form": form})
