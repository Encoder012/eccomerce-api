from rest_framework import routers
from home import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
