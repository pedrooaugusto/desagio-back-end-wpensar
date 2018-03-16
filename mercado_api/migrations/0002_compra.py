# Generated by Django 2.0.3 on 2018-03-09 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mercado_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(default=1)),
                ('preco', models.FloatField(default=0)),
                ('preco_medio', models.FloatField(default=0)),
                ('data', models.DateTimeField(verbose_name='data da compra')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produtos', to='mercado_api.Produto')),
            ],
        ),
    ]
