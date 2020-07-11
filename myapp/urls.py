from django.urls import path
from . import views
from .views import (
    ItemDetailView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    SendFormEmail,
     # PaymentViewbyCash
)

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<^/s/$>',views.search,name='search'),
    path('<str:pk_test>',views.menusearch,name='menusearch'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
#     path('paycash/', PaymentViewbyCash.as_view(), name='cash'),     
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('accounts/register/', views.registerPage, name="register"),
    path('accounts/login/', views.loginPage, name="login"),
    path('accounts/logout/', views.logoutUser, name="logout"),
    
    path('process-payment/', views.process_payment, name='process_payment'),
    path('payment-done/', views.payment_done, name='payment_done'),
    path('payment-cancelled/', views.payment_canceled, name='payment_cancelled'),
    #Reset password start here
    path('reset_password/',auth_views.PasswordResetView.as_view(),name="reset_password" ),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done" ),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm" ),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete" ),
    path('about/', views.about , name='about'),
    #Contact us

    path('send-form-email/',views.SendFormEmail.as_view(),name='send_email'),
   
   
    
    
    
    
 
    
]
