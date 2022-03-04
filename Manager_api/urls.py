"""Manager_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from core.views import *
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

# existing serializer, viewset, router registrations code
...

# Create our schema's view w/ the get_schema_view() helper method. Pass in the proper Renderers for swagger
schema_view = get_schema_view(title='Users API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])


router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'projet',ProjetViewSet)
router.register(r'taches',TacheViewSet)
router.register(r'rtaches',Relation_TachesViewSet)
router.register(r'employe',EmployeViewSet)
router.register(r'Remploye',Rapport_employeViewSet)
router.register(r'suivre',SuivreViewSet)
router.register(r'coment', CommentairesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(router.urls)),
    path('userid/', UserIdViewset.as_view()),
    path('userre/', UserReViewset.as_view()),
    path('projet_user/', ProjetUserViewset.as_view()),
    path('taches_user/', TacheUserViewSet.as_view()),


    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('manager/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('manager/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #the doc
    path(r'admindoc', schema_view, name="docs"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)