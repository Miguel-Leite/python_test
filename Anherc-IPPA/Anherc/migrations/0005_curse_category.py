# Generated by Django 3.2.3 on 2021-08-30 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Anherc', '0004_auto_20210830_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='curse',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Anherc.categorycurse'),
            preserve_default=False,
        ),
    ]
