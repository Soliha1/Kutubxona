from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group, User

class KutubxonachiAdmin(admin.ModelAdmin):

    list_filter = ('ish_vaqti',)
    search_fields = ('ism', )

class MuallifAdmin(admin.ModelAdmin):
    list_display = ('ism','jins','tugilgan_sana','kitob_soni','tirik', )
    search_fields = ('ism', )
    list_filter = ('tirik', )

class RecordAdmin(admin.ModelAdmin):
    list_display=('talaba', 'kitob', 'Admin','olingan_sana','qaytarish_sana',)
    list_editable = ( 'kitob', 'Admin','qaytarish_sana',)



admin.site.register(Talaba)
admin.site.register(Muallif,MuallifAdmin)
admin.site.register(Kitob)
admin.site.register(Kutubxonachi, KutubxonachiAdmin)
admin.site.register(Record,RecordAdmin)

admin.site.unregister(Group)
admin.site.unregister(User)




# Register your models here.
