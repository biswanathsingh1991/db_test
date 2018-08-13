from django.contrib import admin
# from . models import (Albums, Artists, Customers, Employees,
#                       Genres, InvoiceItems, Invoices, MediaTypes,
#                       PlaylistTrack, Playlists, SqliteStat1, Tracks)
# Register your models here.

from .models import(Albums, Artists, AuthGroup, AuthUser, DjangoContentType,
                    AuthPermission, AuthGroupPermissions, AuthUserUserPermissions,
                    AuthUserGroups, DjangoMigrations, DjangoSession, Genres,
                    InvoiceItems, Invoices, Customers, DjangoAdminLog, Employees,
                    MediaTypes, Playlists, Tracks)
admin.site.register(Albums)
admin.site.register(Artists)
admin.site.register(AuthGroup)
admin.site.register(AuthUser)
admin.site.register(DjangoContentType)
admin.site.register(AuthPermission)
admin.site.register(AuthGroupPermissions)
admin.site.register(AuthUserUserPermissions)
admin.site.register(AuthUserGroups)
admin.site.register(DjangoMigrations)
admin.site.register(DjangoSession)
admin.site.register(Genres)
admin.site.register(InvoiceItems)
admin.site.register(Invoices)
admin.site.register(Customers)
admin.site.register(DjangoAdminLog)
admin.site.register(Employees)
admin.site.register(MediaTypes)
# admin.site.register(PlaylistTrack)
admin.site.register(Playlists)
admin.site.register(Tracks)
