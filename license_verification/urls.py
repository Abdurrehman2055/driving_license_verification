from django.urls import path
from .views import LicenseVerificationListCreate, LicenseVerificationRetrieveUpdateDestroy, verify_by_cnic

urlpatterns = [
    path('', LicenseVerificationListCreate.as_view(), name='license-verification-list-create'),
    path('<int:pk>/', LicenseVerificationRetrieveUpdateDestroy.as_view(), name='license-verification-detail'),
    path('verify/<str:cnic>/', verify_by_cnic, name='verify-by-cnic'),
]
