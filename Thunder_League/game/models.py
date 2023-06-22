from django.db import models

class game_inf(models.Model):
    name_game = models.CharField("Название матча", max_lenght=250)
    link = models.CharField('Ссылка')
    date = models.DateField('')

