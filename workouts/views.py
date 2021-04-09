from django.shortcuts import render, redirect, get_object_or_404
from .models import Exercise, Member, Workout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import WorkOutForm, MemberForm

# View for all pages. 

# Home page function
def index(request):
    return render(request, 'index.html')
 
# Function for Body Building page
def BodyBuilding(request):
    BDProgrammes = Exercise.objects.filter(category__category="Body Building")
    context = {
        'BDProgrammes' : BDProgrammes
    }
    return render(request, 'bodybuilding.html', context)

# Function for Aerobics page
def Aerobics(request):
    AerobicsProgrammes = Exercise.objects.filter(category__category="Aerobics")
    context = {
        'AerobicsProgrammes' : AerobicsProgrammes
    }
    return render(request, 'aerobics.html', context)

# Function for exercise details page
def exercise_detail(request, exercise_id):
    exercise = get_object_or_404(Exercise, id=exercise_id)
    context = {
        'exercise' :exercise
    }
    return render(request, 'exercise_detail.html', context)

# Function for user registration
def registerPage(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Member.objects.create(user=user)
            return redirect('login')

    context = {
        'form' :form
    }
    return render(request, 'register.html', context)

# Login page function
def loginPage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')

    return render(request, 'login.html') 

# Function to logout a user
def LogOut(request):
    logout(request)
    return redirect('login')

# Function for member to build their profile
def member(request):
    member = Member.objects.get(user=request.user)
    workouts = member.workout_set.all()
    total_workouts = workouts.count()
    in_progress = workouts.filter(status="In progress").count()
    finished = workouts.filter(status="FInished").count()
    form = MemberForm(instance=member)
    if request.method == 'POST':
        form = MemberForm(request.POST,  request.FILES, instance=member)
        if form.is_valid():
            form.save()
    context = {
        'member' :member,
        'workouts' :workouts,
        'total_workouts':total_workouts,
        "in_progress":in_progress,
        'finished':finished,
        'form':form
    }
    return render(request, 'member.html', context)

def CreateWorkOut(request):
    member = Member.objects.get(user=request.user)
    form = WorkOutForm(request.user)
    if request.method == 'POST':
        form = WorkOutForm(request.user, request.POST)

        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('/')
         
    context = {
        'form':form
    }
    return render(request, 'workout_form.html', context)

def UpdateWorkout(request, id):
    workout = Workout.objects.get(id=id)
    form = WorkOutForm(request.user, instance=workout)

    if request.method == 'POST':
        form = WorkOutForm(request.user, request.POST, instance=workout)

        if form.is_valid():
            form.instance.workout = workout
            form.save()
            return redirect('/')
    
    context = {
        'form':form
    }
    return render(request, 'workout_form.html', context)

def program(request):
    return render(request, 'program.html')

def AboutUs(request):
    return render(request, 'about-us.html')