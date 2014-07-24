from django.contrib import admin

# Register your models here.
from user.models import User,Clock

class ChoiceInline(admin.TabularInline):
    model = Clock
    extra = 3

class PunchAdmin(admin.ModelAdmin):
    fieldsets=[
            (None, {'fields':['name']}),
            ('Date information', {'fields':['regi_date'],'classes':['collapse']}),
            ]
    inlines = [ChoiceInline]
    list_display = ('name','regi_date','was_clocked_recently')
    list_filter = ['regi_date']
    search_fields = ['name']
admin.site.register(User)

