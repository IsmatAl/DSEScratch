from django.urls import path
from .api import PexAPI

urlpatterns = [
    path('api/pex', PexAPI.as_view({'post': 'postDSE'})),
    path('api/pair', PexAPI.as_view({'post': 'postProgramPairing'})),
    path('api/rs', PexAPI.as_view({'post': 'postRandomSampling'})),
    path('api/ref', PexAPI.as_view({'post': 'postRef'})),
    path('api/pse', PexAPI.as_view({'post': 'postPSE'}))
]
