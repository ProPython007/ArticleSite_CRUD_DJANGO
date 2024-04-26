from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import Http404
from django.db.models import Q

# import random
from.forms import ArticleForm
from .models import Article


def home_view(request):
    article_objs = Article.objects.all()

    return render(request, 'home.html', context={'articles': article_objs})


def article_view(request, slug):
    try:
        article_obj = Article.objects.get(slug=slug)
    except Article.DoesNotExist:
        raise Http404

    return render(request, 'detail.html', context={'article': article_obj})


def search_view(request):
    query = request.GET.get('q')
    if query:
        lookups = Q(title__icontains=query) | Q(content__icontains=query)
        articles = Article.objects.filter(lookups)
        context = {'searched_articles': articles}

        return render(request, 'search.html', context=context)
    else:
        return redirect('/articles')


def posts_by_user(request, author):
    try:
        User = get_user_model()
        user_instance = get_object_or_404(User, username=author)
        articles = Article.objects.filter(user=user_instance)
    except Article.DoesNotExist:
        raise Http404

    return render(request, 'posts_by_user.html', context={'searched_articles': articles, 'author': author})
    

@login_required
def create_view(request):
    article = None
    form = ArticleForm() #request.POST or None
    context = {'form': form}
    
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.instance.user = request.user
            article = form.save() #only works on model form!
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # article = Article.objects.create(title=title, content=content)

    context['obj'] = article

    return render(request, 'create.html', context=context)


@login_required
def update_view(request, id):
    obj = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None, instance=obj)

    context = {}
    if request.user == obj.user:
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('article_detail', form.instance.slug)
        
    context["form"] = form

    return render(request, 'update.html', context=context)


@login_required
def del_view(request, id):
    try:
        id = int(id)
        article_to_del = Article.objects.get(id=id)
    except:
        pass
    
    if request.user == article_to_del.user:
        article_to_del.delete()

    return redirect('base')