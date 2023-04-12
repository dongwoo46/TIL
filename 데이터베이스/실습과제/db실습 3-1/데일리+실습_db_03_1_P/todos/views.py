from django.shortcuts import render, redirect
from models import Todo
from django.views.decorators.http import require_http_methods
from .forms import TodoForm

def index(request):
	if not request.user.is_authenticated:
		return redirect('accounts.login')

	todos = Todo.objects.all()
	context = {'todos':todos,}
	return render(request, 'todos/index.html', context)

@require_http_methods(['GET','POST'])
def create(request):
	if not request.user.is_authenticated:
		return redirect('accounts.login')
	
	if request.method == 'POST':
		form = TodoForm(request.POST)
		if form.is_valid():
			todo = form.save(commit=False)
			todo.author = request.user
			todo.save()
			return redirect('toods:index')
	else:
		form = TodoForm()
	context = {'form':form}
	return render(request, 'toods/create.html', context)    