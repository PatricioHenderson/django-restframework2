from django.urls import path
from e_commerce.api.marvel_api_views import *

# Importamos las API_VIEWS:
from e_commerce.api.api_views import *

urlpatterns = [
    # User APIs:
    path('user/login/', LoginUserAPIView.as_view()),

    # APIs de Marvel
    path('get_comics/',get_comics),
    path('purchased_item/',purchased_item),
    
    # Comic API View:
    path('comics/get', GetComicAPIView.as_view()),
    path('comics/<comic_id>/get', GetOneComicAPIView.as_view()),
    path('comics/post', PostComicAPIView.as_view()),
    path('comics/get-post', ListCreateComicAPIView.as_view()),
    path('comics/<pk>/update', RetrieveUpdateComicAPIView.as_view()),
    path('comics/<pk>/delete', DestroyComicAPIView.as_view()),

    # TODO: Wish-list API View
    # WishList API View
    path('wishlist/get', GetWishListAPIView.as_view()),
    path('wishsist/post', PostWishListAPIView.as_view()),
    path('wishlist/get-post' , ListCreateWishListAPIView.as_view()),
    path('wishlist/<pk>/update', RetrieveUpdateWishListAPIView.as_view()),
    path('wishlist/<pk>/delete', DestroyWishListAPIView.as_view()),
    path('wishlist/<username>/get', GetUserFavsAPIView.as_view()),

]