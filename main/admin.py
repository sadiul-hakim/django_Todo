from django.contrib import admin
from .models import Todo

# Register your models here.


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'priority', 'completed', 'created',)
    list_filter = ('completed', 'priority', 'created', 'user',)
    search_fields = ('title', 'description', 'user__username', 'user__email',)
    list_editable = ('completed', 'priority',)
    ordering = ('-created',)
    list_per_page = 20
    list_display_links = ('id', 'title')
