from django.urls import path
from . import views
from .views import PostListViewS,PostDetailViewS,PostCreateViewS,PostUpdateViewS,PostDeleteViewS,UserPostListViewS
from .views import PostListViewA,PostDetailViewA,PostCreateViewA,PostUpdateViewA



urlpatterns = [
    path('suggest/',PostListViewS.as_view() , name='HealthyNSU-healthsuggest'),
    path('suggest/user/<str:username>', UserPostListViewS.as_view() , name='user-posts'),
    path('suggest/post/<int:pk>',PostDetailViewS.as_view() , name='post-detailsug'),
    path('suggest/post/new/',PostCreateViewS.as_view() , name='post-create'),
    path('suggest/post/<int:pk>/update/',PostUpdateViewS.as_view() , name='post-update'),
    path('suggest/post/<int:pk>/delete/',PostDeleteViewS.as_view() , name='post-delete'),


    path('ask/', PostListViewA.as_view(), name='HealthyNSU-healthask'),
    path('ask/post/<int:pk>',PostDetailViewA.as_view() , name='post-detailask'),
    path('ask/post/new',PostCreateViewA.as_view() , name='post-create'),
    path('ask/post/<int:pk>/update/',PostUpdateViewS.as_view() , name='post-update'),
    path('ask/post/<int:pk>/delete/',PostDeleteViewS.as_view() , name='post-delete'),
    ]
