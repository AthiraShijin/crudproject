
from django.urls import path
from.import views

urlpatterns = [
    
    
    path('',views.crud,name='crud'),
    path('Delete/<int:task_id>/',views.Delete,name='Delete'),
    path('Update/<int:task_id1>/',views.Update,name='Update'),
]
