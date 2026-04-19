from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', 'blog')),
    path('pages/', include('pages.urls', 'pages')),
]
