from django.urls import path
from .views import *

urlpatterns=[
    path('index/',index),
    path('userprofile/',userprofile),
    path('userlogin/',UserLoginView),
    path('userregister/',UserRegisterView),
    path('userbio/<int:id>', userbio),
    path('displaybio/', displaybio),

    path('agencyprofile/',agencyprofile),
    path('agencylogin/', AgencyLogin),
    path('agencyregister/', AgencyRegister),
    path('uploadpackages/',uploadview),
    path('packagedisplay/', displayview),
    path('editpackage/<int:id>',editpackage),
    path('deletepackage/<int:id>',deletepackage),
    path('aboutus/',aboutus),
    path('contactus/',contactus),
    path('allpackages/',packageview),
    path('bookpackage/<int:id>', userbook),
    path('emailalert/', emailalert),

    path('addtowishlist/<int:id>',wishlist),
    path('wishdetail/',wishdetail),
    path('removewish/<int:id>',removewish),
    path('agencydetails/',agencydetails),
    path('bookeduser/',bookedusersdisplay),
    path('removebook/<int:id>', removebook),
    path('confirmationmail/<int:id>',agencyconfirm),
    path('placedetails/',statedetails)
]