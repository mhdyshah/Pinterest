# Generated by Django 3.2.8 on 2021-10-26 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalsettings', '0009_auto_20211026_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountsettings',
            name='email',
            field=models.EmailField(default='<django.db.models.query_utils.DeferredAttribute object at 0x7f52a13b6fd0>', max_length=254),
        ),
        migrations.AlterField(
            model_name='accountsettings',
            name='updated_by',
            field=models.CharField(default='<django.db.models.query_utils.DeferredAttribute object at 0x7f52a13b6fd0>', max_length=255),
        ),
        migrations.AlterField(
            model_name='publicprofile',
            name='fullname',
            field=models.CharField(default='<django.db.models.query_utils.DeferredAttribute object at 0x7f52a13b6fd0>', max_length=255),
        ),
        migrations.AlterField(
            model_name='publicprofile',
            name='updated_by',
            field=models.CharField(default='<django.db.models.query_utils.DeferredAttribute object at 0x7f52a13b6fd0>', max_length=255),
        ),
        migrations.AlterField(
            model_name='publicprofile',
            name='username',
            field=models.CharField(default='<django.db.models.query_utils.DeferredAttribute object at 0x7f52a13b6fd0>', max_length=255),
        ),
    ]