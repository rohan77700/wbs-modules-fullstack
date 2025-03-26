from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.db.models.base import Model as Model
from django.views.generic import DetailView, View
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseBadRequest
from app.models import Post
from followers.models import Follower
from .models import Profile

class ProfileDetailView(DetailView):
    http_method_names = ["get"]
    template_name = "profiles/detail.html"
    model = User
    context_object_name = "user"
    slug_field = "username"
    slug_url_kwarg = "username"

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        user = self.get_object()
        context = super().get_context_data(**kwargs)
        context['total_posts'] = Post.objects.filter(author=user).count()
        context['total_followers'] = Follower.objects.filter(following=user).count()
        context['total_following'] = Follower.objects.filter(followed_by=user).count()
        if self.request.user.is_authenticated:
            context['you_follow'] = Follower.objects.filter(following=user, followed_by=self.request.user).exists()
        return context

class ChangeUsername(LoginRequiredMixin, UpdateView):
    template_name = "profiles/change_username.html"
    model = User
    form_class = UserChangeForm
    success_url = '/'

    def get_object(self):
        return self.request.user
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 

class ChangeName(LoginRequiredMixin, UpdateView):
    template_name = 'profiles/change_name.html'
    model = User
    form_class = UserChangeForm
    success_url = '/'
    
    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        user = form.save(commit=False)
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.save()
        return super().form_valid(form)

class ChangePassword(LoginRequiredMixin, PasswordChangeView):
    template_name = "profiles/change_password.html"
    form_class = PasswordChangeForm
    success_url = '/'

class ChangeAvatar(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['image']
    template_name = 'profiles/change_avatar.html'
    success_url = '/'

    def get_object(self):
        return self.request.user.profile

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)   

class FollowView(LoginRequiredMixin, View):
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        data = request.POST.dict()

        if "action" not in data or "username" not in data:
            return HttpResponseBadRequest("Missing data")
        
        try:
            other_user = User.objects.get(username=data['username'])
        except User.DoesNotExist:
            return HttpResponseBadRequest("Missing user")
        
        if data['action'] == "follow":
            follower, created = Follower.objects.get_or_create(
                followed_by = request.user,
                following = other_user
            )
        else:
            try:
                follower = Follower.objects.get(
                    followed_by = request.user,
                    following = other_user
                )
            except Follower.DoesNotExist:
                follower = None

            if follower:
                follower.delete()

        return JsonResponse({
            'success': True,
            'wording': "Unfollow" if data['action'] == "follow" else "Follow"
        })