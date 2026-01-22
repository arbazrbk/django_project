from django.shortcuts import render
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from myapp.models import Student


class StudentcreateView(CreateView):
    model = Student
    fields = '__all__'
    template_name = 'myapp/form.html'
    success_url = reverse_lazy('student_list')


class StudentListView(ListView):
    model = Student
    template_name = 'myapp/student_list.html'
    context_object_name = 'students'


class StudentDetailView(DetailView):
    model = Student
    template_name = 'myapp/student_detail.html'
    context_object_name = 'student'


class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'myapp/form.html'
    context_object_name = 'student'
    fields = '__all__'
    success_url = reverse_lazy('student_list')


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'myapp/student_confirm_delete.html'
    context_object_name = 'student'
    success_url = reverse_lazy('student_list')
