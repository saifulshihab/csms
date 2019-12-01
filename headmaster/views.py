from django.shortcuts import render, redirect
from initapp.models import teacher_verify, headmaster_account


# Create your views here.


def dashboard(request):
    if request.session.has_key('headmaster_eid'):
        return render(request, 'headmaster/dashboard.html')
    else:
        return redirect('userlogin')


def head_logout(request):
    try:
        del request.session['headmaster_eid']
    except KeyError:
        pass
    return redirect('home')


def about(request):
    return render(request, 'about.html')


def teacherverification(request):
    s_eiin = headmaster_account.objects.get(h_empid = request.session.get('headmaster_eid'))
    check_ein = s_eiin.sch_eiin
    tv = teacher_verify.objects.filter(sch_eiin=check_ein)
    #print(tv.values)
    return render(request, 'headmaster/teacher_verification.html', {'tv': tv})
