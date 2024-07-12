from django.contrib import admin

from .models import user, post, category, comment


class UserAdmin(admin.ModelAdmin):
 list_display = ("username", "email")
admin.site.register(user, UserAdmin)


class CategoryAdmin(admin.ModelAdmin):
 list_display2 = ("name")
admin.site.register(category, CategoryAdmin)


class PostAdmin(admin.ModelAdmin):
 list_display3 = ("title")
admin.site.register(post, PostAdmin)



class CommentAdmin(admin.ModelAdmin):
 list_display4 = ("user_id", "content")
admin.site.register(comment, CommentAdmin)