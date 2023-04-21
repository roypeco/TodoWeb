from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import Todo
from .forms import Contact_Form


class TodoList(ListView):
    model = Todo
    context_object_name = "tasks"


class TodoDetail(DetailView):
    model = Todo
    context_object_name = "task"
    


class TodoCreate(CreateView):
    # model = Todo
    # fields = "__all__"
    # success_url = reverse_lazy("list")

    def __init__(self):
        self.params = {
                       "form":Contact_Form(),
                       }
    
    def get(self, request):
        return render(request, "todo/todo_form.html",context=self.params)
    
    def post(self, request):
        if request.method == "POST":
            self.params["form"] = Contact_Form(request.POST)
        
            if self.params["form"].is_valid():

                self.params["form"].save(commit=True)

        # return render(request, "todo/todo_form.html",context=self.params)
        return HttpResponseRedirect('/todo')


class TodoUpdate(UpdateView):
    model = Todo
    fields = "__all__"
    success_url = reverse_lazy("list")


class TodoDelete(DeleteView):
    model = Todo
    context_object_name = "task"
    success_url = reverse_lazy("list")
    