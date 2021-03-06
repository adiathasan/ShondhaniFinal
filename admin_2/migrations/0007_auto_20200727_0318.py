# Generated by Django 3.0.7 on 2020-07-27 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_2', '0006_auto_20200726_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donorinfo',
            name='area',
            field=models.CharField(choices=[('Barguna', 'Barguna'), ('Barisal', 'Barisal'), ('Bhola', 'Bhola'), ('Jhalokati', 'Jhalokati'), ('Patuakhali', 'Patuakhali'), ('Pirojpur', 'Pirojpur'), ('Bandarban', 'Bandarban'), ('Brahmanbaria', 'Brahmanbaria'), ('Chandpur', 'Chandpur'), ('Chittagong', 'Chittagong'), ('Comilla', 'Comilla'), ("Cox's Bazar", "Cox's Bazar"), ('Feni', 'Feni'), ('Khagrachari', 'Khagrachari'), ('Lakshmipur', 'Lakshmipur'), ('Noakhali', 'Noakhali'), ('Rangamati', 'Rangamati'), ('Dhaka', 'Dhaka'), ('Faridpur', 'Faridpur'), ('Gazipur', 'Gazipur'), ('Gopalganj', 'Gopalganj'), ('Kishoreganj', 'Kishoreganj'), ('Madaripur', 'Madaripur'), ('Manikganj', 'Manikganj'), ('Munshiganj', 'Munshiganj'), ('Narayanganj', 'Narayanganj'), ('Narsingdi', 'Narsingdi'), ('Rajbari', 'Rajbari'), ('Shariatpur', 'Shariatpur'), ('Tangail', 'Tangail'), ('Bagerhat', 'Bagerhat'), ('Chuadanga', 'Chuadanga'), ('Jessore', 'Jessore'), ('Jhenaidah', 'Jhenaidah'), ('Khulna', 'Khulna'), ('Kushtia', 'Kushtia'), ('Magura', 'Magura'), ('Meherpur', 'Meherpur'), ('Narail', 'Narail'), ('Satkhira', 'Satkhira'), ('Jamalpur', 'Jamalpur'), ('Mymensingh', 'Mymensingh'), ('Netrokona', 'Netrokona'), ('Sherpur', 'Sherpur'), ('Bogra', 'Bogra'), ('Jaipurhat', 'Jaipurhat'), ('Naogaon', 'Naogaon'), ('Natore', 'Natore'), ('Nawabganj', 'Nawabganj'), ('Pabna', 'Pabna'), ('Rajshahi', 'Rajshahi'), ('Sirajganj', 'Sirajganj'), ('Dinajpur', 'Dinajpur'), ('Gaibandha', 'Gaibandha'), ('Kurigram', 'Kurigram'), ('Lalmonirhat', 'Lalmonirhat'), ('Nilphamari', 'Nilphamari'), ('Panchagarh', 'Panchagarh'), ('Rangpur', 'Rangpur'), ('Thakurgaon', 'Thakurgaon'), ('Habiganj', 'Habiganj'), ('Moulvibazar', 'Moulvibazar'), ('Sunamganj', 'Sunamganj'), ('Sylhet', 'Sylhet')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='donorinfo',
            name='recovery_date',
            field=models.DateTimeField(null=True, verbose_name='symptom date'),
        ),
        migrations.AlterField(
            model_name='donorinfo',
            name='regional_field',
            field=models.CharField(choices=[('AMUMCU', 'AMUMCU'), ('BMCU', 'BMCU'), ('CMCU', 'CMCU'), ('CoxMCU', 'CoxMCU'), ('DDCU', 'DDCU'), ('EWM&UpDCU', 'EWM'), ('FMCU', 'FMCU'), ('GSVMCU', 'GSVMCU'), ('JRRMCU', 'JRRMCU'), ('JMCU', 'JMCU'), ('KuMCU', 'KuMCU'), ('MARMCU', 'MARMCU'), ('MMCU', 'MMCU'), ('PKMCU', 'PKMCU'), ('RMCU', 'RMCU'), ('RmMCU', 'RmMCU'), ('RpMCU', 'RpMCU'), ('SBMCU', 'SBMCU'), ('SMMAMCU', 'SMMAMCU'), ('SOMCU', 'SOMCU'), ('SSMCU', 'SSMCU'), ('SSNIMCU', 'SSNIMCU'), ('ShSMCU', 'ShSMCU'), ('SZMCU', 'SZMCU')], max_length=50),
        ),
        migrations.AlterField(
            model_name='requester',
            name='area',
            field=models.CharField(choices=[('Barguna', 'Barguna'), ('Barisal', 'Barisal'), ('Bhola', 'Bhola'), ('Jhalokati', 'Jhalokati'), ('Patuakhali', 'Patuakhali'), ('Pirojpur', 'Pirojpur'), ('Bandarban', 'Bandarban'), ('Brahmanbaria', 'Brahmanbaria'), ('Chandpur', 'Chandpur'), ('Chittagong', 'Chittagong'), ('Comilla', 'Comilla'), ("Cox's Bazar", "Cox's Bazar"), ('Feni', 'Feni'), ('Khagrachari', 'Khagrachari'), ('Lakshmipur', 'Lakshmipur'), ('Noakhali', 'Noakhali'), ('Rangamati', 'Rangamati'), ('Dhaka', 'Dhaka'), ('Faridpur', 'Faridpur'), ('Gazipur', 'Gazipur'), ('Gopalganj', 'Gopalganj'), ('Kishoreganj', 'Kishoreganj'), ('Madaripur', 'Madaripur'), ('Manikganj', 'Manikganj'), ('Munshiganj', 'Munshiganj'), ('Narayanganj', 'Narayanganj'), ('Narsingdi', 'Narsingdi'), ('Rajbari', 'Rajbari'), ('Shariatpur', 'Shariatpur'), ('Tangail', 'Tangail'), ('Bagerhat', 'Bagerhat'), ('Chuadanga', 'Chuadanga'), ('Jessore', 'Jessore'), ('Jhenaidah', 'Jhenaidah'), ('Khulna', 'Khulna'), ('Kushtia', 'Kushtia'), ('Magura', 'Magura'), ('Meherpur', 'Meherpur'), ('Narail', 'Narail'), ('Satkhira', 'Satkhira'), ('Jamalpur', 'Jamalpur'), ('Mymensingh', 'Mymensingh'), ('Netrokona', 'Netrokona'), ('Sherpur', 'Sherpur'), ('Bogra', 'Bogra'), ('Jaipurhat', 'Jaipurhat'), ('Naogaon', 'Naogaon'), ('Natore', 'Natore'), ('Nawabganj', 'Nawabganj'), ('Pabna', 'Pabna'), ('Rajshahi', 'Rajshahi'), ('Sirajganj', 'Sirajganj'), ('Dinajpur', 'Dinajpur'), ('Gaibandha', 'Gaibandha'), ('Kurigram', 'Kurigram'), ('Lalmonirhat', 'Lalmonirhat'), ('Nilphamari', 'Nilphamari'), ('Panchagarh', 'Panchagarh'), ('Rangpur', 'Rangpur'), ('Thakurgaon', 'Thakurgaon'), ('Habiganj', 'Habiganj'), ('Moulvibazar', 'Moulvibazar'), ('Sunamganj', 'Sunamganj'), ('Sylhet', 'Sylhet')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='requester',
            name='unit_name',
            field=models.CharField(choices=[('AMUMCU', 'AMUMCU'), ('BMCU', 'BMCU'), ('CMCU', 'CMCU'), ('CoxMCU', 'CoxMCU'), ('DDCU', 'DDCU'), ('EWM&UpDCU', 'EWM'), ('FMCU', 'FMCU'), ('GSVMCU', 'GSVMCU'), ('JRRMCU', 'JRRMCU'), ('JMCU', 'JMCU'), ('KuMCU', 'KuMCU'), ('MARMCU', 'MARMCU'), ('MMCU', 'MMCU'), ('PKMCU', 'PKMCU'), ('RMCU', 'RMCU'), ('RmMCU', 'RmMCU'), ('RpMCU', 'RpMCU'), ('SBMCU', 'SBMCU'), ('SMMAMCU', 'SMMAMCU'), ('SOMCU', 'SOMCU'), ('SSMCU', 'SSMCU'), ('SSNIMCU', 'SSNIMCU'), ('ShSMCU', 'ShSMCU'), ('SZMCU', 'SZMCU')], max_length=100),
        ),
        migrations.AlterField(
            model_name='triagepatient',
            name='area',
            field=models.CharField(choices=[('Barguna', 'Barguna'), ('Barisal', 'Barisal'), ('Bhola', 'Bhola'), ('Jhalokati', 'Jhalokati'), ('Patuakhali', 'Patuakhali'), ('Pirojpur', 'Pirojpur'), ('Bandarban', 'Bandarban'), ('Brahmanbaria', 'Brahmanbaria'), ('Chandpur', 'Chandpur'), ('Chittagong', 'Chittagong'), ('Comilla', 'Comilla'), ("Cox's Bazar", "Cox's Bazar"), ('Feni', 'Feni'), ('Khagrachari', 'Khagrachari'), ('Lakshmipur', 'Lakshmipur'), ('Noakhali', 'Noakhali'), ('Rangamati', 'Rangamati'), ('Dhaka', 'Dhaka'), ('Faridpur', 'Faridpur'), ('Gazipur', 'Gazipur'), ('Gopalganj', 'Gopalganj'), ('Kishoreganj', 'Kishoreganj'), ('Madaripur', 'Madaripur'), ('Manikganj', 'Manikganj'), ('Munshiganj', 'Munshiganj'), ('Narayanganj', 'Narayanganj'), ('Narsingdi', 'Narsingdi'), ('Rajbari', 'Rajbari'), ('Shariatpur', 'Shariatpur'), ('Tangail', 'Tangail'), ('Bagerhat', 'Bagerhat'), ('Chuadanga', 'Chuadanga'), ('Jessore', 'Jessore'), ('Jhenaidah', 'Jhenaidah'), ('Khulna', 'Khulna'), ('Kushtia', 'Kushtia'), ('Magura', 'Magura'), ('Meherpur', 'Meherpur'), ('Narail', 'Narail'), ('Satkhira', 'Satkhira'), ('Jamalpur', 'Jamalpur'), ('Mymensingh', 'Mymensingh'), ('Netrokona', 'Netrokona'), ('Sherpur', 'Sherpur'), ('Bogra', 'Bogra'), ('Jaipurhat', 'Jaipurhat'), ('Naogaon', 'Naogaon'), ('Natore', 'Natore'), ('Nawabganj', 'Nawabganj'), ('Pabna', 'Pabna'), ('Rajshahi', 'Rajshahi'), ('Sirajganj', 'Sirajganj'), ('Dinajpur', 'Dinajpur'), ('Gaibandha', 'Gaibandha'), ('Kurigram', 'Kurigram'), ('Lalmonirhat', 'Lalmonirhat'), ('Nilphamari', 'Nilphamari'), ('Panchagarh', 'Panchagarh'), ('Rangpur', 'Rangpur'), ('Thakurgaon', 'Thakurgaon'), ('Habiganj', 'Habiganj'), ('Moulvibazar', 'Moulvibazar'), ('Sunamganj', 'Sunamganj'), ('Sylhet', 'Sylhet')], max_length=40, null=True),
        ),
    ]
