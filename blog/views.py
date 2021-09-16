from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic.base import RedirectView
from .models import Post
from django.http import HttpResponse, HttpResponseNotFound
from .forms import createPost
from django.views.generic import (
            ListView,
            DetailView,
            CreateView,
            UpdateView,
            DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User
import sys, logging
# Create your views here.


# posts =[

#     {
#         'author' : 'first author',
#         'title' : 'first title',
#         'content' : 'first Conten',
#         'date_posted':'25/7/2014'
#     },
#     {
#         'author' : 'second author',
#         'title' : 'second title',
#         'content' : 'second Conten',
#         'date_posted':'25/7/2012'
#     }
# ]
def home(request):
    posts = Post.objects.all()
    return render(request,'blog/home.html',context={'posts':posts})

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'   
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'   
    #ordering = ['-date_posted']
    paginate_by = 5
    #print("Goodbye cruel world!", file=sys.stderr)
    logging.basicConfig(filename = 'a.log',level= logging.INFO)
    logging.info('Goodbye cruel worldghfjghjghj!')


    def get_queryset(self):
        logging.info('aaaaaaaaaaaaa!')
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        logging.info('aaaaaaaaaaaaa!')
        logging.info(f'jkljfdgd{user}')

        logging.info(Post.objects.filter(author=user))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post
    #template_name = 'blog/detail.html'

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog-home')
    #template_name = 'blog/detail.html'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']
    # if test_func():
    #     #messages.MessageFailure(Post.request,f'You don"t have permissions to update the post')
    #     redirect('blog-home')

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # def dispatch(self, request, *args, **kwargs):
    #     post = self.get_object()
    #     if not self.test_func():
    #         messages.error(request,'You have no permissions to update the post')
    #         return redirect('blog-home')
    #     return pass# redirect('post-detail',post.id)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            #messages.MessageFailure(self.request,f'You don"t have permissions to update the post')
            #redirect('blog-home')
            #RedirectView = 'blog-home'
            return False


def about(request):
    # response = HttpResponse()
    # response.write('<p> The About paragraph </p>')
    # return response
    return render(request,'blog/about.html')
