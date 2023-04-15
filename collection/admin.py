from django.contrib import admin
from .models import Collection, Game_Wishlist, Game_Blacklist

admin.site.register(Collection)
admin.site.register(Game_Wishlist)
admin.site.register(Game_Blacklist)
