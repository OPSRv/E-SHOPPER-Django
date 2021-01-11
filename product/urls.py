from django.urls import path, include
from . import views
from .views import SearchResultsView

urlpatterns = [
    path('<int:product_id>/', views.cart, name="cart"),
    path('search/', SearchResultsView.as_view(), name='search_results')
]