# Generated by Django 3.1.2 on 2020-10-20 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cloth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('closet', models.ImageField(blank=True, null=True, upload_to='clothes/closets/')),
                ('category', models.CharField(default='self', max_length=50, null=True)),
                ('label', models.CharField(choices=[('T', 'Top'), ('B', 'Bottom'), ('D', 'Dress')], default='T', max_length=1, null=True)),
                ('category_num', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Recommend',
            fields=[
                ('index', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('Path', models.CharField(max_length=100)),
                ('label_T', models.IntegerField(default=0)),
                ('label_B', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Selection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('v_id', models.IntegerField(default=0)),
                ('v_up', models.IntegerField(default=0)),
                ('v_up_img', models.CharField(max_length=100, null=True)),
                ('v_down', models.IntegerField(default=0)),
                ('v_down_img', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]