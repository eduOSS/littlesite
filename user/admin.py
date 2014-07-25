from django.contrib import admin

# Register your models here.
from user.models import User,Clock

class ClockInline(admin.TabularInline):
    model = Clock
    extra = 3

class UserAdmin(admin.ModelAdmin):
    fieldsets=[
            (None, {'fields':['name']}),
            ('Register information', {'fields':['regi_date'],'classes':['collapse']}),
            ('Log times', {'fields':['log_num'],'classes':['collapse']}),
            ('Coins', {'fields':['coins'],'classes':['collapse']}),

            ]
    inlines = [ClockInline]
    list_display = ('name','regi_date','log_num','coins')
    list_filter = ['regi_date']
    search_fields = ['name']
admin.site.register(User,UserAdmin)

