# Generated by Django 2.0.2 on 2018-03-23 15:13

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
            name='Bathroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('building', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=4)),
                ('gender', models.CharField(max_length=8)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=3)),
                ('bathroomSlug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BathroomImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='bathroom_images')),
                ('bathroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='project.Bathroom')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('bathroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Bathroom')),
                ('responseTo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply', to='project.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(blank=True, default=0)),
                ('bathroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Bathroom')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userSlug', models.SlugField(unique=True)),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('user_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='rate',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.UserProfile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.UserProfile'),
        ),
    ]