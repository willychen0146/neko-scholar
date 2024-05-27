from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.core.mail import send_mail

import json
import markdown2

# Create your views here.
from .models import *
from .forms import PostForm, CreateUserForm, AccountForm, EmailForm, MessageForm
from .filters import CommentFilter, PostFilter
from .decorators import unauthenticated_user, allowed_users, admin_only
from datetime import datetime
from .serializers import UserSerailizer

# register and login
@unauthenticated_user
def registerPage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			# user = form.save()
			user = form.save(commit=False)  # Save the form, but don't commit to the database yet
			user.is_staff = True  # Set the user as staff
			user.save()  # Save the user to the database

			username = form.cleaned_data.get('username')


			messages.success(request, 'Account was created for ' + username)

			return redirect('login')
		

	context = {'form':form}
	return render(request, 'register.html', context)

@unauthenticated_user
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

# @login_required(login_url='login')
@admin_only
def adminHome(request):
	posts = Post.objects.all()
	accounts = Account.objects.all()

	total_accounts = accounts.count()

	elementary = posts.filter(category='Elementary').count()
	junior = posts.filter(category='Junior').count()
	senior = posts.filter(category='Senior').count()

	context = {'posts':posts, 'accounts':accounts,
	'elementary':elementary,'junior':junior,
	'senior':senior }

	return render(request, 'dashboard.html', context)

def home(request):
	posts = Post.objects.all().order_by('-date_created')

	elementary = posts.filter(category='Elementary').count()
	junior = posts.filter(category='Junior').count()
	senior = posts.filter(category='Senior').count()

	# Parse date range from request 
	date_range = request.GET.get('date_range', '') 
	if date_range: 
		dates = date_range.split(' to ') 
		if len(dates) == 2: 
			start_date, end_date = dates 
			posts = posts.filter(date_created__date__gte=datetime.strptime(start_date, '%Y-%m-%d'), date_created__date__lte=datetime.strptime(end_date, '%Y-%m-%d'))

	myFilter = PostFilter(request.GET, queryset=posts)
	posts = myFilter.qs

	# Pagination
	paginator = Paginator(posts, 5) # Show 5 posts per page
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	context = {'page_obj':page_obj, 'elementary':elementary,
	'junior':junior,'senior':senior, 'myFilter':myFilter}
	return render(request, 'home.html', context)

# account settings for user
@login_required(login_url='login')
@allowed_users(allowed_roles=['guest'])
def accountSettings(request):
	account = request.user.account
	followed_posts = Follow.objects.filter(follower=account)
	form = AccountForm(instance=account)

	if request.method == 'POST':
		form = AccountForm(request.POST, request.FILES,instance=account)
		if form.is_valid():
			form.save()


	context = {'form':form, 'followed_posts':followed_posts}
	return render(request, 'account_settings.html', context)

# posts for admin and user
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','guest'])
def posts(request):
	posts = Post.objects.all()

	return render(request, 'posts.html', {'posts':posts})

# modify posts for admin
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def guest(request, pk_test):
	account = Account.objects.get(id=pk_test)

	posts = account.post_set.all()
	post_count = posts.count()

	myFilter = PostFilter(request.GET, queryset=posts)
	posts = myFilter.qs 

	context = {'account':account, 'posts':posts, 'post_count':post_count,
	'myFilter':myFilter}
	return render(request, 'guest.html',context)

# create, update, and delete posts for admin
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createPost(request, pk):
	PostFormSet = inlineformset_factory(Account, Post, fields=('content', 'category', 'tags'), extra=10 )
	account = Account.objects.get(id=pk)
	formset = PostFormSet(queryset=Post.objects.none(),instance=account)
	if request.method == 'POST':
		form = PostForm(request.POST)
		formset = PostFormSet(request.POST, instance=account)
		if formset.is_valid():
			formset.save()
			return redirect('/')

	context = {'form':formset}
	return render(request, 'post_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updatePost(request, pk):
	post = Post.objects.get(id=pk)
	form = PostForm(instance=post)
	print('POST:', post)
	if request.method == 'POST':

		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'post_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deletePost(request, pk):
	post = Post.objects.get(id=pk)
	if request.method == "POST":
		post.delete()
		return redirect('/')

	context = {'item':post}
	return render(request, 'delete.html', context)

def about(request):
    return render(request, 'about.html')

@login_required
def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            recipient_email = form.cleaned_data['recipient_email']
            message = form.cleaned_data['message']
            send_mail(
                subject='Email from Django App',
                message=message,
                from_email=request.user.email,
                recipient_list=[recipient_email],
                fail_silently=False,
            )
            return redirect('email_sent')
    else:
        form = EmailForm()
    return render(request, 'send_email.html', {'form': form})

def email_sent(request):
    return render(request, 'email_sent.html')

# dark/light mode
@login_required
def userSettings(request):
    account = request.user.account
    setting = account.setting

    serializer = UserSerailizer(setting, many=False)

    return JsonResponse(serializer.data, safe=False)

@login_required
def updateTheme(request):
    try:
        data = json.loads(request.body)
        theme = data.get('theme')
        if not theme:
            return JsonResponse({'message': 'Theme is required.'}, status=400)

        account = request.user.account
        setting = account.setting
        if setting:
            setting.value = theme
            setting.save()
            print('Request:', theme)
            return JsonResponse({'message': 'Updated..'}, status=200)
        else:
            return JsonResponse({'message': 'Setting not found.'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'message': 'Invalid JSON.'}, status=400)

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST, user=request.user)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user.account
            message.save()
            return redirect('inbox')
    else:
        form = MessageForm(user=request.user)
    return render(request, 'send_message.html', {'form': form})

@login_required
def inbox(request):
    received_messages = Message.objects.filter(receiver=request.user.account)
    return render(request, 'inbox.html', {'messages': received_messages})

def contact(request):
	return render(request, 'contact.html')

def user_profile(request, user_id):
    # Retrieve the user by username
    user = get_object_or_404(User, id=user_id)
    
    # Pass the user to the template
    return render(request, 'user_profile.html', {'profile_user': user})