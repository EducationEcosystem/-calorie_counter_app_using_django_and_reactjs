# Generated by Django 4.1.7 on 2023-03-15 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_food_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='selectfood',
            name='units',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.RemoveField(
            model_name='selectfood',
            name='food',
        ),
        migrations.AddField(
            model_name='selectfood',
            name='food',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.food'),
        ),
    ]
