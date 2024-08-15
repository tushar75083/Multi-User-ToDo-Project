from django.urls import path
from myapp import views
urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.user_login,name='login'),
    path('signup/',views.user_signup,name='signup'),
    path('logout/',views.user_logout,name='logout'),
    path('addtodo/',views.addtodo,name='addtodo'),
    path('alltodo/',views.alltodo,name='alltodo'),
    path('edit/<int:rid>/',views.editTodo,name='edit'),
    path('delete/<int:rid>/',views.deleteTodo,name='delete'),
]
