from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('vendor/', views.VendorListView.as_view(), name='vendor_list'),
    path('add_vendor/', views.VendorCreateView.as_view(), name='vendor_create'),
    path('stock/', views.StockListView.as_view(), name='stock_list'),
    path('add_stock/', views.StockCreateView.as_view(), name='stock_create'),
    # path('create/', views.create_session),
    # path('get/', views.get_session),
    # path('delete/', views.delete_session),
    # path('createcookie/', views.cookie_session),
    # path('deletecookie/', views.cookie_delete),
]