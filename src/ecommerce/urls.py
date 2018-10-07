"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from foods.views import FoodListView,food_list_view,FoodDetailView,food_detail_view

urlpatterns = [
    url(r'^$', home_page),
    url(r'^login/$', login_page),
    url(r'^register_food/$', register_food_page),
    url(r'^foods/$', FoodListView.as_view()),
    url(r'^foods_fv/$', food_list_view),
    url(r'^foods/(?P<pk>\d+)/$', FoodDetailView.as_view()),
    url(r'^foods_fv/(?P<pk>\d+)/$', food_detail_view),
    url(r'^register/$', register_page),
    url(r'^admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL,
                                      document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL,
                                      document_root=settings.MEDIA_ROOT)
