from django.db import models

# Create your models here.
class UrlShortener(models.Model):
    short_url = models.CharField(max_length=255, unique=True)
    short_id = models.CharField(max_length=8, unique=True)
    long_url = models.URLField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # updated_at = models.DateTimeField(auto_now=True)
    # def __str__(self):
    #     return self.short_url

# class Click(models.Model):
#     url = models.ForeignKey(UrlShortener, on_delete=models.CASCADE)
#     ip_address = models.GenericIPAddressField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return f"{self.ip_address} clicked {self.url}"
