# Generated by Django 3.2.17 on 2023-04-20 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20230420_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='course',
            field=models.CharField(blank=True, choices=[('M.TECH', 'Master of Technology'), ('MCA', 'Master of Computer Applications'), ('MSc', 'Master of Science, Data Science'), ('OTH', 'others'), ('B.TECH', 'Bachelor of Technology')], max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('female', 'Female'), ('male', 'Male'), ('others', 'Others')], max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='institute',
            field=models.CharField(blank=True, choices=[('NIT RRK', 'National Institute of Technology, Rourkela'), ('OTH', 'others'), ('CUTM BBSR', 'Centurion University of Technology and Management, Bhubaneswar'), ('CVRGU BBSR', 'C. V. Raman Global University, Bhubaneswar'), ('SOA BBSR', "Siksha 'O' Anusandhan University, Bhubaneswar"), ('IGIT DNKL', 'Indira Gandhi Institute of Technology, Dhenkanal'), ('GIFT', 'Gandhi Institute for Technology, Bhubaneswar'), ('GIET GNPR', 'GIET University, Gunupur'), ('NIST BAM', 'National Institute of Science and Technology, Berhampur'), ('ITER BBSR', 'Institute of Technical Education and Research, Bhubaneswar'), ('COEB BBSR', 'College of Engineering Bhubaneswar, Bhubaneswar'), ('CUTM PLH', 'Centurion University of Technology and Management, Paralkhemundi'), ('VSSUT SBP', 'Veer Surendra Sai University of Technology, Burla'), ('IIIT BBSR', 'International Institute of Information Technology, Bhubaneswar'), ('SIT SBP', 'Silicon Institute of Technology, Sambalpur'), ('SIT BBSR', 'Silicon Institute of Technology, Bhubaneswar'), ('BPUT BBSR', 'Biju Patnaik University of Technology, Rourkela'), ('CET', 'College of Engineering and Technology, Bhubaneswar'), ('IIT BBSR', 'Indian Institute of Technology, Bhrbaneswar'), ('KIIT BBSR', 'Kalinga Institute of Industrial Technology, Bhubaneswar'), ('XIM BBSR', 'XIM University, Bhubaneswar'), ('BEC BBSR', 'Bhubaneswar Engineering College, Bhubaneswar'), ('SSU CTC', 'Sri Sri University, Cuttack')], max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='yop',
            field=models.CharField(choices=[('2026', '2026'), ('2024', '2024'), ('2023', '2023'), ('2025', '2025')], default='2023', max_length=4),
        ),
    ]