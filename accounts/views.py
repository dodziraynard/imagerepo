from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.contrib.auth.models import User
from . forms import UserForm
from web.models import Image
from web.forms import ImageForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.html import strip_tags
from web . utils import get_image_tags


@login_required(login_url="accounts:login")
def my_images(request):
    template_name = "accounts/user_images.html"
    images = Image.objects.filter(user=request.user).order_by("-id")

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


@login_required(login_url="accounts:login")
def operate_images(request):
    image_ids = request.POST.getlist("selected_images")
    operation = request.POST.get("operation")

    images = Image.objects.filter(id__in=image_ids)
    if operation == "private":
        images.update(is_public=False)
    elif operation == "public":
        images.update(is_public=True)
    elif operation == "delete":
        images.delete()
    return redirect("accounts:my_images")


class UploadImage(View):
    template_name = 'accounts/upload_images.html'
    form = ImageForm

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        is_public = True if request.POST.get("is_public") == "on" else False
        auto_tag = True if request.POST.get("auto_tag") == "on" else False

        for file in request.FILES.getlist("files"):
            form = self.form(request.POST)
            if form.is_valid:
                image = form.save(commit=False)
                image.user = request.user
                image.is_public = is_public
                image.file = file
                image.save()

                # Generating image tags
                if auto_tag:
                    response = get_image_tags(image.file.url)
                    try:
                        if response.status_code == 200:
                            if response.json().get("status").get("type") == "success":
                                tags = response.json().get("result").get("tags")
                                string_tags = ""
                                for tag in tags:
                                    if float(tag.get("confidence")) > 40:
                                        string_tags += f'{tag.get("tag").get("en")} '
                                image.auto_tags = string_tags
                                image.save()
                    except Exception:
                        pass

            else:
                for field, er in form.errors.items():
                    error_message = f"{field.title()}: {strip_tags(er)}"
                    request.session.error_message = error_message
                    return render(request, self.template_name)
        return redirect("accounts:my_images")


class UserLogin(View):
    template_name = 'accounts/login.html'

    def get(self, request):
        redirect_url = request.GET.get("next", "")
        context = {
            "next": redirect_url
        }
        return render(request, self.template_name, context)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user and user.is_active:
            login(request, user,
                  backend='django.contrib.auth.backends.ModelBackend')
            redirect_url = request.GET.get("next") or "accounts:my_images"
            return redirect(redirect_url)
        context = {
            'error_message': 'Wrong password or username, please check and try again.'
        }
        return render(request, self.template_name, context)


class UserRegistration(View):
    template_name = 'accounts/register.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            form = UserForm({"username": username})
            if form.is_valid():
                user = form.save(commit=False)
                user.set_password(password)
                user.save()
                login(request, user,
                      backend='django.contrib.auth.backends.ModelBackend')
                return redirect("web:index")
            request.session.error_message = "Please check your username. You may consider changing it."
        else:
            request.session.error_message = "Passwords did not match."
        return render(request, self.template_name)


def logout_user(request):
    logout(request)
    return redirect('web:index')
