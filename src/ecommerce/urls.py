    
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from accounts.views import login_page,register_page, guest_register_view
from addresses.views import checkout_address_create_view,checkout_address_reuse_view


# from products.views import (
#         ProductListView,
#         product_list_view, 
#         ProductDetailView,
#         product_detail_view,
#         ProductFeaturedListView,
#         ProductFeaturedDetailView,
#         ProductDetailSlugView
#      )


from .views import home_page,about_page,contact_page,index

urlpatterns = [
	
    url(r'^$', index, name='index'),
    url(r'^home_page/$', home_page, name='home'),
    url(r'^about/$', about_page, name='about'),
    url(r'^contact/$', contact_page, name='contact'),
    url(r'^login/$', login_page,name='login'),
    url(r'^register/$', register_page, name='register'),
    url(r'^products/', include("products.urls", namespace='products')),
    url(r'^bootstrap/$', TemplateView.as_view(template_name='bootstrap/example.html')), 
    url(r'^search/', include("search.urls", namespace='search')),
    url(r'^cart/', include("carts.urls", namespace='cart')),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/guest/$', guest_register_view, name='guest_register'),
    url(r'^checkout/address/create/$', checkout_address_create_view, name='checkout_address_create'),
    url(r'^checkout/address/reuse/$', checkout_address_reuse_view, name='checkout_address_reuse'),
    
    
    # url(r'^featured/$', ProductFeaturedListView.as_view()),
    # url(r'^featured/(?P<pk>\d+)$', ProductFeaturedDetailView.as_view()),
    # url(r'^products/$', ProductListView.as_view()),
    # url(r'^products-fbv/$', product_list_view),
    # # url(r'^products/(?P<pk>\d+)$', ProductDetailView.as_view()),
    # url(r'^products/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
    # url(r'^products-fbv/(?P<pk>\d+)$', product_detail_view),

    url(r'^admin/', admin.site.urls),
]



if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# from django.conf import settings
# from django.conf.urls.static import static

# from django.conf.urls import url, include
# from django.contrib import admin
# from django.contrib.auth.views import LogoutView
# from django.views.generic import TemplateView


# from accounts.views import LoginView, RegisterView, guest_register_view
# from addresses.views import checkout_address_create_view, checkout_address_reuse_view
# from billing.views import payment_method_view, payment_method_createview
# from carts.views import cart_detail_api_view

# from .views import home_page, about_page, contact_page

# urlpatterns = [
#     url(r'^$', home_page, name='home'),
#     url(r'^about/$', about_page, name='about'),
#     url(r'^contact/$', contact_page, name='contact'),
#     url(r'^login/$', LoginView.as_view(), name='login'),
#     url(r'^checkout/address/create/$', checkout_address_create_view, name='checkout_address_create'),
#     url(r'^checkout/address/reuse/$', checkout_address_reuse_view, name='checkout_address_reuse'),
#     url(r'^register/guest/$', guest_register_view, name='guest_register'),
#     url(r'^logout/$', LogoutView.as_view(), name='logout'),
#     url(r'^api/cart/$', cart_detail_api_view, name='api-cart'),
#     url(r'^cart/', include("carts.urls", namespace='cart')),
#     url(r'^billing/payment-method/$', payment_method_view, name='billing-payment-method'),
#     url(r'^billing/payment-method/create/$', payment_method_createview, name='billing-payment-method-endpoint'),
#     url(r'^register/$', RegisterView.as_view(), name='register'),
#     url(r'^bootstrap/$', TemplateView.as_view(template_name='bootstrap/example.html')),
#     url(r'^products/', include("products.urls", namespace='products')),
#     url(r'^search/', include("search.urls", namespace='search')),
#     url(r'^admin/', admin.site.urls),
# ]
