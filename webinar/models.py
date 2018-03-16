from django.db import models


class ClientInfo(models.Model):
    """
    Модель инфо человека, записывающегося на вебинар
    """
    first_name = models.CharField("Имя", max_length=15)
    last_name = models.CharField("Фамилия", max_length=15)
    # company = models.CharField("Компания", max_length=50)
    email = models.EmailField("Email")
    # phone = models.IntegerField(verbose_name="Телефон")
    
    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        
    def __str__(self):
        return self.first_name
