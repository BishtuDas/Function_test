from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
# from exam import views as auth_view
admin.site.site_header = 'Dashboard'                    # default: "Django Administration"
admin.site.index_title = 'Admin Panel'                 # default: "Site administration"
admin.site.site_title = 'Admin Panel' # default: "Django site admin"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

