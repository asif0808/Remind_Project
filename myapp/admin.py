from django.contrib import admin
from myapp.models import Remind
class RemindAdmin(admin.ModelAdmin):
    list_display=['id','date','time','method','message']
admin.site.register(Remind,RemindAdmin)
