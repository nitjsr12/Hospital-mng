# Generated by Django 3.0 on 2020-05-21 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hosmng', '0008_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='medical',
            name='doc_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hosmng.Doctor'),
        ),
        migrations.AddField(
            model_name='medical',
            name='pat_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hosmng.Patient'),
        ),
    ]
