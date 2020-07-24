from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
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
    context = {'a_pos': a_pos, 'a_neg': a_neg, 'ab_pos': ab_pos, 'ab_neg': ab_neg, 'o_pos': o_pos,
               'o_neg': o_neg, 'b_pos': b_pos, 'b_neg': b_neg, 'allDonor': allDonor_count, 'all_notice': all_notice}
    template = 'admin_2/index.html'
    return render(request, template, context)


@login_required(login_url='login')
def donorTable(request):
    info = donorInfo.objects.all()
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
def formAdmin2(request):
    form = TriageFormVolunteer(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("homeAdmin")
    context = {'form': form}
    template = 'admin_2/form-wizard.html'
    return render(request, template, context)


@login_required(login_url='login')
def calendar(request):
    context = {}
    template = 'admin_2/pages-calendar.html'
    return render(request, template, context)


@login_required(login_url='login')
def viewDetail(request, pk):
    donor_detail = get_object_or_404(id=pk)
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
    print(request.POST.get('name'), form.is_valid())
    if form.is_valid():
        form.save()
        return redirect('homePublic')
    context = {'form': form}
    template = 'admin_2/form3.html'
    return render(request, template, context)


def reqFormVol(request):
    form = RequisitionFormVolunteer(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('homePublic')
    context = {'form': form}
    template = 'admin_2/reqVol.html'
    return render(request, template, context)
