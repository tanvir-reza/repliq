from django.db import models

# Create your models here.

#Chose Device status
STATUS_CHOICES = (
    ('new', 'New'),
    ('checked_out', 'Checked Out'),
    ('returned', 'Returned'),
)

#Chose device type
DEVICE_CHOICES = (
    ('phone', 'Phone'),
    ('tablet', 'Tablet'),
    ('laptop', 'Laptop'),
    ('other', 'Other'),
)

# Create Company models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name
    


# Create User models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

# Create Asset models here.
class Asset(models.Model):
    device_type = models.CharField(max_length=50, choices=DEVICE_CHOICES,null=True,blank=True)
    description = models.TextField(blank=True)
    device_id = models.CharField(max_length=255, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    checked_out_at = models.DateTimeField(null=True,blank=True)
    returned_at = models.DateTimeField(null=True,blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    checkedOutCondition = models.CharField(max_length=255, blank=True)
    returnCondition = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name_plural = 'Assets'
        verbose_name = 'Asset'
    
    def __str__(self):
        return self.device_type



