from django.shortcuts import render, redirect
from django.views.generic.edit import DeleteView
from .models import Widget
from .forms import WidgetForm
# Create your views here.

class WidgetDelete(DeleteView):
    model= Widget
    success_url = ''

def index(request):
    widgets = Widget.objects.all()
    widget_form = WidgetForm()
    return render(request, 'index.html', {
        'widgets': widgets,
        'widget_form': widget_form
    })

def add_widget(request):
    form = WidgetForm(request.POST)
    if form.is_valid():
        new_widget = form.save(commit=False)
        new_widget.save()
    return redirect('index')

def delete_widget(request, widget_id):
    widget = Widget.objects.get(id=widget_id)
    widget.delete()

    return redirect('index')