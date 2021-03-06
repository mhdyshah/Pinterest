# Generated by Django 3.2.8 on 2021-10-14 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, default='', null=True, upload_to='store_image/')),
                ('fullname', models.CharField(default='<django.db.models.query_utils.DeferredAttribute object at 0x7f2b96ba1df0>', max_length=255)),
                ('shortBio', models.CharField(blank=True, max_length=555, null=True)),
                ('pronouns', models.CharField(blank=True, choices=[('ey/em', 'ey/em'), ('he/him', 'he/him'), ('ne/nem', 'ne/nem'), ('she/her', 'she/her'), ('they/them', 'they/them'), ('ve/ver', 've/ver'), ('xe/xem', 'xe/xem'), ('xie/xem', 'xie/xem'), ('ze/zir', 'ze/zir')], help_text='Add your Pronouns', max_length=20, null=True)),
                ('website', models.URLField(blank=True, help_text='Add a link to drive traffic to your site')),
                ('username', models.CharField(default='<django.db.models.query_utils.DeferredAttribute object at 0x7f2b96ba1df0>', max_length=255)),
                ('age', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(default='<django.db.models.query_utils.DeferredAttribute object at 0x7f2b96ba1df0>', max_length=255)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AccountSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='<django.db.models.query_utils.DeferredAttribute object at 0x7f2b96ba1df0>', max_length=254)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(choices=[('Iran', 'Iran'), ('America', 'America'), ('England', 'England'), ('France', 'France'), ('Italy', 'Italy')], max_length=68)),
                ('language', models.CharField(choices=[('Persian', 'Persian'), ('English(US)', 'English(US)'), ('English(UK)', 'English(UK)'), ('French', 'French'), ('Italiano', 'Italiano')], max_length=68)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Non_Binary', 'Non_Binary')], max_length=24)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(default='<django.db.models.query_utils.DeferredAttribute object at 0x7f2b96ba1df0>', max_length=255)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
