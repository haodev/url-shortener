from django.contrib import admin
from .models import ShortUrl

# Register your models here.
@admin.register(ShortUrl)
class ShortUrlAdmin(admin.ModelAdmin):
    list_display = ('original_url', 'short_url', 'click_count', 'created_at')