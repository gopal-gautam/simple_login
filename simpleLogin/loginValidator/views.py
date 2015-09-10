from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import LoginForm
import csv

def get_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			first_name = form.cleaned_data["firstName"]
			last_name = form.cleaned_data["lastName"]
			phone = form.cleaned_data["phone"]
			address = form.cleaned_data["address"]
			with open("/home/gopal/env/simple_login/simpleLogin/data.csv", "rb") as csvfile:
				datareader = csv.reader(csvfile, delimiter=",")
				for datalist in datareader:
					row = [item.strip().lower() for item in datalist]
					if first_name.lower() in row and last_name.lower() in row and phone.lower() in row and address.lower() in row:
						message = "Welcome to the site"
						return render(request, "welcome.html", {"message":message})	
					else:
						message = "Sorry we dont recognize you"
						return render(request, "login.html", {"message":message, "form":form})
	else:
		form = LoginForm()

	return render(request, 'login.html', {'form':form})
# Create your views here.
