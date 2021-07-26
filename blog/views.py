from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Post
from django.contrib.auth.models import User
from django.views.generic import (
				ListView, 
				DetailView, 
				CreateView,
				UpdateView,
				DeleteView
			)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class MyPostListView(ListView):
	# model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'

	def get_queryset(self):
		return Post.objects.filter(author = self.request.user.id).order_by('-date_posted')


class UserPostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author = user).order_by('-date_posted')


class PostDetailView(DetailView):
	model = Post

class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'

	def test_func(self):
		return self.request.user == self.get_object().author


class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		return self.request.user == self.get_object().author


def about(request):
	return render(request, 'blog/about.html', {'title':'about'})
	
