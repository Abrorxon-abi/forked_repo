from django.db import models
from django.contrib.auth.models import User


class Merchant(models.Model):
    rasshotniy_shot = models.PositiveIntegerField( )
    inn = models.PositiveIntegerField( )
    bank = models.CharField( max_length = 50, verbose_name = "Банк" )
    name = models.CharField( max_length = 50, verbose_name = "Имя" )
    adress = models.CharField( max_length = 120, verbose_name = "Адрес" )
    contacts = models.CharField( max_length = 50, verbose_name = "Контакты" )    
    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name = 'Мерчант'
        verbose_name_plural = 'Мерчанты'


class Paymant_system(models.Model):
    name = models.CharField( max_length = 50)
    class Meta:
        verbose_name = ("Система(тип)")
        verbose_name_plural = ("Системы(типы)")
    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField( max_length = 50)
    class Meta:
        verbose_name = ("Cтатус")
        verbose_name_plural = ("Cтатусы")
    def __str__(self):
        return self.name


class Card(models.Model):
    pan = models.PositiveIntegerField( verbose_name = "Пан")
    token = models.PositiveIntegerField( verbose_name = "Токен" )
    expiry = models.CharField( max_length = 50, verbose_name = "Дата оканчание" )
    phone_number = models.CharField( max_length = 50, verbose_name = "Номер телефона" )
    verified = models.CharField( max_length = 50, verbose_name = "Проверинно" )
    status = models.CharField( max_length = 50, verbose_name = "Статус карты" )
    fraund_index = models.PositiveSmallIntegerField( default = 100)
    merchant = models.ForeignKey( Merchant, on_delete=models.CASCADE)
    system = models.ForeignKey(Paymant_system, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.pan)
    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'
        unique_together = ('pan', 'merchant',)


class Transaction(models.Model):
    name = models.CharField( max_length = 50, verbose_name = "Трансфер" )
    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name_plural = 'Трансфер'
        verbose_name = 'Трансферы'

    
class Tarif(models.Model):
    name = models.CharField( max_length = 50, verbose_name = "Называние тарифа" )
    transaction = models.ForeignKey( Transaction, on_delete=models.CASCADE)
    fee = models.FloatField( )
    e_pos = models.PositiveIntegerField( )
    merchant = models.ForeignKey( Merchant, on_delete=models.CASCADE)
    limit = models.PositiveBigIntegerField( )
    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'
    
    
class Payment(models.Model):
    tarif = models.ForeignKey(Tarif, on_delete=models.CASCADE)
    created_at = models.DateTimeField( auto_now_add = True )
    card = models.ForeignKey( Card, on_delete=models.CASCADE )
    sum = models.PositiveIntegerField( )
    details = models.CharField( max_length = 256 )
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = ( "Платеж ")
        verbose_name_plural = ("Платежи ")
        ordering = ['created_at']



class Transfer(models.Model):
    created_at = models.DateTimeField( auto_now_add = True )
    sender = models.ForeignKey( Card, on_delete = models.CASCADE )
    recipient = models.PositiveIntegerField( )
    sum = models.PositiveIntegerField( )
    fee = models.FloatField( )
    status = models.ForeignKey(Status, on_delete = models.CASCADE )    
    detail = models.CharField( max_length = 50)
    class Meta:
        verbose_name = ( "Перевод" )
        verbose_name_plural = ( "Переводы" )



