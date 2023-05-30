# Generated by Django 4.2.1 on 2023-05-30 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='contact/', verbose_name='Image')),
                ('firstname', models.CharField(max_length=50, verbose_name='Firstname')),
                ('lastname', models.CharField(max_length=50, verbose_name='Lastname')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('phone', models.EmailField(max_length=12, verbose_name='Phone')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('firstname', models.CharField(max_length=12, verbose_name='Firstname')),
                ('lastname', models.CharField(max_length=50, verbose_name='Lastname')),
                ('phone', models.CharField(max_length=12, verbose_name='Phone')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
    ]
