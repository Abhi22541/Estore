from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.views import View
from store.models import Product
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
class Dashboard(View):
    def get(self, request):
        products=Product.objects.all()
        context = {
            'products':products,
        }
        return render(request, 'store/home.html', context) 
    
# class Registrations(View):
#     def post(self, request):
#         form=Userform(request.POST)
#         if form.is_valid():
#             user=form.save()
#             login(request, user)
#             messages.success("Registration Successfully Completed!!")
#             return redirect("main:homepage")
#         messages.error(request, "invalid details provided please check detail again!!")
#         form=Userform()
#         return render(request=request, template_name="store/accounts/register.html", context={"registration_form":form})

def register_request(request):
	if request.method == "POST":
		form = Userform(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = Userform()
	return render (request=request, template_name="store/accounts/register.html", context={"register_form":form})





def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="store/accounts/login.html", context={"login_form":form})

