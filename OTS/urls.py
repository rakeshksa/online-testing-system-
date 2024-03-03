from django.urls import path
from OTS.views import *
app_name='OTS'

urlpatterns = [
    path('',welcome),
    path('new-candidate',candidateRegistrationFrom,name='registrationForm'),
    path('store-candidate',candidateRegistration,name='storeCandidate'),
    path('login',loginView,name='login'),
    path('home',candidateHome,name='home'),
    path('test-paper',testPaper,name='testpaper'),
    path('calculate-result',calculateTestResult,name='calculateTest'),
    path('test-history',testResultHistory,name='testhistory'),
    path('result',showTestResult,name='result'),
    path('loguot',logoutView,name='logout'),
]