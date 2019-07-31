"""practicehere URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views
from accounts import views as ac_views
from django.contrib.auth.views import LoginView,LogoutView
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('new/', views.new, name="new"),
    path('detail/<int:blog_id>', views.detail, name="detail"),
    path('edit/<int:blog_id>', views.edit, name="edit"),
    path('delete/<int:blog_id>', views.delete, name="delete"),
    path('signup/', ac_views.signup, name="signup"),
    path('accounts/login/', LoginView.as_view(), name="login"),
    path('accounts/logout/', LogoutView.as_view(), name="logout"),
    path('portfolio/', portfolio.views.portfolio, name="portfolio"),
    path('accounts/profile/', ac_views.profile, name="profile"),
] 

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#CBV Class Based View, FBV Function Based View
