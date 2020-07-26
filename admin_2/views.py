from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.views import View
from django.forms.models import inlineformset_factory


@login_required(login_url='login')
def homeAdmin(request):
    all_notice = NoticeBoard.objects.all()
    allDonor = donorInfo.objects.all()
    allDonor_count = allDonor.count()
    a_pos = allDonor.filter(blood_group='A+').count()
    a_neg = allDonor.filter(blood_group='A-').count()
    ab_pos = allDonor.filter(blood_group='AB+').count()
    ab_neg = allDonor.filter(blood_group='AB-').count()
    o_pos = allDonor.filter(blood_group='O+').count()
    o_neg = allDonor.filter(blood_group='O-').count()
    b_pos = allDonor.filter(blood_group='B+').count()
    b_neg = allDonor.filter(blood_group='B-').count()
    ava_don = allDonor.filter(donor_status=True).count()
    context = {'a_pos': a_pos, 'a_neg': a_neg, 'ab_pos': ab_pos, 'ab_neg': ab_neg, 'o_pos': o_pos,
               'o_neg': o_neg, 'b_pos': b_pos, 'b_neg': b_neg, 'allDonor': allDonor_count,
               'all_notice': all_notice, 'ava_don': ava_don}
    template = 'admin_2/index.html'
    return render(request, template, context)


@login_required(login_url='login')
def donorTable(request):
    info = MotivatedDonorTable.objects.all()
    context = {'donor_list': info}
    template = 'admin_2/tables.html'
    return render(request, template, context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('homeAdmin')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homeAdmin')
        else:
            messages.info(request, ' invalid username or password')
    template = 'admin_2/authentication-login.html'
    context = {}
    return render(request, template, context)


def logout_user(request):
    logout(request)
    return redirect('login')


def registerPage(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.warning(request, 'password are not matching')
    form = CustomUserCreationForm()
    template = 'admin_2/authentication-register.html'
    context = {'form': form}
    return render(request, template, context)


@login_required(login_url='login')
def formAdmin(request):
    context = {}
    template = 'admin_2/form-basic.html'
    return render(request, template, context)


@login_required(login_url='login')
def TriageVol(request):
    form = TriageFormVolunteer(request.POST or None)
    if form.is_valid():
        form.save()
        form = TriageFormVolunteer()
        messages.success(request, "Submitted successfully")
    context = {'form': form}
    template = 'admin_2/form1.html'
    return render(request, template, context)


@login_required(login_url='login')
def calendar(request):
    context = {}
    template = 'admin_2/pages-calendar.html'
    return render(request, template, context)


@login_required(login_url='login')
def viewDetail(request, pk):
    donor_detail = donorInfo.objects.get(id=pk)
    context = {'donor': donor_detail}
    template = 'admin_2/donor-detail.html'
    return render(request, template, context)


##############################################################################


def homePublic(request):
    units = donorInfo.objects.all()
    context = {'units': units}
    template = 'admin_2/index2.html'
    return render(request, template, context)


def plasmaForm(request):
    form = DonorFormPublic(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Form submitted. Thank You.")
        form = DonorFormPublic()
    context = {'form': form}
    template = 'admin_2/form3.html'
    return render(request, template, context)


def reqFormVol(request):
    form = RequisitionFormVolunteer(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = RequisitionFormVolunteer()
        messages.success(request, "Form Submitted successfully")
    context = {'form': form}
    template = 'admin_2/reqVol.html'
    return render(request, template, context)


def reqFormPub(request):
    form = RequisitionFormPublic(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = RequisitionFormPublic()
        messages.success(request, "Form submitted successfully")
    context = {'form': form}
    template = 'admin_2/reqPub.html'
    return render(request, template, context)


def donorVol(request):
    form = DonorFormVolunteer(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = DonorFormVolunteer()
        messages.success(request, "Form submitted successfully")
    context = {'form': form}
    template = 'admin_2/donVol.html'
    return render(request, template, context)


def motDonForm(request):
    form = MotivatedDonorFormVolunteer(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = DonorFormVolunteer()
        messages.success(request, "Form submitted successfully")
    context = {'form': form}
    template = 'admin_2/motDon.html'
    return render(request, template, context)


def triageTable(request):
    info = triagePatient.objects.all()
    context = {'triage_list': info}
    template = 'admin_2/triTable.html'
    return render(request, template, context)


def reqTable(request):
    info = Requester.objects.all()
    context = {'req_list': info}
    template = 'admin_2/reqTable.html'
    return render(request, template, context)


def donReqTable(request):
    info = DonorRequesterRelation.objects.all()
    context = {'donReq_list': info}
    template = 'admin_2/donReqTable.html'
    return render(request, template, context)


def triageView(request, pk):
    donor_detail = triagePatient.objects.get(id=pk)
    context = {'donor': donor_detail}
    template = 'admin_2/triage-detail.html'
    return render(request, template, context)


def reqView(request, pk):
    donor_detail = Requester.objects.get(id=pk)
    context = {'donor': donor_detail}
    template = 'admin_2/req-view.html'
    return render(request, template, context)


@login_required(login_url='login')
def donReqForm(request):
    form = DonorRequisitionFormVolunteer(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = DonorRequisitionFormVolunteer()
        messages.success(request, "Form submitted successfully")
    context = {'form': form}
    template = 'admin_2/donReqForm.html'
    return render(request, template, context)


class donReqFormView(View):
    def get(self, request):
        form = DonorRequisitionFormVolunteer()
        template = 'admin_2/donReqForm.html'
        context = {'form': form}
        return render(request, template, context)

    def post(self, request, *args, **kwargs):
        form = DonorRequisitionFormVolunteer(request.POST)
        if form.is_valid():
            motive = form.cleaned_data.get('donor').donor
            if motive.motivateddonortable.num_of_don:
                motive.motivateddonortable.num_of_don += 1
            else:
                motive.motivateddonortable.num_of_don = 1
            motive.motivateddonortable.last_don_date = datetime.now()
            motive.motivateddonortable.save()
            form.save()
            form = DonorRequisitionFormVolunteer()
        context = {'form': form}
        template = 'admin_2/donReqForm.html'
        return render(request, template, context)

