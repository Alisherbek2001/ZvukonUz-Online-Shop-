# Generated by Django 4.1.5 on 2023-03-02 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_alter_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(help_text="Tavsiya etiladiogan rasm o'lchani 719x791", upload_to='product/%Y/%m/%d/', verbose_name='rasm'),
        ),
    ]