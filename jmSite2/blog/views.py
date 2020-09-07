from django.shortcuts import render
from createPost.models import createDBPost
from django.http import Http404
from django.views.generic import TemplateView

# Create your views here.
class index(TemplateView):
    template_name = "blog/index.html"

    def get(self, request, *args, **kwargs):
        posts=createDBPost.objects.all()
        return render(request,self.template_name,{'post':posts})


class show(TemplateView):
    template_name = 'blog/show.html'

    def get(self, request, *args, **kwargs):
        tab=[]
        posts=createDBPost.objects.get(pk=self.kwargs["id"])
        tab=str(posts.order)
        tab=tab.split()
        try:
            return render(request,self.template_name,{'post':posts,'tab':tab})
        except:
            raise Http404('Error 404')


class cat(TemplateView):
    template_name = 'blog/cat.html'

    def get(self, request, *args, **kwargs):
        posts=createDBPost.objects.all()
        test=[]
        for post in posts:
            test.append(post.category)
        test=list(set(test))
        return render(request,self.template_name,{'post':test})


class categ(TemplateView):
    template_name = 'blog/showCatArticle.html'

    def get(self, request, *args, **kwargs):
        posts=createDBPost.objects.all()
        listCat=[]
        for post in posts:
            if post.category==self.kwargs["test"]:
                listCat.append(post)
        return render(request,self.template_name,{'post':posts,'test':self.kwargs["test"],'listCat':listCat})
