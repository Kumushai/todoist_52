from django.contrib import admin


from webapp.models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'status', 'created_at']
    list_display_links = ['id', 'content']
    list_filter = ['created_at']
    search_fields = ['content', 'status']
    fields = ['content', 'status', 'details', 'created_at']


admin.site.register(Todo, TodoAdmin)