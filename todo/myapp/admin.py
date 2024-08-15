from django.contrib import admin
from .models import TODO
# Register your models here.

@admin.register(TODO)
class ToDoAdmin(admin.ModelAdmin):
    list_display=['title','status','user','date','priority']
    list_filter=['user']