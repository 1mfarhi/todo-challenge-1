from django.urls import path
from todo.views import TodoDetailView, TodoListView, NoteDetailView, NoteListView





urlpatterns = [
    path('', TodoListView.as_view(), name='todo_list'),
    path('<int:task_id>', TodoDetailView.as_view(), name='task'),
    path('note/', NoteListView.as_view(), name='note_list'),
    path('<int:note_id>', NoteDetailView.as_view(), name='note'),
]
