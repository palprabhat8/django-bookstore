from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Book

# Create your views here.

def homepage(request):
	return render(request, template_name='store/home.html')

def storepage(request):
	if request.method == "GET":
		books = Book.objects.filter(buyer = None)
		return render(request, template_name='store/bookspage.html', context={'books':books})
	if request.method == "POST":
		purchased_book = request.POST.get('purchased-book')
		if purchased_book:
			book_bought = Book.objects.filter(name = purchased_book).first()
			book_bought.buyer= request.user
			book_bought.save()
			messages.success(request, f'You have successfully bought {book_bought.name} for {book_bought.price}!')
		return redirect('books')



def loginpage(request):
	if request.method == 'GET':
		return render(request, template_name='store/login.html')
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			login(request, user)
			return redirect('books')
		else:
			return redirect('login')


def logoutpage(request):
	logout(request)
	return redirect('home')

def registerpage(request):
	if request.method == "GET":
		return render(request, template_name='store/register.html')
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('books')
		else:
			return redirect('register')

	

