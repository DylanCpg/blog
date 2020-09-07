from django.shortcuts import render
from createPost.models import createDBPost
from django.views.generic import TemplateView

#donne les derniers Post dans la page d'accueil
class home(TemplateView):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        posts=createDBPost.objects.all()
        if len(posts)>=4:
            derniersPost=[posts[len(posts)-1]]
            derniersPost=derniersPost+[posts[len(posts)-2]]
            derniersPost=derniersPost+[posts[len(posts)-3]]
            derniersPost=derniersPost+[posts[len(posts)-4]]
        elif len(posts)>=3:
            derniersPost=[posts[len(posts)-1]]
            derniersPost=derniersPost+[posts[len(posts)-2]]
            derniersPost=derniersPost+[posts[len(posts)-3]]
        elif len(posts)>=2:
            derniersPost=[posts[len(posts)-1]]
            derniersPost=derniersPost+[posts[len(posts)-2]]
        elif len(posts)>=1:
            derniersPost=[posts[len(posts)-1]]
        else:
            derniersPost=posts
        return render(request,self.template_name,{"post":derniersPost})
