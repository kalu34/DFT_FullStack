from django.contrib import admin
from .models import Player, FormerPlayer, News, Gallery,Staff,Shop,ContactMessage,Sponser

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'dateOfBirth','gender', 'position', 'phone') 
    list_filter = ('age', 'gender', 'position') 
    search_fields = ('name','last_name')
    prepopulated_fields = {'slug': ('name', 'last_name',)}

admin.site.register(Player, PlayerAdmin)

class FormerPlayerAdmin(admin.ModelAdmin):
    list_display = ('player_name', 'player_age', 'player_gender')
    list_filter = ('player__age', 'player__gender', 'player__position') 
    search_fields = ('player__name','player__last_name')
   

    def player_name(self, obj):
        return obj.player.name

    def player_age(self, obj):
        return obj.player.age

    def player_gender(self, obj):
        return obj.player.gender

admin.site.register(FormerPlayer, FormerPlayerAdmin)

# 
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description') 
    search_fields = ('title','last_name')

admin.site.register(Gallery, GalleryAdmin)
# 
class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'position') 
    search_fields = ('name','position')

admin.site.register(Staff, StaffAdmin)
# 
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'price') 
    search_fields = ('name','price')

admin.site.register(Shop, ShopAdmin)
admin.site.register(ContactMessage)
admin.site.register(Sponser)
admin.site.register(News)