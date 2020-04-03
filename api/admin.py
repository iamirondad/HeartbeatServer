from django.contrib import admin

# Register your models here.
from .models import Profile
from .models import Promise
from .models import Progress

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['realname', 'nickname', 'about']

class PromiseAdmin(admin.ModelAdmin):
    list_display = ['start_date', 'duration', 'target_heartbeats']

class ProgressAdmin(admin.ModelAdmin):
    list_display = ['current_heartbeats']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Promise, PromiseAdmin)
admin.site.register(Progress, ProgressAdmin)
