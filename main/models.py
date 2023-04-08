from django.db import models


class UAV(models.Model):
    name = models.CharField('Название', max_length=100)
    oper_id = models.PositiveIntegerField('Оператор')
    base_id = models.PositiveIntegerField('База')
    description = models.TextField('Описание')
    duration = models.PositiveIntegerField('Длительность в полете')
    on_flight = models.BooleanField('В полете')
    max_range = models.PositiveIntegerField('Макс. дальность туда и обратно')
    cord_x = models.CharField('Текущее расположение по широте', max_length=100)
    cord_y = models.CharField('Текущее расположение по высоте', max_length=100)
    img_url = models.CharField('URL Изображения', max_length=250)
    
    def __str__(self):
        return f"{self.name} {self.oper_id} {self.on_flight}"
    
    class Meta:
        verbose_name = "БПЛА"
        verbose_name_plural = "БПЛА"


class Base(models.Model):
    name = models.CharField('Название', max_length=100)
    disp_id = models.PositiveIntegerField('Диспетчер')
    description = models.TextField('Описание')
    cord_x = models.CharField('Текущее расположение по широте', max_length=100)
    cord_y = models.CharField('Текущее расположение по высоте', max_length=100)
    active = models.BooleanField('Активный')
    
    def __str__(self):
        return f"{self.name} {self.disp_id}"
    
    class Meta:
        verbose_name = "База"
        verbose_name_plural = "Базы"