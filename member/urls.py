from django.contrib import admin
from django.urls import path
from member import views
urlpatterns = [
	path('',views.login,name="login"),
	path('logout',views.logout,name='logout'),
	path('dashboard',views.dashboard,name='dashboard'),
	path('add_member',views.add_member,name='Add Member'),
	path('delete_member',views.delete_member,name='Delete Member'),
	path('all_member',views.all_member,name='All Members'),
	path('edit_member',views.edit_member,name='Edit Member'),
	path('statics',views.statics,name='Statstics'),
	path('delete_member/<int:id1>',views.deletewithid,name="delete_member"),
	path('edit_member/<int:id1>',views.editwithid,name="edit_member"),
	]
