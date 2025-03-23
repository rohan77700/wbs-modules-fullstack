from django.views.generic import TemplateView, DetailView, FormView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-id')
        return context
    
class PostDetilView(DetailView):
    template_name = 'detail.html'
    model = Post

class AddPostView(FormView):
    template_name = 'post.html'
    form_class = PostForm
    success_url = reverse_lazy('app:index')

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        new_object = Post.objects.create(
            text = form.cleaned_data['text'],
            image = form.cleaned_data['image']
        )
        messages.add_message(self.request, messages.SUCCESS, 'Your post was uploaded successfully!')
        return super().form_valid(form)
    