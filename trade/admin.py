from django.contrib import admin

from trade.models import Trade


class TradeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Trade, TradeAdmin)
