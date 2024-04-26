from django.urls import path
from .views import home, profile,admin, website,RegisterView,IDCardView

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('admin/', admin, name='admin-profile'),
    path('website/', website, name='website'),
    path('profile/studentcard/<int:id>', IDCardView.details, name='studentcard'),
]
