# Generated by Django 4.1.1 on 2022-09-20 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_pdf_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf',
            name='pdf',
            field=models.FileField(upload_to=''),
        ),
    ]