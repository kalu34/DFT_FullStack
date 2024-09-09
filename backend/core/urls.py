from django.urls import path
from .api import views as api_view
from . import views

urlpatterns = [
    path('api/player/', api_view.PlayerList.as_view()),
    path('api/former_player/', api_view.FormerPlayerList.as_view()),
    path('api/gallery/', api_view.GalleryList.as_view()),
    path('api/staff/', api_view.StaffList.as_view()),
    path('api/staff/<int:id>/', api_view.StaffDetail.as_view()), 
    path('api/player/<slug:slug>/', api_view.PlayerDetail.as_view()), 
    path('api/shop/', api_view.ShopList.as_view()),
    path('api/news/', api_view.NewsList.as_view()),
    path('api/sponser/', api_view.SponserList.as_view()),
    path('api/players/create/', views.save_player_data, name='player-create'),

    path('contact-us', views.save_contact_form, name='contact-us'),


]