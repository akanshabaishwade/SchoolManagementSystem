# Generated by Django 4.2.9 on 2024-05-13 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_rename_clasfee_studentfee_classfee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentfee',
            old_name='amount',
            new_name='paid_amount',
        ),
        migrations.AddField(
            model_name='studentfee',
            name='due_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]