from django.urls import path
from .views import GetTasks, SingleTask ,AddTask,UpdateTask


urlpatterns =[ 
    path("",GetTasks.as_view()),
    path('<int:pk>',SingleTask.as_view()),
    path('task', AddTask.as_view()),
    path('update/<int:pk>', UpdateTask.as_view()),

 
 
    ]
