from django.shortcuts import render, redirect

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
