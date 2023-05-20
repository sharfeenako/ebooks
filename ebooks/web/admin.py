from django.contrib import admin
from .models import Comment,Book,Category,Lang_Category

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'author','timestamp',  'approved')
    list_filter = ('approved',)
    actions = ['approve_comments', 'reject_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

    def reject_comments(self, request, queryset):
        queryset.delete()

admin.site.register(Comment, CommentAdmin)

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Lang_Category)