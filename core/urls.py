from django.urls import path
from core import views

urlpatterns = [
    path('', views.TodoListView.as_view(), name='list'),
    path('todo/create', views.TodoCreateView.as_view(), name='create'),
    path('todo/<int:pk>', views.TodoDetailView.as_view(), name='detail'),
    path('todo/<int:pk>/update', views.TodoUpdateView.as_view(), name='update'),
    path('todo/<int:pk>/delete', views.TodoDeleteView.as_view(), name='delete'),
]
