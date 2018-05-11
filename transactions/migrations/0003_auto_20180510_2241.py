# Generated by Django 2.0.5 on 2018-05-11 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0008_auto_20180510_2241'),
        ('transactions', '0002_auto_20180509_2353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='value',
            new_name='total',
        ),
        migrations.RenameField(
            model_name='revenue',
            old_name='value',
            new_name='total',
        ),
        migrations.AddField(
            model_name='expense',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='bank.BankAccount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='revenue',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='revenues', to='bank.BankAccount'),
            preserve_default=False,
        ),
    ]
