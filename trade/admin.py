from django.contrib import admin

from trade.models import (Customer, Category, Detail, Order, Payment, Product, Invoice)


# Register your models here.
# customer
@admin.register(Customer.CustomerModel)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'country', 'address', 'phone')


# category
@admin.register(Category.CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk','name')


# detail
@admin.register(Detail.DetailModel)
class DetailAdmin(admin.ModelAdmin):
    list_display = ('pk', 'order', 'product', 'quantity')


# invoice
@admin.register(Invoice.InvoiceModel)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('pk', 'order', 'amount', 'issued', 'due')


# order
@admin.register(Order.OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'date', 'customer')


# payment
@admin.register(Payment.PaymentModel)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'time', 'amount', 'invoice')


# product
@admin.register(Product.ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'category', 'description', 'price', 'photo')
