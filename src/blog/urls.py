from django.urls import path
from .views import post_list, post_detail, PostListView, post_share, post_new
from .feeds import LatestPostsFeed

app_name = 'blog'


urlpatterns = [
    path('', post_list, name='post_list'),
    path('tag/<slug:tag_slug>/', post_list, name='post_list_by_tag'),
    # path('', PostListView.as_view(), name='post_list'),

    path('<int:year>/<int:month>/<int:day>/<slug:post_slug>', post_detail, name='post_detail'),
    path('<int:post_id>/share/', post_share, name='post_share'),
    path('post/new/', post_new, name='post_new'),

    path('feed/', LatestPostsFeed(), name='post_feed'),
]
