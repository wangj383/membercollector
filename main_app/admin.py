from django.contrib import admin
from .models import Member, Task, Photo

# Register your models here.
admin.site.register(Member)
admin.site.register(Task)
admin.site.register(Photo)