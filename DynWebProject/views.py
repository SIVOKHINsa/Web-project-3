from django.shortcuts import render, redirect
from . models import articles
from .forms import articlesform
from django.views.generic import DetailView, UpdateView, DeleteView

def news_home(request):
    news = articles.objects.order_by('-date')[:5]
    return render(request, 'main/newshome.html', {'news': news})

class newsdetailview(DetailView):
    model = articles
    template_name = 'main/details_view.html'
    context_object_name = 'article'

class newsupdateview(UpdateView):
    model = articles
    template_name = 'main/update.html'
    form_class = articlesform

class newsdeleteview(DeleteView):
    model = articles
    success_url = '/'
    template_name = 'main/delete.html'



def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contact.html')

def create(request):
    error = ''
    form = articlesform()
    if request.method == 'POST':
        form = articlesform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        else:
            error = 'Форма заполнена не корректно'

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', data)

