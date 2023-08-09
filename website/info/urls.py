from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.newinfo, name='newinfosnake'),
    path('create', views.create, name='create'),
    path('<int:pk>/', views.NewinfoDetailView.as_view(), name='datilesnake'),
    path('<int:pk>/update', views.NewinfoDetailViewUpdate.as_view(), name='datilesnake_update'),
    path('<int:pk>/delete', views.NewinfoDetailViewDelete.as_view(), name='datilesnake_delete')

]
