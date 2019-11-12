from django.contrib import admin
from .models import Request, Services
from django.utils.html import format_html
from django.shortcuts import reverse


admin.site.register(Services)

def RequestPDF(obj):
    return format_html('<a href="{}">PDF</a>'.format(reverse('AdminRequestPDF', args=[obj.id])))
RequestPDF.short_description = 'В PDF'

class RequestAdmin(admin.ModelAdmin):
    list_display = ['author', 'car', 'service', 'date_end', 'status' , RequestPDF]
admin.site.register(Request, RequestAdmin)