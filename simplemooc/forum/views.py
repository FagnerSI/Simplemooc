# import json

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (TemplateView, View, ListView, DetailView)
from django.contrib import messages
from django.http import HttpResponse

from .models import Thread, Reply
from .forms import ReplyForm
# Create your views here.

# class ForumView(TemplateView):

# 	template_name = 'forum/index.html'

# index = ForumView.as_view()

# index = TemplateView.as_view(template_name = 'forum/index.html')

class ForumView(ListView):

	paginate_by = 5
	template_name = 'forum/index.html'

	def get_queryset(self):
		queryset = Thread.objects.all()
		order = self.request.GET.get('order','')

		if order == 'views':
			queryset = queryset.order_by('-views')

		elif order == 'answers':
			queryset = queryset.order_by('-answers')

		tag = self.kwargs.get('tag','')

		if 'tag':
			queryset = queryset.filter(tags__slug__icontains=tag)

		return queryset

	def get_context_data(self, **kwargs):
		context = super(ForumView, self).get_context_data(**kwargs)
		context['tags'] = Thread.tags.all()
		return context

class ThreadView(DetailView):

	model = Thread
	template_name = 'forum/thread.html'

	def get(self, request, *args, **kwargs):
		response = super(ThreadView, self).get(request, *args, **kwargs)
		if not self.request.user.is_authenticated() or self.object.author != self.request.user:
			self.object.views = self.object.views + 1
			self.object.save()
		return response


	def get_context_data(self, **kwargs):
		context = super(ThreadView, self).get_context_data(**kwargs)
		context['tags'] = Thread.tags.all()
		context['form'] = ReplyForm(self.request.POST or None)
		return context

	def post(self, request, *args, **kwargs):
		
		if not self.request.user.is_authenticated():
			messages.error(self.request,'Para responder ao tópico é necessário estar logado')
			return redirect(self.request.path)

		self.object = self.get_object()
		context = self.get_context_data(object=self.object)
		form = context['form']

		if form.is_valid():
			reply = form.save(commit=False)
			reply.thread = self.object
			reply.author = request.user
			reply.save()
			messages.success(self.request, 'A sua responsta foi enviada com sucesso')
			
			context['form'] = ReplyForm()
		
		return self.render_to_response(context)


class ReplyCorrectView(View):
		
		correct = True

		def get(self, request, pk):
			reply = get_object_or_404(Reply, pk=pk)
			reply.correct = self.correct
			reply.save()
			messages.success(request, 'Resposta Atualizada com Sucesso')
			return redirect(reply.thread.get_absolute_url())



index = ForumView.as_view()
thread = ThreadView.as_view()
reply_correct = ReplyCorrectView.as_view()
reply_incorrect = ReplyCorrectView.as_view(correct=False)





