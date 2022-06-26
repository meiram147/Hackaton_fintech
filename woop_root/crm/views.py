from django.shortcuts import render
from .forms import OrderFrom
from .models import Orders
from django.http import HttpResponse

# Create your views here.
def analyze_page(request):
    form = OrderFrom()
    return render(request, './index.html', {'form': form})

def thanks_page(request):
    #получаем наши значения которые ввел юзер
    name = request.POST['name']
    position = request.POST['position']
    one_transefer_income = request.POST['one_transefer_income']
    any_more_consumption = request.POST['any_more_consumption']
    one_refueling = request.POST['one_refueling']
    one_work_hours = request.POST['one_work_hours']
    work_graph = request.POST['work_graph']
    services = request.POST['services']
    services_one_day = request.POST['services_one_day']
    work_day = request.POST['work_day']
    ESP = request.POST['ESP']
    # записываем эти значения в бд для дальнейшей аналитики 
    element = Orders(order_name = name, order_position = position, order_one_transefer_income = one_transefer_income, 
                    order_any_more_consumption = any_more_consumption, order_one_refueling = one_refueling,
                    order_one_work_hours = one_work_hours, order_work_graph = work_graph, order_services = services,
                    order_services_one_day = services_one_day, order_work_day = work_day, order_ESP = ESP)
    element.save()
    # перводим наши значения в инт
    one_work_hours_int = int(one_work_hours)
    one_refueling_int = int(one_refueling)
    one_transefer_income_int = int(one_transefer_income)
    work_graph_int = int(work_graph)
    any_more_consumption_int = int(any_more_consumption)
    services_one_day_int = int(services_one_day)
    services_int = int(services)
    work_day_int = int(work_day)
    ESP_int = int(ESP)
    # провверка на затраты если затрат не было то пропускаем как 0
    if one_refueling_int == 0 or one_refueling_int <= -1:
        one_transefer = 0
    else:
        one_transefer = one_refueling_int-one_transefer_income_int
    # используев формулу поиска дохода за 1 час 
    one_service = one_transefer_income_int/one_work_hours_int
    # формула подсчета дохода за 1 день
    one_day_income = (one_service*work_graph_int)-any_more_consumption_int
    # подсчет проваленных сервисов за 1 день
    failed_service = services_one_day_int-services_int
    # ....................................................................................
    # делаем аналитуку за месяц с учетом этих данных
    mount_income = (one_day_income*work_day_int)-ESP_int
    failed_service_mounth = failed_service*work_day_int
    services_mounth = services_int*work_day_int
    one_transefer_mounth = one_transefer*work_day_int
    # ....................................................................................
    # делаем аналитуку за год с учетом этих данных
    mount_income_year = mount_income*12
    failed_service_mounth_yaer = failed_service_mounth*12
    services_mounth_year = services_mounth*12
    one_transefer_mounth_year = one_transefer_mounth*12
    return render(request, './thanks.html', {'one_service':one_service, 'one_transefer':one_transefer, 
                                            'one_day_income':one_day_income, 'services_int':services_int,
                                            'failed_service':failed_service, 'work_day_int':work_day_int, 'mount_income':mount_income,
                                            'failed_service_mounth':failed_service_mounth,'services_mounth':services_mounth,
                                            'one_transefer_mounth':one_transefer_mounth,
                                            'mount_income_year':mount_income_year,
                                            "failed_service_mounth_yaer":failed_service_mounth_yaer,
                                            'services_mounth_year':services_mounth_year,
                                            'one_transefer_mounth_year':one_transefer_mounth_year,
                                            })
