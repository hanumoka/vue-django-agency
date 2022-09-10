from django.views import View
from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView
from django.http import JsonResponse

from api.utils import obj_to_post, prev_next_post
from blog.models import Post, Category, Tag


# BaseListView, BaseDetailView는 모델이 한개일때 사용하는 뷰이다.

# Create your views here.
class ApiPostLV(BaseListView):
    # model = Post

    # get_queryset 메소드의 결과값이 context["object_list"] 에 전달된다. 해당 메소드를 정의하면 위 model = Post 선언이 불필요해진다.
    def get_queryset(self):
        paramCate = self.request.GET.get('category')
        paramTag = self.request.GET.get('tag')
        if paramCate:
            qs = Post.objects.filter(category__name__iexact=paramCate)
        elif paramTag:
            qs = Post.objects.filter(tags__name__iexact=paramTag)
        else:
            qs = Post.objects.all()
        return qs

    def render_to_response(self, context, **response_kwargs):
        qs = context["object_list"]
        postList = [obj_to_post(obj, False) for obj in qs]
        return JsonResponse(data=postList, safe=False, status=200)


class ApiPostDV(BaseDetailView):
    model = Post

    def render_to_response(self, context, **response_kwargs):
        obj = context["object"]
        post = obj_to_post(obj)
        prevPost, nextPost = prev_next_post(obj)

        jsonData = {
            'post': post,
            'prevPost': prevPost,
            'nextPost': nextPost,
        }

        return JsonResponse(data=jsonData, safe=True, status=200)


# 두개 모델 사용 뷰
class ApiCateTagView(View):
    def get(self, request, *args, **kwargs):
        qs1 = Category.objects.all()
        qs2 = Tag.objects.all()
        cateList = [cate.name for cate in qs1]
        tagList = [tag.name for tag in qs2]

        jsonData = {
            "cateList": cateList,
            "tagList": tagList
        }

        return JsonResponse(data=jsonData, safe=True, status=200)
