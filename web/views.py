from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from . models import Image
from django.db.models import Q


def index(request):
    template_name = "web/index.html"
    images = Image.objects.filter(is_public=True).order_by("-id")

    query = request.GET.get("query")
    if query:
        images = images.filter(
            Q(title__icontains=query) |
            Q(auto_tags__icontains=query) |
            Q(user_tags__icontains=query)
        )
    context = {
        "images": images
    }
    return render(request, template_name, context)


def search(request):
    template_name = "web/search_view.html"
    images = Image.objects.filter(is_public=True).order_by("-id")

    query = request.GET.get("query")
    if query:
        images = images.filter(
            Q(title__icontains=query) |
            Q(auto_tags__icontains=query) |
            Q(user_tags__icontains=query)
        )
    else:
        return redirect("web:index")
    context = {
        "images": images,
        "query": query,
    }
    return render(request, template_name, context)


def image_details(request, id):
    template_name = "web/image_details.html"
    image = get_object_or_404(Image, id=id)
    images = Image.objects.filter(is_public=True).order_by("-id")

    auto_tag = image.auto_tags.split()[0] if image.auto_tags != None else ""
    user_tag = image.user_tags.split()[0] if image.user_tags != None else ""

    related_images = images.filter(
        Q(auto_tags__icontains=auto_tag) |
        Q(user_tags__icontains=user_tag)
    ).exclude(id=image.id)
    context = {
        "image": image,
        "images": related_images
    }
    return render(request, template_name, context)
