from django.urls import path
from .views import AdminProcess, AcceptOfferAdmin, RejectOfferAdmin, Profile, Offer, Home, Payments, Search, Passenger, ConfirmBooking


urlpatterns = [
     path('', Home, name="home"),
    path('addoffer/',Offer, name='addoffer'),
    path("adminreview/", AdminProcess, name= 'adminreview'),
    path("accept/<int:pk>",AcceptOfferAdmin,name="accept"),
    path("reject/<int:pk>",RejectOfferAdmin, name="reject"),
    path('profile/',Profile, name='profile'),
    path('payment/', Payments, name='payment'),
    path('search/', Search, name='search'),
    path('passenger/', Passenger, name='passenger'),
    path('confirmbooking/', ConfirmBooking, name='confirmbooking'),
] 