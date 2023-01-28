from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from django.conf import settings
from django.conf.urls.static import static
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('obtaintoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'),

    path('user/',views.UserApiView.as_view()),
    path('user/<int:pk>',views.UserApiView.as_view()),
    path('display',views.display),    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)