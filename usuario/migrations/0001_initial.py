# Generated by Django 4.1 on 2022-12-09 21:05

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import usuario.validations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('rut', models.CharField(max_length=12, unique=True, validators=[django.core.validators.RegexValidator(message='El rut debe de ser sin puntos y con guion', regex='^[0-9]+-[0-9kK]{1}$'), usuario.validations.ValidacionRut])),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(max_length=36)),
                ('last_name', models.CharField(max_length=36)),
                ('telefono', models.IntegerField(null=True)),
                ('is_cliente', models.BooleanField(default=True)),
                ('is_medico', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=50)),
                ('usuario', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Residente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=12, unique=True, validators=[django.core.validators.RegexValidator(message='El rut debe de ser sin puntos y con guion', regex='^[0-9]+-[0-9kK]{1}$'), usuario.validations.ValidacionRut])),
                ('nombre', models.CharField(max_length=36)),
                ('apellido', models.CharField(max_length=36)),
                ('fecha_estadia', models.DateTimeField(default=django.utils.timezone.now)),
                ('enfermedad', models.TextField(null=True)),
                ('medicamento', models.TextField(null=True)),
                ('esta_activo', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='residente', to='usuario.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='PeticionResidente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('esta_aceptado', models.BooleanField(default=False)),
                ('fecha_peticion', models.DateField(default=django.utils.timezone.now)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.cliente')),
                ('residente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.residente')),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sueldo', models.IntegerField(null=True)),
                ('fecha_contrato', models.DateField(null=True)),
                ('especialidad', models.CharField(max_length=5)),
                ('usuario', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medico', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Control_medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo_visita', models.CharField(max_length=150)),
                ('fecha_control', models.DateTimeField(default=django.utils.timezone.now)),
                ('diagnostico', models.TextField(max_length=300)),
                ('tratamiento', models.TextField(max_length=300)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuario.medico')),
                ('residente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.residente')),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_contrato', models.DateField(null=True)),
                ('sueldo', models.IntegerField(null=True)),
                ('usuario', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
