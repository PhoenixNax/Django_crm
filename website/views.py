from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from website.forms import SignUpForm, AddRecordForm
from website.models import Record

# Create your views here.

def home(request):
  records = Record.objects.all()
  #check to see if logging in 
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    # Authenticate
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      messages.success(request, "You have been Logged In!")
      return redirect('website:home')
    else: 
      messages.success(request, "There was an error logging in, please try again.")
      return redirect('website:home')
  else:
    context = {'records': records}
    return render(request, "website/home.html", context)

def login_user(request):
  pass

def logout_user(request):
  logout(request)
  messages.success(request, "You have been Logged Out...")
  return redirect('website:home')

def register_user(request):
  return render(request, "website/register.html", {})

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('website:home')
	else:
		form = SignUpForm()
		return render(request, 'website/register.html', {'form':form})

	return render(request, 'website/register.html', {'form':form})

def customer_record(request, record_id):
  if request.user.is_authenticated:
    records = Record.objects.get(id=record_id)
    context = {'record': records}
    return render(request, "website/record.html", context)
  else:
    messages.success(request, "You need to be logged in to view this page.")
    return redirect('website:home')

def delete_record(request, record_id):
  if request.user.is_authenticated:
    delete_it = Record.objects.get(id=record_id)
    delete_it.delete()
    messages.success(request, "Record has been deleted.")
    return redirect('website:home')
  else:
    messages.success(request, "You need to be logged in to delete a record.")
    return redirect('website:home')

def add_record(request):
  form = AddRecordForm(request.POST or None)
  if request.user.is_authenticated:
      if request.method == "POST":
          if form.is_valid():
            add_record = form.save()
            messages.success(request, "Record Added...")
            return redirect('website:home')
      context = {'form': form}
      return render(request, "website/add_record.html", context)
  else:
    messages.success(request, "You need to be logged in to add a record.")
    return redirect('website:home')

def update_record(request, record_id):
  if request.user.is_authenticated:
    current_record = Record.objects.get(id=record_id)
    form = AddRecordForm(request.POST or None, instance=current_record)
    if form.is_valid():
      form.save()
      messages.success(request, "Record has been updated.")
      return redirect('website:home')
    context = {'form': form}
    return render(request, "website/update_record.html", context)
  else:
    messages.success(request, "You need to be logged in to update a record.")
    return redirect('website:home')

