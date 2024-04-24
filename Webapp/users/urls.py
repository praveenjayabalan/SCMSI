from django.urls import path
from .views import home, profile, RegisterView,IDCardView

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    # path('studentcard/<id>', IDCardView.as_view(), name='studentcard'),

    path('profile/studentcard/<int:id>', IDCardView.details, name='studentcard'),
]
