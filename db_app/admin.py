from django.contrib import admin
# from . models import (Albums, Artists, Customers, Employees,
#                       Genres, InvoiceItems, Invoices, MediaTypes,
#                       PlaylistTrack, Playlists, SqliteStat1, Tracks)
# Register your models here.

from .models import Albums, Artists
admin.site.register(Albums)
admin.site.register(Artists)
# admin.site.register(Customers)
# admin.site.register(Employees)
# admin.site.register(Genres)
# admin.site.register(InvoiceItems)
# admin.site.register(Invoices)
# admin.site.register(MediaTypes)
# admin.site.register(PlaylistTrack)
# admin.site.register(SqliteStat1)
# admin.site.register(Playlists)
# admin.site.register(Tracks)
