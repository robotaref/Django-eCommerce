
from django.conf.urls import url
from .views import *

urlpatterns = [

    url(r'^$', FoodListView.as_view(), name='list'),
    url(r'(?P<slug>[-\w]+)/$', FoodDetailSlugView.as_view(), name='detail'),

]
