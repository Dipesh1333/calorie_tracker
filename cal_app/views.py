# STD imports
from datetime import timedelta
from datetime import date
# django imports
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# local imports
from .forms import SelectFoodForm,CreateUserForm,ProfileForm
from .models import Profile,FoodConsumptionPerDay,Food


#home page view
@login_required(login_url='login')
def HomePageView(request):

	#taking the latest profile object
	calories = Profile.objects.filter(person_of=request.user).last()
	calorie_goal = calories.calorie_goal
	
	#creating one profile each day
	if date.today() > calories.date:
		profile=Profile.objects.create(person_of=request.user,calorie_count = calories.calorie_count)
		profile.save()

	calories = Profile.objects.filter(person_of=request.user).last()
		
	# showing all food consumed present day

	all_food_today=FoodConsumptionPerDay.objects.filter(profile=calories)
	
	calorie_goal_status = calorie_goal -calories.total_calorie
	over_calorie = 0
	if calorie_goal_status < 0 :
		over_calorie = abs(calorie_goal_status)

	context = {
	'total_calorie':calories.total_calorie,
	'calorie_goal':calorie_goal,
	'calorie_goal_status':calorie_goal_status,
	'over_calorie' : over_calorie,
	'food_selected_today':all_food_today
	}
	

	return render(request, 'home.html',context)


#for selecting food each day
@login_required
def select_food(request):
	person = Profile.objects.filter(person_of=request.user).last()
	#for showing all food items available
	food_items = Food.objects.all()#filter(person_of=request.user)
	form = SelectFoodForm(request.user,instance=person)
	if request.method == 'POST':
		form = SelectFoodForm(request.user,request.POST,instance=person)
		if form.is_valid():
			if person.quantity > 0:
				form.save()
				return redirect('home')
			else:
				messages.info(request,'Please Enter quantity of food more then zero')
	else:
		form = SelectFoodForm(request.user)

	context = {'form':form,'food_items':food_items}
	return render(request, 'select_food.html',context)


#for deleting food given by the user
@login_required
def delete_food(request,pk):
	food_item = Food.objects.get(id=pk)
	if request.method == "POST":
		food_item.delete()
		return redirect('profile')
	context = {'food':food_item,}
	return render(request,'delete_food.html',context)

#profile page of user
@login_required
def ProfilePage(request):
	#getting the lastest profile object for the user
	person = Profile.objects.filter(person_of=request.user).last()
	food_items = Food.objects.all()#filter(person_of=request.user)
	form = ProfileForm(instance=person)

	if request.method == 'POST':
		form = ProfileForm(request.POST,instance=person)
		if form.is_valid():	
			form.save()
			return redirect('home')
	else:
		form = ProfileForm(instance=person)

	#querying all records for the last seven days 
	some_day_last_week = timezone.now().date() -timedelta(days=7)
	records=Profile.objects.filter(date__gte=some_day_last_week,date__lt=timezone.now().date(),person_of=request.user)

	context = {'form':form,'food_items':food_items,'records':records}
	return render(request, 'profile.html',context)

#signup page
def RegisterPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request,"Account was created for "+ user)
				return redirect('login')

		context = {'form':form}
		return render(request,'register.html',context)

#login page
def LoginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:

		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(request,username=username,password=password)
			if user is not None:
				login(request,user)
				return redirect('home')
			else:
				messages.info(request,'Username or password is incorrect')
		context = {}
		return render(request,'login.html',context)

#logout page
def LogOutPage(request):
	logout(request)
	return redirect('login')
