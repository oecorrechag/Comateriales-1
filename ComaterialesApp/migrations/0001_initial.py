# Generated by Django 3.2.8 on 2021-10-08 01:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogo',
            fields=[
                ('id_catalogo', models.AutoField(primary_key=True, serialize=False)),
                ('categoria', models.CharField(max_length=10)),
                ('clasificacion', models.CharField(max_length=10)),
                ('temporada', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=3)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('city_code', models.CharField(max_length=10)),
                ('country_code', models.CharField(max_length=10)),
                ('created_at', models.TimeField()),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
                ('descripcion', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=15)),
                ('fabricante', models.CharField(max_length=15)),
                ('fecha_creacion', models.DateTimeField()),
                ('unidades', models.IntegerField()),
                ('categoria_catalogo', models.CharField(max_length=10)),
                ('clasificacion_catalogo', models.CharField(max_length=10)),
                ('id_catalogo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ComaterialesApp.catalogo')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('pago', models.IntegerField()),
                ('estado', models.CharField(max_length=20)),
                ('fecha_creacion', models.DateTimeField()),
                ('info', models.CharField(max_length=20)),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ComaterialesApp.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id_detalles', models.AutoField(primary_key=True, serialize=False)),
                ('precio', models.BigIntegerField()),
                ('cantidad', models.IntegerField()),
                ('id_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ComaterialesApp.pedido')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ComaterialesApp.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('balance', models.IntegerField(default=0)),
                ('lastChangeDate', models.DateTimeField()),
                ('isActive', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
