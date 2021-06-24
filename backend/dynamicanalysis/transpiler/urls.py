from django.urls import path
from .api import TransplileAPI

urlpatterns = [
  path('api/upload', TransplileAPI.as_view({'post': 'postUploadFile'})),
  path('api/delete', TransplileAPI.as_view({'delete': 'deleteFile'})),
  path('api/files', TransplileAPI.as_view({'get': 'getFiles'})),
  path('api/active', TransplileAPI.as_view({'post': 'postActiveFile'})),
  path('api/code', TransplileAPI.as_view({'post': 'postCode'}))
]