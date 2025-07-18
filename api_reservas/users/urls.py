from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from users import views

urlpatterns = [
    path('users/', views.UsersList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)