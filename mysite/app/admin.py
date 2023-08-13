from django.contrib import admin
from .models import Advertisement

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_date', 'updated_date', 'auction', 'image']
    list_filter = ['auction', "created_at"]
    actions = ["MakeAuctionAsFalse", "MakeAuctionAsTrue"]
    fieldsets = (
        (
            'Общее', {"fields": ('title', 'description', 'image')}
        ),
        (
            'Финансы', {"fields": ('price', 'auction'), "classes": ["collapse"]}
        ),
    )
    
    @admin.action(description="убрать торг")
    def MakeAuctionAsFalse(self,request, quaryset):
        quaryset.update(auction=False)
        
    @admin.action(description="добавить торг")
    def MakeAuctionAsTrue(self,request, quaryset):
        quaryset.update(auction=True)

admin.site.register(Advertisement, AdvertisementAdmin)

