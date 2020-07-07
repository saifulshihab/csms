# Generated by Django 2.2.6 on 2020-06-20 15:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='scholl_result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sch_class', models.CharField(default=6, max_length=50)),
                ('eiin', models.CharField(max_length=100)),
                ('year', models.CharField(choices=[('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024')], max_length=100)),
                ('exam_type', models.CharField(choices=[('Half yearly exam', 'Half yearly exam'), ('Final exam', 'Final exam')], max_length=100)),
                ('total_pass', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='student_attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clss', models.CharField(max_length=5)),
                ('todays_attendance', models.IntegerField()),
                ('eiin', models.CharField(max_length=100)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='teacher_account',
            fields=[
                ('t_fullname', models.CharField(max_length=100)),
                ('t_email', models.CharField(max_length=100)),
                ('dp', models.ImageField(default='default.jpg', upload_to='teacher')),
                ('t_empid', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('t_pass', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('t_phone', models.CharField(max_length=50)),
                ('sch_eiin', models.CharField(default=None, max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='teacher_verify',
            fields=[
                ('t_fullname', models.CharField(max_length=100)),
                ('t_email', models.CharField(max_length=100)),
                ('t_empid', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('dp', models.ImageField(default='default.jpg', upload_to='teacher')),
                ('t_pass', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('t_phone', models.CharField(max_length=50)),
                ('sch_eiin', models.CharField(default=None, max_length=25)),
            ],
        ),
    ]
