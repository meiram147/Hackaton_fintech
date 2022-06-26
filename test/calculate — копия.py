one_transefer_income = int(input("Введите стоимость 1 услуги в тнг: "))
any_more_consumption = int(input("прочие рассходы (обед) в тнг: "))
one_refueling = int(input("затраты на одну услугу в тнг: "))
one_work_hours = int(input("время работы за одну услугу в тнг: "))
work_graph = int(input("Введите график работы: "))
services = int(input("Введите сколько заказов вы сделали сегодня: "))
services_one_day = int(input("Колличество заказов за день: "))
work_day = int(input("Колличество рабочих дней в месяц: "))

def calculate_day():
    global one_transefer
    if one_refueling == 0 or one_refueling <= -1:
        one_transefer = 0
    else:
        one_transefer = one_refueling-one_transefer_income
    one_service = one_transefer_income/one_work_hours
    print(f"час вашей работы стоит: {int(one_service)}тг \nЗатраты за услуги:{one_transefer}тг")
    global one_day_income
    one_day_income = (one_service*work_graph)-any_more_consumption
    global failed_service
    failed_service = services_one_day-services
    print(f"Доход за 1 день в тнг: {one_day_income}тг")
    print(f"Вы сделали сегодня {services} услуг \nКолличество проваленных услуг: {failed_service}")
calculate_day()

def calculate_mounth():
    global mount_income
    mount_income = (one_day_income*work_day)-3063
    print(f"прогноз прибыли с учетом расходов и ЕСП на {work_day} рабочих дней в месяц: {mount_income}тг")
    global failed_service_mounth
    failed_service_mounth = failed_service*work_day
    print(f"Прогноз колличества проваленных услуг за {work_day} рабочих дней в месяц: {failed_service_mounth} услуг")
    global services_mounth
    services_mounth = services*work_day
    print(f"Прогноз колличества выполненных услуг за {work_day} рабочих дней в месяц: {services_mounth} услуг")
    global one_transefer_mounth  
    one_transefer_mounth = one_transefer*work_day
    print(f"Прогноз колличества расходов за {work_day} рабочих дней в месяц: {one_transefer_mounth}тнг")
calculate_mounth()

def calculate_year():
    mount_income_year = mount_income*12
    print(f"прогноз прибыли на 12 мясецв, с учетом расходов и ЕСП на {work_day} рабочих дней в месяц: {mount_income_year}тг")
    failed_service_mounth_yaer = failed_service_mounth*12
    print(f"Прогноз колличества проваленных услуг на 12 мясецв, за {work_day} рабочих дней в месяц: {failed_service_mounth_yaer} услуг")
    services_mounth_year = services_mounth*12
    print(f"Прогноз колличества выполненных услуг на 12 мясецв, за {work_day} рабочих дней в месяц: {services_mounth_year} услуг")
    one_transefer_mounth_year = one_transefer_mounth*12
    print(f"Прогноз колличества расходов на 12 мясецв, за {work_day} рабочих дней в месяц: {one_transefer_mounth_year}тнг")
calculate_year()