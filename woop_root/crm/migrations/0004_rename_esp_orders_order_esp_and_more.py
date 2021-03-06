# Generated by Django 4.0.5 on 2022-06-25 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_orders_esp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='ESP',
            new_name='order_ESP',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='any_more_consumption',
            new_name='order_any_more_consumption',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='name',
            new_name='order_name',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='one_refueling',
            new_name='order_one_refueling',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='one_transefer_income',
            new_name='order_one_transefer_income',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='one_work_hours',
            new_name='order_one_work_hours',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='position',
            new_name='order_position',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='services',
            new_name='order_services',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='services_one_day',
            new_name='order_services_one_day',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='work_day',
            new_name='order_work_day',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='work_graph',
            new_name='order_work_graph',
        ),
    ]
