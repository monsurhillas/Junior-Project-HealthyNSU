from django.shortcuts import render,get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import (ListView,
                                DetailView,
                                CreateView,
                                UpdateView,
                                DeleteView)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


@login_required
def home(request):
    context ={
    'posts' : Post.objects.all()
    }
    return render(request, 'healthsuggest/healthsuggest.html',context)

#For healthsuggest Section
class PostListViewS(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'healthsuggest/healthsuggest.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3


class UserPostListViewS(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'healthsuggest/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User,username = self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-date_posted')





class PostDetailViewS(LoginRequiredMixin, DetailView):
    model = Post

class PostCreateViewS(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateViewS(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteViewS(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/healthsuggest/suggest'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

#-----------------------------------------------------
#-----------------------------------------------------


#for HealthAsk section
class PostDetailViewA(DetailView):
    model = Post


@login_required
def healthask(request):
    context={
    'posts' : Post.objects.all()
    }
    return render(request,'healthsuggest/healthask.html',context)

class PostListViewA(ListView):
    model = Post
    template_name = 'healthsuggest/healthask.html'
    context_object_name = 'posts'
    ordering =['-date_posted']
    paginate_by = 4

class PostCreateViewA(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateViewA(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteViewA(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/healthsuggest/ask'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
#---------------------------------------------------------
# Create your views here.
