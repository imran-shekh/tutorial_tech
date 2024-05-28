from django.contrib import admin

# Register your models here.
from .models import *


class Tag_info(admin.TabularInline):
    model = tag


class learning_info(admin.TabularInline):
    model = learning


class prereq_info(admin.TabularInline):
    model = prereq


class videos_info(admin.TabularInline):
    model = Videos


class course_info(admin.ModelAdmin):
    inlines = [Tag_info, learning_info, prereq_info, videos_info]

admin.site.register(Signup)
admin.site.register(Course_details,course_info)
admin.site.register(Videos)
admin.site.register(User_Course)
admin.site.register(Payment)
admin.site.register(Ref_Code)