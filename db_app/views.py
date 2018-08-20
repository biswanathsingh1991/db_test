from django.shortcuts import render
from django.views.generic import ListView, TemplateView
# Create your views here.
from .models import(Albums, Artists, AuthGroup, AuthUser, DjangoContentType,
                    AuthPermission, AuthGroupPermissions, AuthUserUserPermissions,
                    AuthUserGroups, DjangoMigrations, DjangoSession, Genres,
                    InvoiceItems, Invoices, Customers, DjangoAdminLog, Employees,
                    MediaTypes, Playlists, Tracks)
from rest_framework.generics import ListAPIView
from . serializer import SerializersAllalbum


class Test1(ListView):
    template_name = 'test1.html'
    queryset = Albums.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        # genres = Genres.objects.all()
        media_type = MediaTypes.objects.all()[3]
        media = Tracks.objects.filter(mediatypeid=media_type)
        context['media'] = media
        context['media_count'] = media.count()
        context['media_type'] = media_type
        composer = Tracks.objects.only('composer')
        context['composer'] = composer
        context.update(kwargs)
        return context


class Allalbum(TemplateView):
    template_name = 'allalbum.html'


class AllAlbumApi(ListAPIView):
    template_name = 'allalbum.html'
    queryset = Albums.objects.all()
    serializer_class = SerializersAllalbum
