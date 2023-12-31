# Generated by Django 4.2.7 on 2023-12-06 17:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=50, null=True)),
                ('additional_mail', models.CharField(blank=True, max_length=50, null=True)),
                ('phoneNumber', models.CharField(blank=True, max_length=50, null=True)),
                ('house', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('region', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('area', models.CharField(blank=True, max_length=50, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to=None)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
