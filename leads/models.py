from django.db import models
from django.contrib.auth.models import User
from accounts.models import Account

LEAD_SOURCE = (
    ('call', 'Call'),
    ('email', 'Email'),
    ('existing customer', 'Existing Customer'),
    ('partner', 'Partner'),
    ('public relations', 'Public Relations'),
    ('compaign', 'Campaign'),
    ('other', 'Other'),
)

LEAD_STATUS = (
    ('assigned', 'Assigned'),
    ('in process', 'In Process'),
    ('converted', 'Converted'),
    ('recycled', 'Recycled'),
    ('dead', 'Dead')
)

class Lead(models.Model):
    title = models.CharField("Treatment Pronouns for the customer",
        max_length=64, blank=True, null=True)
    first_name = models.CharField(("First name"), max_length=255)
    last_name = models.CharField(("Last name"), max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=True, blank=True)
    account = models.ForeignKey(Account, related_name='Leads', on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField("Status of Lead", max_length=255,
                              blank=True, null=True, choices=LEAD_STATUS)
    source = models.CharField("Source of Lead", max_length=255,
                              blank=True, null=True, choices=LEAD_SOURCE)
    address = models.CharField("Address", max_length=255, blank=True, null=True)

    website = models.CharField("Website", max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    assigned_to = models.ManyToManyField(User, related_name='lead_assigned_users')    
    account_name = models.CharField(max_length=255, null=True, blank=True)
    opportunity_amount = models.DecimalField("Opportunity Amount", decimal_places=2, max_digits=12,
        blank=True, null=True)
    createdBy = models.ForeignKey(User, related_name='lead_created_by', on_delete=models.CASCADE)
    createdOn = models.DateTimeField("Created on", auto_now_add=True)
    isActive = models.BooleanField(default=False)
    enquery_type = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.first_name + self.last_name
