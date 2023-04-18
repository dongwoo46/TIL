from django.urls import path
from . import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
        title='Music/Comment API',
        default_version='v1',
        description="음악과 댓글 정보를 제공하는 API 서비스입니다.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="happy@test.com"),
        license=openapi.License(name="TEST License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('musics/', views.music_list),
    path('musics/<int:music_pk>/', views.music_detail),
    path('redocs/', schema_view.with_ui('redoc')),
    path('swagger/', schema_view.with_ui('swagger')),
]
