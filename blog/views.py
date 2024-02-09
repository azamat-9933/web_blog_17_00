from django.shortcuts import render

from .models import *


def index(request):
    categories = Category.objects.all()
    articles = Article.objects.all()

    context = {
        "title": "Главная страница",
        "categories": categories,
        "articles": articles
    }

    return render(request, "blog/index.html", context)


def category_page_view(request, category_id):
    # filter() --- брать по условию
    articles = Article.objects.filter(category=category_id)
    trends = Article.objects.all().order_by('views')
    category = Category.objects.get(id=category_id)

    context = {
        "title": f"Катагория: {category.title}",
        "articles": articles,
        "trends": trends
    }

    return render(request, "blog/category_page.html", context)


def about_us_page_view(request):
    context = {
        "title": "О нас"
    }

    return render(request, "blog/about_us.html", context)


def our_team_page_view(request):
    context = {
        "title": "Наша команда"
    }

    return render(request, "blog/team_page.html", context)


def services_page_view(request):
    context = {
        "title": "Наши сервисы"
    }

    return render(request, "blog/services_page.html", context)
