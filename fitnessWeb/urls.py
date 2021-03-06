"""fitnessWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from workouts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.LogOut, name='logout'),
    path('member/', views.member, name='member'),
    path('program/', views.program, name='program'),
    path('AboutUs/', views.AboutUs, name='AboutUs'),
    path('workout_form/', views.CreateWorkOut, name='workout_form'),
    path('update_workout/<int:id>/', views.UpdateWorkout, name='update-workout'),
    path('', views.index, name='index'),
    path('bodybuilding', views.BodyBuilding, name='bodybuilding'),
    path('aerobics', views.Aerobics, name='aerobics'),
    path('exercise/<int:exercise_id>/', views.exercise_detail, name="exercise_detail"),
    path('tinymce/', include('tinymce.urls')),
    path('blog/', include('blog.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

