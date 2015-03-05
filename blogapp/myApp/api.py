from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from myApp.models import Post
from myApp.models import Comment


class PostResource(ModelResource):
    class Meta:
        queryset = Post.objects.all()
        resource_name = 'post'
        authorization=Authorization()
        always_return_data = True

class CommentResource(ModelResource):
	post = fields.ForeignKey(PostResource,'post')
    class Meta:
        queryset = Comment.objects.all()
        resource_name = 'comment'
        authorization=Authorization()
        always_return_data = True