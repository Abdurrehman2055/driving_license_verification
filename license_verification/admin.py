from django.contrib import admin
from .models import LicenseVerification

class LicenseVerificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'cnic', 'father_or_husband_name', 'gender', 'date_of_birth', 'issue_date', 'license_number')
    search_fields = ('name', 'cnic', 'license_number')

admin.site.register(LicenseVerification, LicenseVerificationAdmin)
