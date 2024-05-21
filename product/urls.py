from django.urls import path
from .views import *

app_name = 'product'
urlpatterns = [
    path('category/', CategoryView.as_view(), name='gul-list'),
    path('gul/<int:pk>/', GulDetailView.as_view(), name='gul-detail'),
    path('gul_delete/<int:pk>',GulProductDelete.as_view(), name='gul-delete'),
    path('batafsil_review/<int:pk>',BatafsilReview.as_view(), name='batafsil-review'),
    path('addcomment<int:pk>', AddComment.as_view(), name='add-comment'),
    path('batafsil_malumot/<int:pk>',BatafsilMalumotView.as_view(), name='batafsil-malumot'),
    path('malumotview/', MalumotView.as_view(), name='malumot'),

    path('expensive/', ExpensiveProduct.as_view(), name='expensive'),
    path('arzon/',CheapProduct.as_view(), name='arzon'),

]


