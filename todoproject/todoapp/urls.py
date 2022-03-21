from django.urls import path
from . import views





urlpatterns = [
    path('',views.work,name='work'),
    path('delete/<int:tasks>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('listview/',views.List.as_view(),name='listview'),
    path('detailview/<int:pk>/',views.Detail.as_view(),name='detailview'),
    path('updateview/<int:pk>/',views.Update.as_view(),name='updateview'),
    path('deleteview/<int:pk>/',views.Delete.as_view(),name='deleteview'),
    ]
