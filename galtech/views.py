from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User



# Create your views here.
def index(request):
    return render(request,'index.html')
def cart(request):
    return render(request,'cart.html')
def student_dashboard(request):
    return render(request, 'dashboard/student-dashboard.html')
def dashboard(request):
    return render(request,'dashboard/student-dashboard.html')
def student_profile(request):
    return render(request,'dashboard/student-profile.html')

def student_settings(request):
    return render(request,'dashboard/student-settings.html')
def student_enrolled_courses(request):
    return render(request,'dashboard/student-enrolled-courses.html')
def login_view(request):
    if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None: 
                login(request, user)
                
                return redirect('index')  
            else:
                messages.error(request, 'Invalid username or password')
    return render(request, 'login_view.html')

def sign_up(request):
    if request.method == "POST":
        if 'register' in request.POST:
            # User fields
            First_Name = request.POST.get("First_Name")
            Last_Name = request.POST.get("Last_Name")
            Email = request.POST.get("Email")
            Password = request.POST.get("Password")
            username = request.POST.get("Email")

            # Creating a new user
            user = User.objects.create_user(first_name=First_Name, last_name=Last_Name, email=Email, password=Password, username=username)

            # Creating a user profile
            phone = request.POST.get("Phone")
            Upload_Profile_Picture = request.FILES.get("Upload Profile Picture")
            query = UsersProfile.objects.create(user=user, phone_number=phone, profile_picture=Upload_Profile_Picture)

    return render(request, 'login_view.html')

def checkout(request):
    return render(request,"checkout.html")

def cart(request):
    return render(request,"cart.html")


def course(request):   
    course = courses.objects.all()
    return render(request,'course.html', {'course': course})

def lesson(request):
    lessons=Lessons.objects.all()
    context = {'lessons': lessons}
    return render(request, 'lesson.html', context)
 

   
def course_details(request, slug):
    course = get_object_or_404(courses, slug=slug)
    if request.method == 'POST' and 'submit' in request.POST:
        current_user = request.user
        rating = request.POST.get("rating")  
        review_text = request.POST.get("comment")  
        Reviews.objects.create(user=current_user,course=course,rating=rating,review_text=review_text)
       
    
    for less in course.lessons_set.all():
        print(less.lesson_title)
        for video in less.video_set.all():
            print(video.video_title)
    return render(request, 'course-details.html', {'course': course})


