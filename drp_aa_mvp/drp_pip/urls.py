from django.urls import path
from . import views


urlpatterns = [
    # DRP 0.7 API paths
    path('.well-known/data-rights.json', views.static_discovery, name='discovery'),
    # TKTKTK fix path to match
    path('v1/data-right-request/', views.exercise, name='receive_request'),
    path('v1/data-rights-request/<str:request_id>', views.get_status, name='get_status'),
    path('v1/agent/<str:aa_id>', views.agent, name='agent_router_ugghhh'),

    # service operation paths
    path('', views.index, name='index'),
    path('update-directory', views.update_directory, name='update-directory'),
]
