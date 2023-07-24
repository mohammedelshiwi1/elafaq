from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from account.models import Account
from .forms import createuser,notifications,question
from django.contrib import messages
import string,random
from django.contrib.auth.forms import UserCreationForm
from .models import lecture,notfication,questions
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required


def test(request):
    return render(request,"afaq/test.html")

@login_required(login_url='login')
def home(request):
          
          lec1=lecture.objects.filter(lecture_month="jan")
          lec2=lecture.objects.filter(lecture_month="feb")
          lec3=lecture.objects.filter(lecture_month="mar")
          lec4=lecture.objects.filter(lecture_month="apr")
          lec5=lecture.objects.filter(lecture_month="may")
          lec6=lecture.objects.filter(lecture_month="jun")
          lec7=lecture.objects.filter(lecture_month="jul")
          lec8=lecture.objects.filter(lecture_month="aug")
          lec9=lecture.objects.filter(lecture_month="sep")
          lec10=lecture.objects.filter(lecture_month="oct")
          lec11=lecture.objects.filter(lecture_month="nov")
          lec12=lecture.objects.filter(lecture_month="dec")
          return render(request,"afaq/home.html",{
        "lec1":lec1,
        "lec2":lec2,
        "lec3":lec3,
        "lec4":lec4,
        "lec5":lec5,
        "lec6":lec6,
        "lec7":lec7,
        "lec8":lec8,
        "lec9":lec9,
        "lec10":lec10,
        "lec11":lec11,
        "lec12":lec12,
        })
def sign_up(request):
  
  if request.method=="GET":
     form=createuser()
     up =string.ascii_uppercase
     low=string.ascii_lowercase
     num=string.digits
     sym=string.punctuation
     all=up+low+num+sym
     sample=random.sample(all,10)
     password="".join(sample)
     
    
     return render(request,"afaq/register.html",{'form':form
                                                     ,'password':password})
  if request.method=="POST":
     up =string.ascii_uppercase
     low=string.ascii_lowercase
     num=string.digits
     sym=string.punctuation
     all=up+low+num+sym
     sample=random.sample(all,10)
     password="".join(sample)
     
     form=createuser(request.POST)
     print(request.POST)
     if form.is_valid():
            
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
  return redirect('login') 
def log_in(request):
    if request.method == 'POST':
      form=AuthenticationForm(request,data=request.POST)
      if form.is_valid():
         username=form.cleaned_data.get('username')
         password=form.cleaned_data.get('password')
         user =authenticate(username=username,password=password)
         if user is not None:
             login(request,user)
             messages.info(request, f"You are now logged in as {username}.")
             return redirect('home')
         else:
             messages.error(request,"Invalid username or password.")
      else:
          messages.error(request,"Invalid username or password.")
          
    form=AuthenticationForm()
    return render(request, "afaq/login.html", context={"login_form":form})
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("login")
@login_required(login_url='login')
def mess_page(request):
    
    if request.method=="GET":
        notifi=notifications()
        return render(request,"afaq/messages.html",{
            "form":notifi,
        })
    else:
        notifi=notifications(request.POST)
        if notifi.is_valid():
            note=notfication(
                name=notifi.cleaned_data["name"],
                email=notifi.cleaned_data["email"]
                ,number=notifi.cleaned_data["number"],
                des=notifi.cleaned_data["des"],
            )
            note.save()
        return redirect("home")


@login_required(login_url='login')

def lecture_page(request,lecture_title,lecture_slug):
         lec=lecture.objects.get(slug=lecture_slug,title=lecture_title)
         quests=questions.objects.filter(lecture=lec)
         form=question()
         if request.method == 'get':
          return render(request,"afaq/lecture.html",{
          "lec":lec,
          "form":form,
          "quests":quests,
           }) 
         else:  
             form=question(request.POST)
             if form.is_valid():
                 print(form) 
                 quest=questions(
                 user=form.cleaned_data["user"],
                 ques=form.cleaned_data["ques"],
                 lecture=lec )
                 quest.save()
             return render(request,"afaq/lecture.html",{
                  "lec":lec,
                 "form":form,
                 "quests":quests,
                 }) 
              