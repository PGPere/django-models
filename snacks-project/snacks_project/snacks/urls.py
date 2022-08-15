from django.urls import path
from .views import HomePageView, AboutView, SnacksList
from .views import SnacksDetail

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path(' ', SnacksList.as_view(), name="snacks_list"),
    path('<int:pk>', SnacksDetail.as_view(), name="snacks_detail")
]
