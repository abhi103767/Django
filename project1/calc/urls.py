from django.urls import path , include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from . import views
from django.conf import settings

from django.conf.urls.static import static


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     print('amaing')
#     print(queryset)
#     serializer_class = UserSerializer()


router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    path('',views.home,name='home'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns  = urlpatterns + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)