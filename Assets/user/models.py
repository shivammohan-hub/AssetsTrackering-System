from django.db import models
from django.conf import settings
from manager.models import Asset

class ToAssign(models.Model):
    assignee_name = models.CharField(max_length=255, default="N/A")
    employee_id = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    assignment_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    remarks = models.TextField(blank=True, null=True)
    
    
    assets = models.ManyToManyField(Asset)
    
    assigned_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"Assigned to {self.assignee_name} on {self.assignment_date}"