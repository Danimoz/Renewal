from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
import datetime

class Trademark(models.Model):
    trademarkName = models.CharField(max_length=100)
    trademarkClass = models.CharField(max_length=100)
    dateCreated = models.DateTimeField(default=timezone.now)
    acknowledgeDoc = models.FileField(upload_to='acknowledge_docs', null=True, blank=True)
    acceptanceDoc = models.FileField(upload_to='acceptance_docs/', null=True, blank=True)
    cert = models.FileField(upload_to='trademark_cert/', null=True, blank=True)
    renewalDoc = models.FileField(upload_to='renewalDocs', null=True, blank=True)
    dateRenewed = models.DateTimeField(default=timezone.now)
    uploadedBy = models.ForeignKey(User, on_delete=models.RESTRICT)
    
    @property
    def shelfLife(self):
        return self.dateRenewed + datetime.timedelta(days = 365*5)
        
    def __str__(self):
        return self.trademarkName

class Container(models.Model):
    productName = models.CharField(max_length=100)
    containerNo = models.CharField(max_length=100)
    agentName = models.CharField(max_length=100)
    receiptDoc = models.FileField(upload_to='receipts', null=True, blank=True)
    endorsementDoc = models.FileField(upload_to='endorsements', null=True, blank=True)
    dateCreated = models.DateTimeField(default=timezone.now)
    dateRenewed = models.DateTimeField(default=timezone.now)
    expiryDate = models.DateTimeField(default=timezone.now)
    uploadedBy = models.ForeignKey(User, on_delete=models.RESTRICT)


    def __str__(self):
        return self.productName