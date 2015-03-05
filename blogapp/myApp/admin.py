from django.contrib import admin
from myApp.models import Post,Comment

class AdminPost(admin.ModelAdmin):
	list_display = ('author','title','text','pub_date','upd_date','is_public')
admin.site.register(Post,AdminPost)

class AdminComment(admin.ModelAdmin):
	list_display = ('author','text','pub_date')
admin.site.register(Comment,AdminComment)
