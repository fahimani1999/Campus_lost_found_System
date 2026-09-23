"""
URL configuration for campus_lost_found project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from report import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("home/", views.home, name="home_alias"),

    path(
        "reports/",
        views.report_list,
        name="reports"
    ),

    path(
        "reports/<int:pk>/",
        views.report_detail,
        name="report_detail"
    ),

    path(
        "reports/create/",
        views.report_create,
        name="report_create"
    ),

    path(
        "reports/<int:pk>/edit/",
        views.report_update,
        name="report_update"
    ),

    path(
        "reports/<int:pk>/delete/",
        views.report_delete,
        name="report_delete"
    ),

    path(
        "reports/<int:pk>/resolve/",
        views.report_resolve,
        name="report_resolve"
    ),

    path(
        "my-reports/",
        views.my_reports,
        name="my_reports"
    ),

    path(
        "register/",
        views.register,
        name="register"
    ),

    path(
        "login/",
        views.UserLoginView.as_view(),
        name="login"
    ),

    path(
        "logout/",
        views.UserLogoutView.as_view(),
        name="logout"
    ),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )