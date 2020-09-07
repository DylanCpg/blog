from django.shortcuts import render
from createPost.models import createDBPost
from .forms import createPost
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView

#création de la page de création de posts
class create(TemplateView):
    template_name='createPost/create.html'

    def get(self, request, *args, **kwargs):
        form=createPost()
        return render(request,self.template_name,{"form":form})

    #récupération du post
    def post(self, request, *args, **kwargs):
        context = {}
        global url
        tab=""
        order=""

        form = createPost(request.POST,request.FILES)

        if form.is_valid():
            #récupération des images et des champs du post
            files=request.FILES.getlist('image')
            filesPost=request.POST.getlist('name')

            #ordonancement des images pour voir si l'ordre à était modifié
            for fp in filesPost:
                order=order+' '+str(fp)


            for f in files:
                tab=tab+' '+str(f)

            order=order.split()
            tab=tab.split()
            int=0

            for i in range((len(tab))):
                print(int)
                int=int+1
                if tab[i]!=order[i]:
                    tab[i]=order[i]


            #réupération des champs de manière claire
            title=form.cleaned_data["title"]
            text=form.cleaned_data["text"]
            category=form.cleaned_data["category"]

            inc=0
            tab=' '.join(tab)

            #mise dans la bd des différentes image la création se fait images par image
            for f in files:
                if inc==0:
                    image=f
                    createDBPost.objects.create(title=title,text=text,category=category,order=tab,image=f)
                    inc=inc+1
                else:
                    title='Stock'
                    createDBPost.objects.create(title=title,image=f)
                    db=createDBPost.objects.filter(title=title).delete()


            return render(request,'createPost/create.html',{"form":form})
