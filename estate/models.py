from django.db import models

class Estate(models.Model):
    estate_name = models.CharField(
        verbose_name='Назв. недвижимости',
        max_length=255
    )
    city_id = models.ForeignKey(
        verbose_name='Местоположение',
        to='City',
        on_delete=models.CASCADE
    )
    estate_type_id = models.ForeignKey(
        verbose_name='Тип недвижимости',
        to='EstateType',
        on_delete=models.CASCADE
    )
    floor_space = models.DecimalField(
        verbose_name='Площадь недвижимости',
        max_digits=8, 
        decimal_places=2
    )
    number_of_baclonies = models.PositiveSmallIntegerField(
        verbose_name='Количество балконов / лоджий'
    )
    baclonies_space = models.DecimalField(
        verbose_name='Площадь балконов / лоджий',
        max_digits=8, 
        decimal_places=2
    )
    number_of_bedrooms = models.PositiveSmallIntegerField(
        verbose_name='Кол-во спален'
    )
    number_of_bathrooms = models.PositiveSmallIntegerField(
        verbose_name='Кол-во ванных комнат'
    )
    number_of_garages = models.PositiveSmallIntegerField(
        verbose_name='Кол-во гаражей'
    )
    number_of_parking_spaces = models.PositiveSmallIntegerField(
        verbose_name='Кол-во парковочных мест'
    )
    pets_allowed = models.BooleanField(
        verbose_name='Разрешены ли животные'
    )
    estate_description = models.TextField(
        verbose_name='Описание недвижимости'
    )
    estate_status_id = models.ForeignKey(
        verbose_name='Статус недвижимости',
        to='EstateStatus',
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f'{self.estate_name}'

    class Meta:
        verbose_name = "Недвижимость"
        verbose_name_plural = "Недвижимость"


class City(models.Model):
    city_name = models.CharField(
        verbose_name='Город',
        max_length=128
    )
    country_id = models.ForeignKey(
        verbose_name='Страна',
        to='Country',
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f'{self.city_name}'
    
    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class Country(models.Model):
    country_name = models.CharField(
        verbose_name='Страна',
        max_length=128
    )

    def __str__(self) -> str:
        return f'{self.country_name}'

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"


class EstateType(models.Model):
    type_name = models.CharField(
        verbose_name='Тип недвижимости',
        max_length=128,
        help_text='In the estate_type dictionary, we’ll store values like “apartment”, “house”, “field”, etc.'
    )

    def __str__(self) -> str:
        return f'{self.type_name}'

    class Meta:
        verbose_name = "Тип недвижимости"
        verbose_name_plural = "Типы недвжижимости"


class EstateStatus(models.Model):
    estate_status_name = models.CharField(
        verbose_name='Статус недвижимости',
        max_length=64,
        help_text='The estate_status table will have values stating if the property is currently available or not, such as “estate leased”, “estate bought”, “estate sold”, “estate rented”.'
    )

    def __str__(self) -> str:
        return f'{self.estate_status_name}'

    class Meta:
        verbose_name = "Статус недвижимости"
        verbose_name_plural = "Статусы недвижимости"