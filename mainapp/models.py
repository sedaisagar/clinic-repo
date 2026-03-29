from django.db import models

from mainapp.utils import CommonModel

# Create your models here.
class Banner(CommonModel):
    info = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=250)

    banner_image = models.ImageField(upload_to="banner-image")


    class Meta:
        db_table = "banner"

class Services(CommonModel):
    icon = models.ImageField(upload_to="services/icons")
    image = models.ImageField(upload_to="services/images")
    title =  models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    class Meta:
        db_table = "services"


class Testimonials(CommonModel):
    image = models.ImageField(upload_to="services/images")
    name =  models.CharField(max_length=50)
    position =  models.CharField(max_length=50)
    review = models.CharField(max_length=250)

    class Meta:
        db_table = "testimonials"
    

class TrustedPartners(CommonModel):
    name =  models.CharField(max_length=50)
    image = models.ImageField(upload_to="services/images")
  
    class Meta:
        db_table = "trusted_partners"
    

