# Generated by Django 3.2.9 on 2021-11-20 23:02

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
            name='Categoria_Prov',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=4, max_digits=20)),
                ('f_inicio', models.DateTimeField()),
                ('f_fin', models.DateTimeField()),
                ('activo', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nit', models.CharField(max_length=20, verbose_name='num_doc')),
                ('nombre', models.CharField(max_length=100, verbose_name='nombre')),
                ('direccion', models.CharField(max_length=100, verbose_name='direccion')),
                ('ciudad', models.CharField(max_length=50, verbose_name='ciudad')),
                ('activo', models.BooleanField(default=False)),
                ('imagen', models.CharField(max_length=250, verbose_name='imagen')),
                ('cat_prov', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proveedor', to='appEcoturism.categoria_prov')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=False)),
                ('imagen', models.CharField(max_length=250, verbose_name='imagen')),
                ('precio', models.DecimalField(decimal_places=4, max_digits=20)),
                ('plan', models.ManyToManyField(blank=True, related_name='servicio', to='appEcoturism.Plan')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servicio', to='appEcoturism.proveedor')),
                ('tipo_serv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servicio', to='appEcoturism.tipo_servicio')),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('num_doc', models.CharField(max_length=20, verbose_name='num_doc')),
                ('ciudad', models.CharField(max_length=50, verbose_name='ciudad')),
                ('celular', models.CharField(max_length=100, verbose_name='celular')),
                ('direccion', models.CharField(max_length=100, verbose_name='direccion')),
                ('activo', models.BooleanField(default=False)),
                ('imagen', models.CharField(max_length=250, verbose_name='imagen')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perfil', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
