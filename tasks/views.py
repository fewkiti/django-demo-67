from django.shortcuts import render
from task.forms import TaskForm
# Create your views here.
tasks = ["foo", "bar", "baz"]

def index(request):
    context = 