from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from .models import(Albums, Artists, AuthGroup, AuthUser, DjangoContentType,
                    AuthPermission, AuthGroupPermissions, AuthUserUserPermissions,
                    AuthUserGroups, DjangoMigrations, DjangoSession, Genres,
                    InvoiceItems, Invoices, Customers, DjangoAdminLog, Employees,
                    MediaTypes, Playlists, Tracks)


class Test1(ListView):
    template_name = 'test1.html'
    queryset = Artists.objects.first()
