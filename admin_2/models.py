from django.db import models

sex_cat = (
    ('male', 'male'),
    ('female', 'female'),
    ('Others', 'Others'),
)

Area = (
    ('Barguna', 'Barguna'),
    ('Barisal', 'Barisal'),
    ('Bhola', 'Bhola'),
    ('Jhalokati', 'Jhalokati'),
    ('Patuakhali', 'Patuakhali'),
    ('Pirojpur', 'Pirojpur'),
    ('Bandarban', 'Bandarban'),
    ('Brahmanbaria', 'Brahmanbaria'),
    ('Chandpur', 'Chandpur'),
    ('Chittagong', 'Chittagong'),
    ('Comilla', 'Comilla'),
    ("Cox's Bazar", "Cox's Bazar"),
    ('Feni', 'Feni'),
    ('Khagrachari', 'Khagrachari'),
    ('Lakshmipur', 'Lakshmipur'),
    ('Noakhali', 'Noakhali'),
    ('Rangamati', 'Rangamati'),
    ('Dhaka', 'Dhaka'),
    ('Faridpur', 'Faridpur'),
    ('Gazipur', 'Gazipur'),
    ('Gopalganj', 'Gopalganj'),
    ('Kishoreganj', 'Kishoreganj'),
    ('Madaripur', 'Madaripur'),
    ('Manikganj', 'Manikganj'),
    ('Munshiganj', 'Munshiganj'),
    ('Narayanganj', 'Narayanganj'),
    ('Narsingdi', 'Narsingdi'),
    ('Rajbari', 'Rajbari'),
    ('Shariatpur', 'Shariatpur'),
    ('Tangail', 'Tangail'),
    ('Bagerhat', 'Bagerhat'),
    ('Chuadanga', 'Chuadanga'),
    ('Jessore', 'Jessore'),
    ('Jhenaidah', 'Jhenaidah'),
    ('Khulna', 'Khulna'),
    ('Kushtia', 'Kushtia'),
    ('Magura', 'Magura'),
    ('Meherpur', 'Meherpur'),
    ('Narail', 'Narail'),
    ('Satkhira', 'Satkhira'),
    ('Jamalpur', 'Jamalpur'),
    ('Mymensingh', 'Mymensingh'),
    ('Netrokona', 'Netrokona'),
    ('Sherpur', 'Sherpur'),
    ('Bogra', 'Bogra'),
    ('Jaipurhat', 'Jaipurhat'),
    ('Naogaon', 'Naogaon'),
    ('Natore', 'Natore'),
    ('Nawabganj', 'Nawabganj'),
    ('Pabna', 'Pabna'),
    ('Rajshahi', 'Rajshahi'),
    ('Sirajganj', 'Sirajganj'),
    ('Dinajpur', 'Dinajpur'),
    ('Gaibandha', 'Gaibandha'),
    ('Kurigram', 'Kurigram'),
    ('Lalmonirhat', 'Lalmonirhat'),
    ('Nilphamari', 'Nilphamari'),
    ('Panchagarh', 'Panchagarh'),
    ('Rangpur', 'Rangpur'),
    ('Thakurgaon', 'Thakurgaon'),
    ('Habiganj', 'Habiganj'),
    ('Moulvibazar', 'Moulvibazar'),
    ('Sunamganj', 'Sunamganj'),
    ('Sylhet', 'Sylhet'),
)
unit = (
    ('AMUMCU', 'AMUMCU'),
    ('BMCU', 'BMCU'),
    ('CMCU', 'CMCU'),
    ('CoxMCU', 'CoxMCU'),
    ('DDCU', 'DDCU'),
    ('EWM&UpDCU', 'EWM'),
    ('FMCU', 'FMCU'),
    ('GSVMCU', 'GSVMCU'),
    ('JRRMCU', 'JRRMCU'),
    ('JMCU', 'JMCU'),
    ('KuMCU', 'KuMCU'),
    ('MARMCU', 'MARMCU'),
    ('MMCU', 'MMCU'),
    ('PKMCU', 'PKMCU'),
    ('RMCU', 'RMCU'),
    ('RmMCU', 'RmMCU'),
    ('RpMCU', 'RpMCU'),
    ('SBMCU', 'SBMCU'),
    ('SMMAMCU', 'SMMAMCU'),
    ('SOMCU', 'SOMCU'),
    ('SSMCU', 'SSMCU'),
    ('SSNIMCU', 'SSNIMCU'),
    ('ShSMCU', 'ShSMCU'),
    ('SZMCU', 'SZMCU'),

)

blood_c = (
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
)


class donorInfo(models.Model):
    area = models.CharField(null=True, blank=False, choices=Area, max_length=40)
    Conceived_before = models.BooleanField(default=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    blood_group = models.CharField(max_length=25, blank=False, null=False, choices=blood_c)
    donor_status = models.BooleanField(default=False)  # ready / not ready
    donation_status = models.BooleanField(default=False)  # donated or not
    last_donation_date = models.DateTimeField(blank=True, null=True)
    times_donated = models.IntegerField(default=0, null=True)
    age = models.IntegerField(null=True, blank=False)
    sex = models.CharField(max_length=10, choices=sex_cat)
    occupation = models.CharField(max_length=200, blank=True, null=True)
    contact_number = models.CharField(blank=False, null=True, max_length=14)
    address = models.TextField(blank=False, null=False)
    comment_of_donor = models.TextField(null=True, blank=True)
    disease = models.CharField(max_length=300, null=True, blank=False)
    hospital_name = models.CharField(max_length=200, blank=True, null=True)
    first_positive = models.DateTimeField(blank=False, null=True)
    first_negative = models.DateTimeField(blank=False, null=True)
    recovery_date = models.DateTimeField(blank=False, null=True, verbose_name='symptom date')
    convinced_before = models.BooleanField(null=True, blank=True)
    m_l = (
        ('Highly Interested', 'Highly Interested'),
        ('Interested', 'Interested'),
        ('Less Interested', 'Less Interested'),

    )
    motivation_level = models.CharField(max_length=25, blank=False, null=True, choices=m_l)
    regional_field = models.CharField(max_length=50, null=False, blank=False, choices=unit)
    entry_date = models.DateTimeField(auto_now_add=True)
    volunteer_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class MotivatedDonorTable(models.Model):
    donor = models.OneToOneField(donorInfo, on_delete=models.CASCADE, null=True)
    num_of_don = models.IntegerField(verbose_name='Number of Donation', blank=True, null=True)
    last_don_date = models.DateTimeField(verbose_name='Last Donation Date', blank=True, null=True)
    f_pos_ava = models.IntegerField(null=True, blank=True, verbose_name='Availability from first positive test')
    f_neg_ava = models.IntegerField(null=True, blank=True, verbose_name='Availability from first negative test')
    s_res_ava = models.IntegerField(null=True, blank=True, verbose_name='Availability from symptom resolution date')
    status = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return f'motivated donor : {self.donor.name} id: {self.donor.id}'


class NoticeBoard(models.Model):
    notice = models.TextField(null=True, blank=True, max_length=200)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.notice


class Requester(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name='patient name')
    emergency_contact = models.CharField(blank=False, null=True, max_length=14)
    blood_group = models.CharField(max_length=25, blank=False, null=False, choices=blood_c)
    hospital_name = models.CharField(max_length=200, blank=True, null=True)
    admission_registration_no = models.CharField(max_length=100, blank=False, null=False)
    plasma_req_form_img = models.FileField(blank=True, null=True)
    emergency_contact_persons_name = models.CharField(blank=False, null=True, max_length=100)
    comment_of_patient = models.TextField(null=True, blank=True)
    reference = models.CharField(max_length=100, blank=True, null=True)
    vol_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Volunteer Name')
    unit_name = models.CharField(max_length=100, blank=False, null=False, choices=unit)
    area = models.CharField(null=True, blank=False, choices=Area, max_length=60)

    def __str__(self):
        return self.name


class triagePatient(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True, verbose_name='patient_name')

    sex = models.CharField(max_length=10, choices=sex_cat)
    age = models.IntegerField(null=False, blank=False)
    contact_number = models.CharField(blank=False, null=True, max_length=14)
    hospital_name = models.CharField(max_length=200, blank=True, null=True)
    first_positive = models.DateTimeField(blank=False, null=False)
    hospital_admit_dt = models.DateTimeField(blank=True, null=True)
    hospital_release_dt = models.DateTimeField(blank=True, null=True)
    area = models.CharField(null=True, blank=False, choices=Area, max_length=40)

    def __str__(self):
        return f'triage patient: {self.name}'


class DonorRequesterRelation(models.Model):
    donor = models.ForeignKey(MotivatedDonorTable, on_delete=models.CASCADE)
    requester = models.ForeignKey(Requester, on_delete=models.CASCADE)

    def __str__(self):
        return f'donor : {self.donor.donor.name} || requester : {self.requester.name}'
