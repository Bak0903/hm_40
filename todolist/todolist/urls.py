
from django.contrib import admin
from django.urls import path
from webapp.views import index_view, change_status, delete_task, edit_task, kill_all

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('task/<int:task_id>/new_status', change_status, name='new_status'),
    path('task/<int:task_id>/delete', delete_task, name='delete'),
    path('task/<int:task_id>/edit', edit_task, name='edit'),
    path('kill_all', kill_all, name='kill_all')
]
