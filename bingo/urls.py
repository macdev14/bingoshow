from django.urls import path
from bingo.views import HomeView, UserView, PerguntaViewSet, TabelaViewSet, UserViewSet, GerarTabela

from django.urls import path, include

from rest_framework import routers, serializers, viewsets

app_name='bingo'

router = routers.DefaultRouter()
router.register(r'pergunta', PerguntaViewSet, basename='bingo-pergunta')
router.register(r'tabela', TabelaViewSet, basename='bingo-tabela')
router.register(r'usuario', UserViewSet, basename='bingo-user')
# router.register(r'gerartabela', GerarTabela.as_view(), basename='bingo-gerar' )
urlpatterns = [
    path('', UserView.as_view(), name='user' ),
    path('bingo/<int:pk>', HomeView.as_view(), name='home' ),
    path('api/', include(router.urls),name="api"),
    path('api/gerartabela/', GerarTabela.as_view(),name="gerar"),
]