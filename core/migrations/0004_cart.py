# Generated by Django 3.2.9 on 2022-02-03 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0003_alter_category_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('on_created', models.DateTimeField(auto_now_add=True)),
                ('books', models.ManyToManyField(to='core.Book')),
                ('products', models.ManyToManyField(to='core.Product')),
            ],
        ),
    ]
