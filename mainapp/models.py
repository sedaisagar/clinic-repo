from django.db import models
from django.urls import reverse_lazy

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
    review_title =  models.CharField(max_length=50)
    review = models.CharField(max_length=250)

    class Meta:
        db_table = "testimonials"
    

    # @property
    # def get_edit_url(self):
    #     return reverse_lazy("admin-testimonials-update-page", self.pk)    
    
    # @property
    # def get_delete_url(self):
    #     return reverse_lazy("admin-testimonials-delete-page", self.pk)

class TrustedPartners(CommonModel):
    name =  models.CharField(max_length=50)
    image = models.ImageField(upload_to="services/images")
  
    class Meta:
        db_table = "trusted_partners"
    


class Departments(CommonModel):
    image = models.ImageField(upload_to="departments/images")
    name =  models.CharField(max_length=50)
    short_info = models.CharField(max_length=150)
    description = models.TextField()

    extra_info = models.JSONField(default=dict)

    """
    {
        "schedules": [
            {
                "days": "Mon - Fri",
                "hours" : "9:00 - 17:00",
            }
        ], 
        "features" : [
            "International Drug Database",
            "Stretchers and Stretcher Accessories"
        ],
        "helpline_number":"+23-4565-65768",
    }
    """

    class Meta:
        db_table = "departments"
    
    def __str__(self):
        return self.name
        
class Doctors(CommonModel):
    image = models.ImageField(upload_to="doctors/images")
    name =  models.CharField(max_length=50)
    
    department = models.ForeignKey(Departments, on_delete=models.CASCADE, related_name="doctors")

    doctors_intro = models.TextField()

    facebook_link = models.URLField(max_length=1000)
    twitter_link = models.URLField(max_length=1000)
    skype_link = models.URLField(max_length=1000)
    linkedin_link = models.URLField(max_length=1000)
    pinterest_link = models.URLField(max_length=1000)

    class Meta:
        db_table = "doctors"
    
    def __str__(self):
        return self.name

class BlogCategories(CommonModel):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "blog_categories"

    def __str__(self):
        return self.name
            
class BlogTags(CommonModel):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "blog_tags"
        
    def __str__(self):
        return self.name

class Blogs(CommonModel):
    category = models.ForeignKey(BlogCategories, on_delete=models.CASCADE, related_name="blogs")
    tags = models.ManyToManyField(BlogTags, blank=True, related_name="blogs")

    image = models.ImageField(upload_to="doctors/images")
    title =  models.CharField(max_length=255)
    short_description =  models.CharField(max_length=500)
    

    description = models.TextField()


    class Meta:
        db_table = "blogs"
    



# Appointments

class Appointments(CommonModel):
    department = models.ForeignKey(Departments, on_delete=models.CASCADE, related_name="appointments")
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE, related_name="appointments")

    # Who booked appointment ? 
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="appointments", null=True, blank=True)

    appointment_date = models.DateField()
    appointment_time = models.TimeField()

    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=25)

    message = models.TextField()


    class Meta:
        db_table = "appointments"

        
class Contacts(CommonModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    phone = models.CharField(max_length=25)

    message = models.TextField()

    class Meta:
        db_table = "public_contacts"