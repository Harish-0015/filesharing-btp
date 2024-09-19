from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('reer/', views.RegisterView.as_view(), name='auth_register'),
    path('user/<str:unique_id>/', views.GetUserDetailsView.as_view(), name='user-details-by-uniqueid'),

    path('test/', views.testEndPoint, name='test'),
    path('', views.getRoutes),
]
