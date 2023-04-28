from django.urls import path, include

from core.views import *

urlpatterns = [
    path('', LoginUser.as_view(), name='login'),
    path('create/', CreateTableView.as_view(), name='main'),
    path('logout/', LogoutUser, name='logout'),
]
