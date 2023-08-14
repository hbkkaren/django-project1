from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name="contact"),
    path('blog/',views.blog,name="blog"),
    path('cart/',views.cart,name="cart"),
    path('category/',views.category,name="category"),
    path('confirmation/',views.confirmation,name="confirmation"),
    path('elements/',views.elements,name="elements"),
    path('login/',views.login,name="login"),
    path('single-blog/',views.single_blog,name="single-blog"),
    path('single-product/',views.single_product,name="single-product"),
    path('tracking/',views.tracking,name="tracking"),
    path('checkout/',views.checkout,name="checkout"),
    path('signup/',views.signup,name="signup"),
    path('logout/',views.logout,name="logout"),
    path('change-password/',views.change_password,name="change-password"),
    path('seller-add-product',views.seller_add_product,name="seller-add-product"),
    path('seller-view-product',views.seller_view_product,name="seller-view-product"),
    path('seller-product-detail/<int:pk>/',views.seller_product_detail,name="seller-product-detail"),
    path('seller-edit-product/<int:pk>/',views.seller_edit_product,name="seller-edit-product"),
    path('seller-index/',views.seller_index,name="seller-index"),
    path('seller-delete-product/<int:pk>/',views.seller_delete_product,name="seller-delete-product"),
    path('product-detail/<int:pk>/',views.product_detail,name="product-detail"),
    path('add-to-wishlist/<int:pk>/',views.add_to_wishlist,name="add-to-wishlist"),
    path('remove-from-wishlist/<int:pk>/',views.remove_from_wishlist,name="remove-from-wishlist"),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('add-to-cart/<int:pk>/',views.add_to_cart,name="add-to-cart"),
    path('remove-from-cart/<int:pk>/',views.remove_from_cart,name="remove-from-cart"),
    path('cart/',views.cart,name='cart'),
    path('change-qty/',views.change_qty,name='change-qty'),
    path('create-checkout-session/', views.create_checkout_session, name='payment'),
    path('success.html/', views.success,name='success'),
    path('cancel.html/', views.cancel,name='cancel'),
    path('forgot-password/',views.forgot_password,name='forgot-password'),
    path('verify-otp/',views.verify_otp,name='verify-otp'),
    path('new-password/',views.new_password,name='new-password'),
    path('myorder/',views.myorder,name='myorder'),
    
    
   

    
    



    
]
