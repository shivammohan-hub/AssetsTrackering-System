from django.db import models
from manager.models import Asset


class ToAssign(models.Model):

    person_name = models.CharField(max_length=200)

    person_email = models.EmailField()

    DEPARTMENT = [
        ("it", "IT"),
        ("hr", "Human Resources"),
        ("finance", "Finance"),
        ("sales", "Sales"),
        ("marketing", "Marketing"),
        ("administration", "Administration"),
        ("accounts", "Accounts"),
        ("customer_support", "Customer Support"),
    ]

    department = models.CharField(
        max_length=50,
        choices=DEPARTMENT,
        default="it"
    )

    person_designation = models.CharField(max_length=200)

    assignment_date = models.DateField()

    remarks = models.TextField(
        null=True,
        blank=True
    )

    assets = models.ManyToManyField(Asset)

    def __str__(self):
        return self.person_name