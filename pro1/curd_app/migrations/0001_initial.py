# Generated by Django 5.0.3 on 2024-03-24 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('food', models.CharField(choices=[('TEA', 'tea'), ('PULAV', 'pulav'), ('PAV BHAJI', 'pav bhaji'), ('COLD COFFEE', 'cold coffee')], max_length=20)),
                ('payment', models.CharField(choices=[('ONLINE', 'online'), ('CASH', 'cash')], max_length=20)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
            ],
        ),
    ]
