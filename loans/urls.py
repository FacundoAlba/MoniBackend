from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .api import LoanViewSet
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('api/loans', LoanViewSet, 'loans')

urlpatterns = [
    path('', views.home, name='home'),
    path('', include(router.urls)),
    path('signup/', views.signup, name='signup'), 
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('user/', views.user_detail, name='user'),
    path('loans/', views.loans, name='loans'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]