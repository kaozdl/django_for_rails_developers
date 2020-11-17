from rest_framework import routers

from api import views


router = routers.DefaultRouter()
router.register(r'boards', views.BoardViewSet)
router.register(r'columns', views.ColumnViewSet)
router.register(r'cards', views.CardViewSet)

urlpatterns = router.urls
