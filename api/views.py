from django.views.generic.list import BaseListView
from django.http import JsonResponse

from api.utils import obj_to_post
from blog.models import Post


# Create your views here.
class ApiPostLV(BaseListView):
    model = Post

    def render_to_response(self, context, **response_kwargs):
        qs = context["object_list"]
        postList = [obj_to_post(obj) for obj in qs]
        return JsonResponse(data=postList, safe=False, status=200)
