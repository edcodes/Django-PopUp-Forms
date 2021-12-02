from django.urls import path
from .views import PhoneBookList, PhoneBookReadPopup ,PhoneBookCreatePopup,PhoneBookUpdatePopup,PhoneBookDeletePopup

urlpatterns = [

    path('', PhoneBookList.as_view(), name='phonebook-list'),
    path('popup/<int:pk>/', PhoneBookReadPopup.as_view(), name='phonebook-detail-popup'),
    path('popupcreate/', PhoneBookCreatePopup.as_view(), name='phonebook-create-popup'),
    path('popupupdate/<int:pk>/', PhoneBookUpdatePopup.as_view(), name='phonebook-update-popup'),
    path('popupdelete/<int:pk>/', PhoneBookDeletePopup.as_view(), name='phonebook-delete-popup'),
   
]


