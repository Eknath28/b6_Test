# Generated by Django 3.2.12 on 2022-04-11 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_department_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='firstapp.department'),
        ),
    ]
