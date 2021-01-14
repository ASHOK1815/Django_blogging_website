from django.contrib import admin

# Register your models here.
from blog.models import Post1,BlogComment



admin.site.register((Post1,BlogComment))
