from django.urls import path, include

urlpatterns = [
    path('', include('frontend.urls')),
    path('', include('dse.urls')),
    path('', include('transpiler.urls')),
    path('', include('codecoverage.urls'))
]
