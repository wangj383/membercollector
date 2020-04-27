from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('members/', views.members_index, name='members_index'),
    path('members/<int:member_id>', views.member_detail, name='member_detail'),
    path('members/create',views.MemberCreateView.as_view(), name="member_create"),
    path('members/<int:pk>/update', views.MemberUpdateView.as_view(), name='member_update'),
    path('members/<int:pk>/delete', views.MemberDeleteView.as_view(), name='member_delete'),
    path('members/<int:member_id>/add_task', views.add_task, name='add_task'),
    path('members/<int:member_id>/associate_event/<int:event_id>', views.associate_event, name='associate_event'),
    path('members/<int:member_id>/events/<int:event_id>', views.unassociate_event, name="unassociate_event"),
    path('members/<int:member_id>/add_photo', views.add_photo, name='add_photo'),
    path('accounts/signup', views.signup, name = 'signup'),
]