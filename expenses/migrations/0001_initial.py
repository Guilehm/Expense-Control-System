# Generated by Django 2.0.5 on 2018-05-09 02:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('value', models.DecimalField(decimal_places=2, max_digits=9)),
                ('due_date', models.DateField(db_index=True)),
                ('paid_out', models.BooleanField(default=False)),
                ('note', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField()),
                ('date_added', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_changed', models.DateTimeField(auto_now=True, db_index=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='core.Category')),
                ('tags', models.ManyToManyField(related_name='tags', to='core.Tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]