# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Artists(models.Model):
    # Field name made lowercase.
    id = models.IntegerField(db_column='ArtistId', primary_key=True)
    # Field name made lowercase. This field type is a guess.
    name = models.TextField(db_column='Name', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'artists'


class Albums(models.Model):
    # Field name made lowercase.
    artists = models.ForeignKey(Artists, db_column='ArtistId', on_delete="None")
    id = models.IntegerField(db_column='AlbumId', primary_key=True)
    # Field name made lowercase. This field type is a guess.
    title = models.TextField(db_column='Title')
    # artistid = models.IntegerField(db_column='ArtistId')  # Field name made lowercase.

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'albums'


class AuthGroup(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthUser(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    def __str__(self):
        return self.username

    class Meta:
        managed = False
        db_table = 'auth_user'


class DjangoContentType(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class AuthPermission(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthGroupPermissions(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING, db_column='group_id')
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING, db_column='permission_id')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthUserGroups(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='user_id')
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING, db_column='group_id')

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='user_id')
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING, db_column='permission_id')

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)

    def __str__(self):
        return self.firstname

    class Meta:
        managed = False
        db_table = 'customers'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoMigrations(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employees(models.Model):
    # Field name made lowercase.
    employeeid = models.IntegerField(db_column='EmployeeId', primary_key=True)
    # Field name made lowercase. This field type is a guess.
    lastname = models.TextField(db_column='LastName')
    # Field name made lowercase. This field type is a guess.
    firstname = models.TextField(db_column='FirstName')
    # Field name made lowercase. This field type is a guess.
    title = models.TextField(db_column='Title', blank=True, null=True)
    # Field name made lowercase.
    reportsto = models.ForeignKey("self", models.DO_NOTHING,
                                  db_column='ReportsTo', blank=True, null=True)
    # Field name made lowercase.
    birthdate = models.DateTimeField(db_column='BirthDate', blank=True, null=True)
    # Field name made lowercase.
    hiredate = models.DateTimeField(db_column='HireDate', blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    address = models.TextField(db_column='Address', blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    city = models.TextField(db_column='City', blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    state = models.TextField(db_column='State', blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    country = models.TextField(db_column='Country', blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    postalcode = models.TextField(db_column='PostalCode', blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    phone = models.TextField(db_column='Phone', blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    fax = models.TextField(db_column='Fax', blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    email = models.TextField(db_column='Email', blank=True, null=True)

    def __str__(self):
        return self.firstname

    class Meta:
        managed = False
        db_table = 'employees'


class Customers(models.Model):
    # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId', primary_key=True)
    # Field name made lowercase. This field type is a guess.
    firstname = models.TextField(db_column='FirstName')
    # Field name made lowercase. This field type is a guess.
    lastname = models.TextField(db_column='LastName')
    # Field name made lowercase. This field type is a guess.
    company = models.TextField(db_column='Company', blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    address = models.TextField(db_column='Address', blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    city = models.TextField(db_column='City', blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    state = models.TextField(db_column='State', blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    country = models.TextField(db_column='Country', blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    postalcode = models.TextField(db_column='PostalCode', blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    phone = models.TextField(db_column='Phone', blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    fax = models.TextField(db_column='Fax', blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    email = models.TextField(db_column='Email')
    # Field name made lowercase.
    supportrepid = models.ForeignKey(Employees, models.DO_NOTHING,
                                     db_column='SupportRepId', blank=True, null=True)

    def __str__(self):
        return self.firstname+" "+self.lastname

    class Meta:
        managed = False
        db_table = 'customers'


class Genres(models.Model):
    # Field name made lowercase.
    genreid = models.IntegerField(db_column='GenreId', primary_key=True)
    # Field name made lowercase. This field type is a guess.
    name = models.TextField(db_column='Name', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genres'

#


#


class Invoices(models.Model):
    # Field name made lowercase.
    id = models.IntegerField(db_column='InvoiceId', primary_key=True)
    # Field name made lowercase.
    customerid = models.ForeignKey(Customers, models.DO_NOTHING, db_column='CustomerId')
    invoicedate = models.DateTimeField(db_column='InvoiceDate')  # Field name made lowercase.
    # Field name made lowercase. This field type is a guess.
    billingaddress = models.TextField(db_column='BillingAddress', blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    billingcity = models.TextField(db_column='BillingCity', blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    billingstate = models.TextField(db_column='BillingState', blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    billingcountry = models.TextField(db_column='BillingCountry', blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    billingpostalcode = models.TextField(db_column='BillingPostalCode', blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    total = models.TextField(db_column='Total')

    def __str__(self):
        return str(self.id)

    class Meta:
        managed = False
        db_table = 'invoices'


class MediaTypes(models.Model):
    # Field name made lowercase.
    mediatypeid = models.IntegerField(db_column='MediaTypeId', primary_key=True)
    # Field name made lowercase. This field type is a guess.
    name = models.TextField(db_column='Name', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'media_types'


# class SqliteStat1(models.Model):
#     tbl = models.TextField(blank=True, null=True)  # This field type is a guess.
#     idx = models.TextField(blank=True, null=True)  # This field type is a guess.
#     stat = models.TextField(blank=True, null=True)  # This field type is a guess.
#
#     class Meta:
#         managed = False
#         db_table = 'sqlite_stat1'

#
class Tracks(models.Model):
    # Field name made lowercase.
    trackid = models.IntegerField(db_column='TrackId', primary_key=True)
    # Field name made lowercase. This field type is a guess.
    name = models.TextField(db_column='Name')
    # Field name made lowercase.
    albumid = models.ForeignKey(Albums, on_delete=models.CASCADE,
                                db_column='AlbumId', blank=True, null=True)
    # Field name made lowercase.
    mediatypeid = models.ForeignKey(MediaTypes, models.DO_NOTHING, db_column='MediaTypeId')
    # Field name made lowercase.
    genreid = models.ForeignKey(Genres, models.DO_NOTHING,
                                db_column='GenreId', blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    composer = models.TextField(db_column='Composer', blank=True, null=True)
    milliseconds = models.IntegerField(db_column='Milliseconds')  # Field name made lowercase.
    # Field name made lowercase.
    bytes = models.IntegerField(db_column='Bytes', blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    unitprice = models.TextField(db_column='UnitPrice')

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'tracks'


class InvoiceItems(models.Model):
    # Field name made lowercase.
    id = models.IntegerField(db_column='InvoiceLineId', primary_key=True)
    # Field name made lowercase.
    invoiceid = models.ForeignKey(Invoices, models.DO_NOTHING, db_column='InvoiceId')
    # Field name made lowercase.
    trackid = models.ForeignKey(Tracks, models.DO_NOTHING, db_column='TrackId')
    # Field name made lowercase. This field type is a guess.
    unitprice = models.TextField(db_column='UnitPrice')
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.

    def __str__(self):
        return str(self.id)

    class Meta:
        managed = False
        db_table = 'invoice_items'

#


class Playlists(models.Model):
    # Field name made lowercase.
    id = models.IntegerField(db_column='PlaylistId', primary_key=True)
    # Field name made lowercase. This field type is a guess.
    name = models.TextField(db_column='Name', blank=True, null=True)
    track = models.ManyToManyField(Tracks)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'playlists'


# class PlaylistTrack(models.Model):
#     # Field name made lowercase.
#     playlistid = models.ForeignKey(Playlists, models.DO_NOTHING, db_column='PlaylistId')
#     # Field name made lowercase.
#     trackid = models.ForeignKey(Tracks, models.DO_NOTHING,
#                                 db_column='TrackId', related_name="rel_track")
#
#     class Meta:
#         managed = False
#         db_table = 'playlist_track'
#         unique_together = (('playlistid', 'trackid'),)
