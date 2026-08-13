from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True, default="N/A")

    def __str__(self):
        return self.category_name
    

class Asset(models.Model):
    assetId = models.CharField(max_length=50, null=True,blank=True)
    asset_name = models.CharField(max_length=200)
    category = models.ForeignKey("manager.Category", on_delete=models.PROTECT)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=200)
    serial_number = models.CharField(max_length=50)
    purchase_date = models.DateField()
    purchase_price = models.IntegerField()

    CONDITION_CHOICES = [
        ("new", "New"),
        ("good", "Good"),
        ("fair", "Fair"),
        ("damaged", "Damaged")
    ]
    condition = models.CharField(max_length=40, choices=CONDITION_CHOICES, default="new")

    STATUS = [
        ("available", "Available"),
        ("not_available", "Not Available"),
    ]
    status = models.CharField(max_length=50, choices=STATUS, default="available")

    quantity = models.IntegerField(null=True, blank=True, default=1)
    asset_description = models.TextField(null=True, blank=True, default="N/A")
    image = models.ImageField(upload_to="assets_image/", null=True, blank=True,)


    def __str__(self):
        return self.asset_name


