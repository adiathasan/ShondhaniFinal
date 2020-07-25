from functools import partial
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from .models import *

DateInput = partial(forms.DateInput, {'class': 'datepicker'})

CATEGORY = (
    ('khulna', 'khulna'),
    ('rajshahi', 'rajshahi'),
    ('dhaka', 'dhaka'),
    ('chittagong', 'chittagong'),
)


class registrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['password1', 'password2', 'username', 'email']


class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    email = forms.EmailField(label='Enter email', widget=forms.EmailInput)
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    regional_field = forms.CharField(max_length=50, label='region', widget=forms.Select(choices=CATEGORY))

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['regional_field'],
            self.cleaned_data['password1'],
            # self.cleaned_data['email'],
        )
        return user


class DonorFormPublic(forms.ModelForm):
    first_positive = forms.DateField(widget=DateInput(), label="First positive date")
    first_negative = forms.DateField(widget=DateInput(), label="First negative date")
    recovery_date = forms.DateField(widget=DateInput(), label="Full recovery date")
    choices = (
        ('No disease', "No disease"),
        ('Diabetes', "Diabetes"),
        ('High Blood Pressure', "High Blood Pressure"),
        ('Kidney Disease', "Kidney Disease"),
        ('Heart Disease', "Heart Disease"),
        ('Respiratory Distress', "Respiratory Distress")
    )
    disease = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=choices,
    )

    class Meta:
        model = donorInfo

        fields = ['motivation_level', 'name', 'sex', 'Conceived_before', 'age',
                  'blood_group', 'contact_number', 'address',
                  'area', 'first_positive', 'first_negative', 'recovery_date',
                  'disease', 'occupation', 'comment_of_donor']

    def clean_disease(self):
        disease = self.cleaned_data.get('disease')
        all_disease = []
        for _ in disease:
            if _ == 'No disease' and len(disease) > 1:
                raise forms.ValidationError("You can not select option 'No disease' and others at the same time")
            all_disease.append(_)
        return " || ".join(all_disease)

    def clean_name(self, *args, **kwargs):
        name = self.cleaned_data.get('name')
        check = []
        for i in name:
            try:
                check.append(int(i))
            except ValueError:
                pass
        if len(check) > 0:
            raise forms.ValidationError("Characters only please")
        return name

    def clean_age(self, *args, **kwargs):
        sex = self.cleaned_data.get('sex')
        age = self.cleaned_data.get('age')
        if sex == 'male':
            if 18 > age or age > 50:
                raise forms.ValidationError("Range of male must be between [18-50]")
        if sex == 'female':
            if 18 > age or age > 28:
                raise forms.ValidationError("Range of female must be between [18-50]")
        if sex == 'Others':
            if 18 > age or age > 50:
                raise forms.ValidationError("Range of others must be between [18-50]")
        return age

    def clean_contact_number(self, *args, **kwargs):
        contact_number = self.cleaned_data.get('contact_number')
        try:
            number = [int(_) for _ in contact_number]
            if len(number) != 11:
                raise forms.ValidationError("Must be a 11 digit")
            return contact_number
        except ValueError:
            raise forms.ValidationError("Must be digit only")


class DonorFormVolunteer(forms.ModelForm):
    first_positive = forms.DateField(widget=DateInput(), label="First positive date")
    first_negative = forms.DateField(widget=DateInput(), label="First negative date")
    recovery_date = forms.DateField(widget=DateInput(), label="Full recovery date")
    choices = (
        ('No disease', "No disease"),
        ('Diabetes', "Diabetes"),
        ('High Blood Pressure', "High Blood Pressure"),
        ('Kidney Disease', "Kidney Disease"),
        ('Heart Disease', "Heart Disease"),
        ('Respiratory Distress', "Respiratory Distress")
    )
    disease = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=choices,
    )

    class Meta:
        model = donorInfo

        fields = ['motivation_level', 'name', 'sex', 'Conceived_before', 'age',
                  'blood_group', 'contact_number', 'address',
                  'area', 'first_positive', 'first_negative', 'recovery_date',
                  'disease', 'occupation', 'comment_of_donor', 'volunteer_name',
                  'regional_field']

    def clean_disease(self):
        disease = self.cleaned_data.get('disease')
        all_disease = []
        for _ in disease:
            if _ == 'No disease' and len(disease) > 1:
                raise forms.ValidationError("You can not select option 'No disease' and others at the same time")
            all_disease.append(_)
        return " || ".join(all_disease)

    def clean_name(self, *args, **kwargs):
        name = self.cleaned_data.get('name')
        check = []
        for i in name:
            try:
                check.append(int(i))
            except ValueError:
                pass
        if len(check) > 0:
            raise forms.ValidationError("Characters only please")
        return name

    def clean_age(self, *args, **kwargs):
        sex = self.cleaned_data.get('sex')
        age = self.cleaned_data.get('age')
        if sex == 'male':
            if 18 > age or age > 50:
                raise forms.ValidationError("Range of male must be between [18-50]")
        if sex == 'female':
            if 18 > age or age > 28:
                raise forms.ValidationError("Range of female must be between [18-50]")
        if sex == 'Others':
            if 18 > age or age > 50:
                raise forms.ValidationError("Range of others must be between [18-50]")
        return age

    def clean_contact_number(self, *args, **kwargs):
        contact_number = self.cleaned_data.get('contact_number')
        try:
            number = [int(_) for _ in contact_number]
            if len(number) != 11:
                raise forms.ValidationError("Must be a 11 digit")
            return contact_number
        except ValueError:
            raise forms.ValidationError("Must be digit only")


class RequisitionFormPublic(forms.ModelForm):
    class Meta:
        model = Requester

        fields = ['name', 'blood_group', 'emergency_contact', 'admission_registration_no', 'area',
                  'hospital_name', 'plasma_req_form_img', 'comment_of_patient', 'emergency_contact_persons_name']

    def clean_name(self, *args, **kwargs):
        name = self.cleaned_data.get('name')
        check = []
        for i in name:
            try:
                check.append(int(i))
            except ValueError:
                pass
        if len(check) > 0:
            raise forms.ValidationError("Characters only please")
        return name

    def clean_emergency_contact(self, *args, **kwargs):
        contact_number = self.cleaned_data.get('emergency_contact')
        try:
            number = [int(_) for _ in contact_number]
            if len(number) != 11:
                raise forms.ValidationError("Must be a 11 digit")
            return contact_number
        except ValueError:
            raise forms.ValidationError("Must be digit only")

    def clean_emergency_contact_persons_name(self, *args, **kwargs):
        name = self.cleaned_data.get('emergency_contact_persons_name')
        check = []
        for i in name:
            try:
                check.append(int(i))
            except ValueError:
                pass
        if len(check) > 0:
            raise forms.ValidationError("Characters only please")
        return name

    def clean_hospital_name(self, *args, **kwargs):
        name = self.cleaned_data.get('hospital_name')
        check = []
        for i in name:
            try:
                check.append(int(i))
            except ValueError:
                pass
        if len(check) > 0:
            raise forms.ValidationError("Characters only please")
        return name

    def clean_admission_registration_no(self, *args, **kwargs):
        number = self.cleaned_data.get('admission_registration_no')
        all_reg_num = Requester.objects.filter(admission_registration_no=number)
        if all_reg_num.count() > 0:
            raise forms.ValidationError("Registration number already exists")
        return number


class RequisitionFormVolunteer(forms.ModelForm):
    plasma_req_form_img = forms.ImageField(required=False)

    class Meta:
        model = Requester

        fields = ['name', 'blood_group', 'emergency_contact', 'admission_registration_no', 'area',
                  'hospital_name', 'plasma_req_form_img', 'comment_of_patient', "reference",
                  'emergency_contact_persons_name', "vol_name", "unit_name"]

    def clean_name(self, *args, **kwargs):
        name = self.cleaned_data.get('name')
        check = []
        for i in name:
            try:
                check.append(int(i))
            except ValueError:
                pass
        if len(check) > 0:
            raise forms.ValidationError("Characters only please")
        return name

    def clean_emergency_contact(self, *args, **kwargs):
        contact_number = self.cleaned_data.get('emergency_contact')
        try:
            number = [int(_) for _ in contact_number]
            if len(number) != 11:
                raise forms.ValidationError("Must be a 11 digit")
            return contact_number
        except ValueError:
            raise forms.ValidationError("Must be digit only")

    def clean_emergency_contact_persons_name(self, *args, **kwargs):
        name = self.cleaned_data.get('emergency_contact_persons_name')
        check = []
        for i in name:
            try:
                check.append(int(i))
            except ValueError:
                pass
        if len(check) > 0:
            raise forms.ValidationError("Characters only please")
        return name

    def clean_hospital_name(self, *args, **kwargs):
        name = self.cleaned_data.get('hospital_name')
        check = []
        for i in name:
            try:
                check.append(int(i))
            except ValueError:
                pass
        if len(check) > 0:
            raise forms.ValidationError("Characters only please")
        return name

    def clean_admission_registration_no(self, *args, **kwargs):
        number = self.cleaned_data.get('admission_registration_no')
        all_reg_num = Requester.objects.filter(admission_registration_no=number)
        if all_reg_num.count() > 0:
            raise forms.ValidationError("Registration number already exists")
        return number

    def clean_vol_name(self, *args, **kwargs):
        name = self.cleaned_data.get('vol_name')
        check = []
        for i in name:
            try:
                check.append(int(i))
            except ValueError:
                pass
        if len(check) > 0:
            raise forms.ValidationError("Characters only please")
        return name


class TriageFormVolunteer(forms.ModelForm):
    first_positive = forms.DateField(widget=DateInput(), label="first positive date")
    hospital_admit_dt = forms.DateField(widget=DateInput(), label="hospital admit date")
    hospital_release_dt = forms.DateField(widget=DateInput(), label="hospital release date")

    class Meta:
        model = triagePatient

        fields = ['name', 'sex', 'age', 'area',
                  'hospital_name', 'contact_number', 'first_positive',
                  'hospital_admit_dt', "hospital_release_dt"]

    def clean_name(self, *args, **kwargs):
        name = self.cleaned_data.get('name')
        check = []
        for i in name:
            try:
                check.append(int(i))
            except ValueError:
                pass
        if len(check) > 0:
            raise forms.ValidationError("Characters only please")
        return name

    def clean_contact_number(self, *args, **kwargs):
        contact_number = self.cleaned_data.get('contact_number')
        try:
            number = [int(_) for _ in contact_number]
            if len(number) != 11:
                raise forms.ValidationError("Must be a 11 digit")
            return contact_number
        except ValueError:
            raise forms.ValidationError("Must be digit only")

    def clean_hospital_name(self, *args, **kwargs):
        name = self.cleaned_data.get('hospital_name')
        check = []
        for i in name:
            try:
                check.append(int(i))
            except ValueError:
                pass
        if len(check) > 0:
            raise forms.ValidationError("Characters only please")
        return name

    def clean_age(self, *args, **kwargs):
        sex = self.cleaned_data.get('sex')
        age = self.cleaned_data.get('age')
        print(sex, age, type(age))
        if sex == 'male':
            if 18 > age or age > 50:
                raise forms.ValidationError("Range of male must be between [18-50]")
        if sex == 'female':
            if 18 > age or age > 28:
                raise forms.ValidationError("Range of female must be between [18-28]")
        if sex == 'Others':
            if 18 > age or age > 50:
                raise forms.ValidationError("Range of others must be between [18-50]")
        return age


class MotivatedDonorFormVolunteer(forms.ModelForm):
    class Meta:
        model = MotivatedDonorTable

        fields = ['donor', 'last_don_date', 'f_pos_ava', 'f_neg_ava',
                  's_res_ava', 'status']


class DonorRequisitionFormVolunteer(forms.ModelForm):
    class Meta:
        model = DonorRequesterRelation

        fields = ['donor', 'requester']
