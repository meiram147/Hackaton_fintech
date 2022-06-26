from django import forms

class OrderFrom(forms.Form):
    order_name = forms.CharField(max_length=100, label='Имя:')
    order_position = forms.CharField(max_length=100, label='Вид деятельности:')
    order_one_transefer_income = forms.IntegerField(label='стоимость 1 услуги в тнг:')
    order_any_more_consumption = forms.IntegerField(label='прочие рассходы (обед) в тнг:')
    order_one_refueling = forms.IntegerField(label='затраты на одну услугу в тнг:')
    order_one_work_hours = forms.IntegerField(label='время работы за одну услугу в часах:')
    order_work_graph = forms.IntegerField(label='график работы в часах:')
    order_services = forms.IntegerField(label='Введите сколько заказов вы сделали сегодня:')
    order_services_one_day = forms.IntegerField(label='Колличество заказов за день:')
    order_work_day = forms.IntegerField(label='Колличество рабочих дней в месяце:')
    order_ESP = forms.IntegerField(label='ЕСП за этот год: ')