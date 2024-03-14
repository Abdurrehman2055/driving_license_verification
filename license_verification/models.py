from django.db import models

class LicenseVerification(models.Model):
    cnic = models.CharField(max_length=15, unique=True)
    father_or_husband_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    blood_group = models.CharField(max_length=5)
    issue_date = models.DateField()
    license_number = models.CharField(max_length=50)
    license_type = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='license_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
