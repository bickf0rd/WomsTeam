# -*- coding: utf-8 -*-
from django import forms
from django.forms import TextInput, EmailInput
from .models import ClientInfo


class ClientForm(forms.ModelForm):
    """Форма для отправки данных клиента, записывающегося на вебинар
    """
    
    class Meta:
        model = ClientInfo
        fields = ["first_name", "last_name", "email"]
        widgets = {
            "first_name": TextInput(attrs={"class": "inp-text",
                                           "placeholder": "Имя",
                                           # "id": "title",
                                           # "name": "title"
                                           }),
            "last_name": TextInput(attrs={"class": "inp-text",
                                          "placeholder": "Фамилия",
                                          }),
            # "company": TextInput(attrs={"class": "inp-text",
            #                             "placeholder": "Компания",
            #                             }),
            "email": EmailInput(attrs={"class": "inp-text",
                                       "placeholder": "Email",
                                       }),
            # "phone": NumberInput(attrs={"class": "inp-text",
            #                             "placeholder": "Телефон",
            #                             }),
            
        }
