from django.urls import path, include

urlpatterns = [
    path('', include('dse.urls')),
    path('', include('transpiler.urls')),
    path('', include('codecoverage.urls'))
]
