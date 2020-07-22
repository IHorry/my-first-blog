from django.urls import path
from django.conf import settings 
from django.contrib import admin
from django.conf.urls.static import static 
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/delete/', views.post_remove, name="post_remove"),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('cv/new', views.CV_new, name='CV_new'),
    path('cv/edit', views.CV_edit, name='CV_edit'),
    path('cv/edit/skill/new',views.skills_new, name='skills_new'),
    path('cv/edit/skill/<int:pk>/edit',views.skill_edit, name='skill_edit'),
    path('cv/edit/skill/<int:pk>/delete/', views.skill_remove, name="skill_remove"),
    path('cv/edit/work/new', views.work_new, name='work_new'),
    path('cv/edit/work/<int:pk>/edit', views.work_edit, name='work_edit'),
    path('cv/edit/work/<int:pk>/delete', views.work_remove, name='work_remove'),
    path('cv/edit/qual/new', views.qual_new, name='qual_new'),
    path('cv/edit/qual/<int:pk>/edit', views.qual_edit, name='qual_edit'),
    path('cv/edit/qual/<int:pk>/delete', views.qual_remove, name='qual_remove'),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

