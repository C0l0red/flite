from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .users import views as user_views


router = DefaultRouter()
router.register(r'users', user_views.UserViewSet)
router.register(r'users', user_views.UserBankTransfersViewset, basename='user')
router.register(r'users', user_views.UserCreateViewSet)
router.register(r'phone', user_views.SendNewPhonenumberVerifyViewSet)
router.register(r'account', user_views.UserAccountTransactionsViewSet, basename='account')
router.register(r'account', user_views.UserP2PTransferCreateViewSet, basename='account')



urlpatterns = [
    path('admin/', admin.site.urls),
    #   path('jet_api/', include('jet_django.urls')),
    path('api/v1/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

