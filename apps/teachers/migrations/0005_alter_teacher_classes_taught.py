# Generated by Django 4.2.9 on 2024-05-12 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0004_alter_teacher_classes_taught'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='classes_taught',
            field=models.ManyToManyField(related_name='teachers', to='teachers.class'),
        ),
    ]
