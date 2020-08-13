# Generated by Django 2.2.13 on 2020-08-05 19:43

from django.db import migrations, models
import django.db.models.deletion
import eomf.aboutus.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Post Title')),
                ('date', models.DateField(verbose_name='date')),
                ('content', models.TextField(verbose_name='Content')),
                ('image_comlumn_number', models.CharField(choices=[('1', 'One column image'), ('2', 'Two columns image')], default='1', max_length=1, verbose_name=' column images')),
            ],
        ),
        migrations.CreateModel(
            name='PostFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='File title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('file_attached', models.FileField(upload_to='news/docs')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='aboutus.Post')),
            ],
        ),
        migrations.CreateModel(
            name='GalleryPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', eomf.aboutus.models.YearField(max_length=4)),
                ('order', models.IntegerField()),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('picture', models.ImageField(upload_to='aboutus/group_photos/photos')),
            ],
            options={
                'unique_together': {('year', 'order')},
            },
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
                ('order', models.PositiveIntegerField()),
                ('image', models.ImageField(null=True, upload_to='news')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='aboutus.Post')),
            ],
            options={
                'unique_together': {('post', 'order')},
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=16, null=True)),
                ('link', models.CharField(blank=True, max_length=250, null=True)),
                ('date', models.DateField(null=True, verbose_name='date published')),
                ('extra', models.TextField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('headshot', models.ImageField(default='/media/people/dummy_headshot222.jpg', null=True, upload_to='people/')),
                ('order', models.IntegerField(default=9999)),
                ('alumni_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='personAsAlumniGroup', to='aboutus.Group')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personAsGroup', to='aboutus.Group')),
            ],
            options={
                'unique_together': {('first_name', 'middle_name', 'last_name')},
            },
        ),
    ]
