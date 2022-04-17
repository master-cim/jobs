from django.contrib import admin
from .models import Posting, Client, Message


class PostingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'start', 'duration', 'text', 'client_filter', 'finish')
    search_fields = ('start', 'end',)
    list_filter = ('client_filter',)
    empty_value_display = '-пусто-'


class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'phone', 'mobile_code', 'tag', 'timezone',)
    search_fields = ('phone',)
    list_filter = ('mobile_code', 'tag',)
    empty_value_display = '-пусто-'


class MessageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'pub_date', 'sending_status',
                    'posting', 'client',)
    list_editable = ('posting', 'client',)
    search_fields = ('pub_date',)
    list_filter = ('pub_date', 'sending_status',)
    
    empty_value_display = '-пусто-'


admin.site.register(Posting, PostingAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Message, MessageAdmin)

