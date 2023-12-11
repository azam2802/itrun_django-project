from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login , authenticate

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        profile_image = request.FILES.get('profile_image')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        occupation = request.POST.get('occupation')
        skills = request.POST.get('skills')
        birth = request.POST.get('birth')
        if password == confirm_password:
             user = User.objects.create(
                 username = username,
                 email = email,
                 phone = phone,
                 occupation = occupation,
                 skills = skills,
                 birth = birth,
                 profile_image  = profile_image
             )
             user.set_password(password)
             user.save()
             user = User.objects.get(username = username)
             user = authenticate(username = username , password = password)
             login(request , user)
             return redirect('index')
        else:
            return redirect('register')
    return render (request , 'user/register.html')


def user_login(request):
        try:
            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = User.objects.get(username = username)
                user = authenticate(username = username , password = password)
                login(request , user)
                return redirect('index')
            return render (request , 'user/login.html')
        except:
            return errors(request, 'Не верный пароль или имя пользователя! Попробуйте еще раз.')
    
def user_profile(request , id):
    user = User.objects.get(id=id)
    context = {
        'user':user,
    }
    return render (request, 'user/user_profile.html' , context)


def user_update(request , id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        username =  request.POST.get('username')
        email =  request.POST.get('email')
        phone =  request.POST.get('phone')
        occupation = request.POST.get('occupation')
        skills = request.POST.get('skills')
        birth = request.POST.get('birth')
        profile_image = request.FILES.get('profile_image')
        user = User.objects.get(id=id)
        user.username = username
        user.email = email
        user.phone = phone
        user.occupation = occupation
        user.skills = skills
        user.birth = birth
        user.profile_image = profile_image
        user.save()
        return redirect('user_profile' , user.id)
    context = {
        'user':user
    }
    return render(request , 'user/user_update.html' , context )

def user_delete(request , id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        user = User.objects.get(id=id)
        user.delete()
        return redirect('index')
    context = {
        'user' : user
    }
    return render (request , 'user/user_delete.html' , context)


def errors(request, str_err):
    context = {
        'error': str_err
    }
    return render(request, 'errors.html', context)