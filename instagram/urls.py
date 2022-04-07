from django.urls import path,include
# from django.conf.urls import  url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.homepage,name = 'home'),
    path('search/', views.search, name='search'),
    path('signup/', views.signup, name='signup'),
    path('profile',views.show_profile, name='profile'),
    path('update/<id>', views.update_profile, name='update_profile'),
    path('posts/',views.new_post, name='post'),
    path('comment/<id>', views.comment, name='comment'),
    path('accounts/profile/',views.show_profile, name='profile'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('logout/', views.signout,name='logout'),
]