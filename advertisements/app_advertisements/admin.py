from django.contrib import admin
from .models import Advertisement
from django.db.models.query import QuerySet

class AdvertisementsAdmin(admin.ModelAdmin):
    list_display = ['id','title','descriptional','price','auction','created_at','created_date','updated_date']
    list_filter = ['auction','created_at','price']
    actions = ['make_action_as_false','make_action_as_true']
    fieldsets = [
        (
            'Общие',
            {
                "fields": ['title','descriptional'],
                "classes": ["collapse"]
            },
        ),
        (
            'Финансы',
            {
                "fields": ['price','auction'],
                "classes": ["collapse"]
            },
            
        ),
    ]


    @admin.action(description='Убрать возможность торга')
    def make_action_as_false(self, request, queryset):
       queryset.update(auction = False)

    @admin.action(description='Добавить возможность торга')
    def make_action_as_true(self, request, queryset):
       queryset.update(auction = True)

admin.site.register(Advertisement, AdvertisementsAdmin)
