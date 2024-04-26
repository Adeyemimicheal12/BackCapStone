# from django.urls import path
# from .views import CreateEndPoint,UpdateEndPoint,DeleteEndPoint
# urlpatterns=[
#     path("users/create/",CreateEndPoint.as_view(), name="create-end"),
#     path("users/update-list/<int:pk>/",UpdateEndPoint.as_view(), name="updateend"),
#     path("users/delete-post/<int:pk>/",DeleteEndPoint.as_view(),name="delete-point")
# ]

# urls.py

from django.urls import path
from .views import create_blog_post, update_blog_post, delete_blog_post

urlpatterns = [
    path('users/create/', create_blog_post, name='create_blog_post'),
    path('users/update-posts/<int:pk>/', update_blog_post, name='update_blog_post'),
    path('users/delete-posts/<int:pk>/delete/', delete_blog_post, name='delete_blog_post'),
]
