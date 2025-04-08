from django.urls import path
from . import views

#define a list of URL patterns
urlpatterns = [
    path('', views.index, name='index'),
   
]
# urlpatterns is a list of URL patterns that Django will use to match incoming requests to the appropriate view function.
# Each URL pattern is defined using the path() function, which takes three arguments:
# 1. The URL pattern (a string) that you want to match.
# 2. The view function that should be called when the URL pattern is matched.
# 3. An optional name for the URL pattern, which can be used to refer to this URL pattern in other parts of your code.
# In this case, the urlpatterns list contains four URL patterns: