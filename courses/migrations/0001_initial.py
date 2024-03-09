# Generated by Django 4.2.11 on 2024-03-09 16:59

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
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='Title')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='URL Tag')),
                ('description', models.TextField(verbose_name='Course Description')),
                ('content', models.TextField(verbose_name='Course Content')),
                ('date', models.DateField(verbose_name='Course Date')),
                ('duration', models.CharField(choices=[('short_term', 'Short-term'), ('long_term', 'Long-term')], max_length=20, verbose_name='Course Duration')),
                ('review', models.IntegerField(choices=[(1, 'Excellent'), (2, 'Good'), (3, 'Average'), (4, 'Poor'), (5, 'Very Poor')], verbose_name='Course Rating')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0, verbose_name='Status')),
                ('category', models.CharField(max_length=100, verbose_name='Category')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to=settings.AUTH_USER_MODEL, verbose_name='Instructor')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
    ]