from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from officer.models import officer_account
from django.contrib import messages
from school.models import schoolInfo
# Create your views here.


def enterOfficer(request):
    if request.session.has_key('empid'):
        school = schoolInfo.objects.all()
        return render(request, 'dashboard.html', {'school': school})
    else:
        return render(request, 'login.html')


def registration(request):
    if request == "POST":
        pass
    else:
        return render(request, 'registration.html')


def backlogin(request):
    return render(request, 'login.html')


def officerReg(request):
    if request.method == "POST":
        oname = request.POST['oname']
        oemail = request.POST['oemail']
        oempid = request.POST['oempid']
        opass = request.POST['opass']
        ocpass = request.POST['ocpass']
        oworkp = request.POST['oworkp']
        check_eid = officer_account.objects.filter(oempid=oempid)
        if check_eid:
            messages.success(request, 'Employee ID is already taken!')
            return render(request, 'registration.html')
        else:
            if opass == ocpass:
                acc_save = officer_account(
                    oname=oname, oemail=oemail, oempid=oempid, opass=opass, oworkp=oworkp)
                acc_save.save()
                messages.success(request, 'Registration successfull!')
                return render(request, 'registration.html')
            else:
                messages.success(request, "Password doesn't match!")
                return render(request, 'registration.html')

    else:
        return render(request, 'registration.html')


def offcierLogin(request):
    if request.method == "POST":
        oempid = request.POST['oempid']
        opass = request.POST['opass']
        login = officer_account.objects.filter(oempid=oempid, opass=opass)

        if login:
            request.session['empid'] = oempid
            return render(request, 'dashboard.html')
        else:
            messages.success(request, "Invalid credential! Try again..")
            return render(request, 'login.html')
    else:
        if request.session.has_key('empid'):
            return render(request, 'dashboard.html')
        else:
            return render(request, 'login.html')


def logout(request):
    try:
        del request.session['empid']
    except KeyError:
        pass
    return redirect('home')


def school_detail(request, school_eiin):
    try:
        obj = schoolInfo.objects.get(SchoolEIIN=school_eiin)
    except schoolInfo.DoesNotExist:
        raise Http404
    context = {'school': obj}
    return render(request, 'school_detail_view.html', context)
