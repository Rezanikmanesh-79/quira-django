from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login.as_view(), name='login'),
    path('tasks/', login_required(views.ListOfTasks.as_view()), name='task_list'),
    path('tasks/<int:pk>/', login_required(views.TaskDetail.as_view()), name='task_detail'),
    path('tasks/<int:pk>/done/', login_required(views.MarkTaskDone.as_view()), name='mark_task_done'),
    path('tasks/<int:pk>/update/', login_required(views.TaskUpdateView.as_view()), name='update_task'),
]
