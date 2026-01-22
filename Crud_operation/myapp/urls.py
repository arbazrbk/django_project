from django.urls import path
from myapp import views

urlpatterns = [
    path('create/', views.StudentcreateView.as_view(), name='student_create'),
    path('list/', views.StudentListView.as_view(), name='student_list'),
    path('detail/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('update/<int:pk>/', views.StudentUpdateView.as_view(), name='student_update'),
    path('delete/<int:pk>/', views.StudentDeleteView.as_view(), name='student_delete'),
]