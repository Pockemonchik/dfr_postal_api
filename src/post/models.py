from django.db import models


class PostalItem(models.Model):
    """Общий Модель для почтовых отправлений"""
    sender_name = models.CharField(
        max_length=50,  verbose_name="ФИО отправителя")
    receiver_name = models.CharField(
        max_length=50,  verbose_name="ФИО получателя")
    send_point = models.CharField(
        max_length=50,  verbose_name="пункт отправки")
    receive_point = models.CharField(
        max_length=50,  verbose_name="пункт получения")
    send_index = models.CharField(
        max_length=50,  verbose_name="индекс места отправки")
    receive_index = models.CharField(
        max_length=50,  verbose_name="индекс места получения")

    class Meta:
        verbose_name = "Почтовое отправление"
        verbose_name_plural = "Почтовые отправления"
        ordering = ["-id"]

    def __str__(self):
        return str(self.id)


class Letter(PostalItem):
    """Модель почтовых писем"""
    class LetterTypes(models.IntegerChoices):
        DEFAULT = 0, 'письмо'
        REGISTERED = 1, 'заказное письмо'
        VALUABLE = 2, 'ценное письмо'
        EXPRESS = 3, 'экспресс-письмо'

    type = models.IntegerField(default=LetterTypes.DEFAULT, choices=LetterTypes.choices,
                               verbose_name="тип письма")
    weight = models.IntegerField(default=0,
                                 verbose_name="вес письма")

    class Meta:
        verbose_name = "Письмо"
        verbose_name_plural = "Письма"
        ordering = ["-time"]

    def __str__(self):
        return str(self.id)


class Parcel(models.Model):
    """Модель почтовых посылок"""
    class ParcelTypes(models.IntegerChoices):
        PACKEAGE = 0, 'мелкий пакет'
        PARCEL = 1, 'посылка'
        FIRST_CLASS = 3, 'посылка 1 Модельа'
        INTERNATIONAL = 4, 'посылка международная'
        VALUABLE = 5, 'ценная посылка'
        EXPRESS = 6, 'экспресс-посылка'

    type = models.IntegerField(default=ParcelTypes.DEFAULT, choices=ParcelTypes.choices,
                               verbose_name="тип посылки")
    phone_number = models.CharField(
        max_length=50,
        verbose_name="телефон для извещения")
    summary_price = models.IntegerField(default=0,
                                        verbose_name="сумма платежа")

    class Meta:
        verbose_name = "Посылка"
        verbose_name_plural = "Посылки"
        ordering = ["-id"]

    def __str__(self):
        return str(self.id)
