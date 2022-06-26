from django.db import models

# Create your models here.
class Orders(models.Model):
    order_name = models.CharField(max_length=100, verbose_name='Имя:')
    order_position = models.CharField(max_length=100, verbose_name='Вид деятельности:')
    order_one_transefer_income = models.CharField(max_length=100, verbose_name='стоимость 1 услуги в тнг:')
    order_any_more_consumption = models.CharField(max_length=100,verbose_name='прочие рассходы (обед) в тнг:')
    order_one_refueling = models.CharField(max_length=100, verbose_name='затраты на одну услугу в тнг:')
    order_one_work_hours = models.CharField(max_length=100, verbose_name='время работы за одну услугу:')
    order_work_graph = models.CharField(max_length=100, verbose_name='график работы:')
    order_services = models.CharField(max_length=100, verbose_name='Введите сколько заказов вы сделали сегодня:')
    order_services_one_day = models.CharField(max_length=100, verbose_name='Колличество заказов за день:')
    order_work_day = models.CharField(max_length=100, verbose_name='Колличество рабочих дней в месяце:')
    order_ESP = models.CharField(max_length=100, verbose_name='ЕСП за этот год: ')
    def __str__(self):
            return self.order_position
    
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'