from django.contrib import admin

from .models import Paragraph, Result

# Register your models here.


class ResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'paragraph')
    list_filter = ['user', 'paragraph']


class ParagraphAdmin(admin.ModelAdmin):
    list_display = ('id', 'count')


admin.site.register(Paragraph, ParagraphAdmin)
admin.site.register(Result, ResultAdmin)
