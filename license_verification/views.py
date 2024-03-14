from rest_framework import generics
from .models import LicenseVerification
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import LicenseVerificationSerializer

class LicenseVerificationListCreate(generics.ListCreateAPIView):
    queryset = LicenseVerification.objects.all()
    serializer_class = LicenseVerificationSerializer

class LicenseVerificationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = LicenseVerification.objects.all()
    serializer_class = LicenseVerificationSerializer


@api_view(['GET'])
def verify_by_cnic(request, cnic):
    try:
        license_verification = LicenseVerification.objects.get(cnic=cnic)
        serializer = LicenseVerificationSerializer(license_verification)
        return Response(serializer.data)
    except LicenseVerification.DoesNotExist:
        return Response({"message": "No record found for this CNIC."}, status=404)

