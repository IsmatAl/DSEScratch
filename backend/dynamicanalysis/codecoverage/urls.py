from .views import codecoverage_view
from django.urls import path
from .api import CodeCoverageAPI

urlpatterns = [
    path('api/cvg', CodeCoverageAPI.as_view({'post': 'postCoverage'})),
    path('api/sse',
         CodeCoverageAPI.as_view({'post': 'postSSE'})),
#     path('api/pse',
#          CodeCoverageAPI.as_view({'post': 'postPSE'})),
    path('api/coverage-report', codecoverage_view)         
]
