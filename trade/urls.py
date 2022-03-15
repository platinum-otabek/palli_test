from django.urls import path
from rest_framework.routers import DefaultRouter

from trade.views.Category import CategoryListCreateApiView, CategoryProductDetail
from trade.views.Customer import CustomerWithoutOrdersView, CustomerLastOrdersView
from trade.views.Invoice import InvoiceExpiredViews, OverpaidInvoicesView
from trade.views.Order import OrderCreateApiView, OrderDetailView, OrderWithoutDetailView, OrderWithOutInvoiceView
from trade.views.Payment import PaymentWithInvoiceApiView, PaymentDetailView
from trade.views.Product import ProductListCreateApiView, ProductDetailApiView, HighDemandProducts, BulkProductsView, \
    NumberOfProductsInYearView

router = DefaultRouter()
urlpatterns = [
    #category
    path('category/<int:product_id>/', CategoryProductDetail.as_view(), name='category-product-detail'),

    #product
    path('product/', ProductListCreateApiView.as_view(), name='product-list'),
    path('high_demand_products/', HighDemandProducts.as_view(), name='high_demand_products-list'),
    path('product/<int:product_id>', ProductDetailApiView.as_view(), name='product-list'),
    path('bulk_products/', BulkProductsView.as_view(), name='bulk_products'),
    path('number_of_products_in_year/', NumberOfProductsInYearView.as_view(), name='number_of_products_in_year'),

    #order
    path('order/', OrderCreateApiView.as_view(), name='order-list'),
    path('order/detail/<int:order_id>/', OrderDetailView.as_view(), name='order-detail'),
    path('orders_without_details/', OrderWithoutDetailView.as_view(), name='orders_without_details'),
    path('orders_without_invoices/', OrderWithOutInvoiceView.as_view(), name='orders_without_invoices'),


    #payment
    path('payment/', PaymentWithInvoiceApiView.as_view(), name='payment'),
    path('payment/<int:pk>', PaymentDetailView.as_view(), name='payment-detail'),

    #invoice
    path('expired_invoices/', InvoiceExpiredViews.as_view(), name='experid_invoices'),

    #customer
    path('customers_without_orders/', CustomerWithoutOrdersView.as_view(), name='customers_without_orders'),
    path('customers_last_orders/', CustomerLastOrdersView.as_view(), name='customers_last_orders'),

    #invoice
    path('overpaid_invoices/', PaymentDetailView.as_view(), name='overpaid_invoices'),

]
router.register('category', CategoryListCreateApiView)

urlpatterns += router.urls
