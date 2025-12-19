from django.urls import path
from .views import PostView,PostDetailView

app_name="blog" #Reverse function use this to find the url page

urlpatterns=[
    path("post",PostView.as_view(),name="post"),
     path('<int:year>/<int:month>/<int:day>/<slug:slug>/',
         PostDetailView.as_view(),
         name='post_detail'),
]

"""

"""