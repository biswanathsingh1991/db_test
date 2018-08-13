# Generated by Django 2.1 on 2018-08-13 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.IntegerField(db_column='AlbumId', primary_key=True, serialize=False)),
                ('title', models.TextField(db_column='Title')),
            ],
            options={
                'db_table': 'albums',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Artists',
            fields=[
                ('id', models.IntegerField(db_column='ArtistId', primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
            ],
            options={
                'db_table': 'artists',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codename', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
                ('last_name', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customerid', models.IntegerField(db_column='CustomerId', primary_key=True, serialize=False)),
                ('firstname', models.TextField(db_column='FirstName')),
                ('lastname', models.TextField(db_column='LastName')),
                ('company', models.TextField(blank=True, db_column='Company', null=True)),
                ('address', models.TextField(blank=True, db_column='Address', null=True)),
                ('city', models.TextField(blank=True, db_column='City', null=True)),
                ('state', models.TextField(blank=True, db_column='State', null=True)),
                ('country', models.TextField(blank=True, db_column='Country', null=True)),
                ('postalcode', models.TextField(blank=True, db_column='PostalCode', null=True)),
                ('phone', models.TextField(blank=True, db_column='Phone', null=True)),
                ('fax', models.TextField(blank=True, db_column='Fax', null=True)),
                ('email', models.TextField(db_column='Email')),
                ('supportrepid', models.IntegerField(blank=True, db_column='SupportRepId', null=True)),
            ],
            options={
                'db_table': 'customers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('change_message', models.TextField()),
                ('action_flag', models.PositiveSmallIntegerField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('employeeid', models.IntegerField(db_column='EmployeeId', primary_key=True, serialize=False)),
                ('lastname', models.TextField(db_column='LastName')),
                ('firstname', models.TextField(db_column='FirstName')),
                ('title', models.TextField(blank=True, db_column='Title', null=True)),
                ('reportsto', models.IntegerField(blank=True, db_column='ReportsTo', null=True)),
                ('birthdate', models.DateTimeField(blank=True, db_column='BirthDate', null=True)),
                ('hiredate', models.DateTimeField(blank=True, db_column='HireDate', null=True)),
                ('address', models.TextField(blank=True, db_column='Address', null=True)),
                ('city', models.TextField(blank=True, db_column='City', null=True)),
                ('state', models.TextField(blank=True, db_column='State', null=True)),
                ('country', models.TextField(blank=True, db_column='Country', null=True)),
                ('postalcode', models.TextField(blank=True, db_column='PostalCode', null=True)),
                ('phone', models.TextField(blank=True, db_column='Phone', null=True)),
                ('fax', models.TextField(blank=True, db_column='Fax', null=True)),
                ('email', models.TextField(blank=True, db_column='Email', null=True)),
            ],
            options={
                'db_table': 'employees',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('genreid', models.IntegerField(db_column='GenreId', primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
            ],
            options={
                'db_table': 'genres',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InvoiceItems',
            fields=[
                ('invoicelineid', models.IntegerField(db_column='InvoiceLineId', primary_key=True, serialize=False)),
                ('invoiceid', models.IntegerField(db_column='InvoiceId')),
                ('trackid', models.IntegerField(db_column='TrackId')),
                ('unitprice', models.TextField(db_column='UnitPrice')),
                ('quantity', models.IntegerField(db_column='Quantity')),
            ],
            options={
                'db_table': 'invoice_items',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Invoices',
            fields=[
                ('invoiceid', models.IntegerField(db_column='InvoiceId', primary_key=True, serialize=False)),
                ('customerid', models.IntegerField(db_column='CustomerId')),
                ('invoicedate', models.DateTimeField(db_column='InvoiceDate')),
                ('billingaddress', models.TextField(blank=True, db_column='BillingAddress', null=True)),
                ('billingcity', models.TextField(blank=True, db_column='BillingCity', null=True)),
                ('billingstate', models.TextField(blank=True, db_column='BillingState', null=True)),
                ('billingcountry', models.TextField(blank=True, db_column='BillingCountry', null=True)),
                ('billingpostalcode', models.TextField(blank=True, db_column='BillingPostalCode', null=True)),
                ('total', models.TextField(db_column='Total')),
            ],
            options={
                'db_table': 'invoices',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MediaTypes',
            fields=[
                ('mediatypeid', models.IntegerField(db_column='MediaTypeId', primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
            ],
            options={
                'db_table': 'media_types',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Playlists',
            fields=[
                ('playlistid', models.IntegerField(db_column='PlaylistId', primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
            ],
            options={
                'db_table': 'playlists',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PlaylistTrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'playlist_track',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tracks',
            fields=[
                ('trackid', models.IntegerField(db_column='TrackId', primary_key=True, serialize=False)),
                ('name', models.TextField(db_column='Name')),
                ('albumid', models.IntegerField(blank=True, db_column='AlbumId', null=True)),
                ('mediatypeid', models.IntegerField(db_column='MediaTypeId')),
                ('genreid', models.IntegerField(blank=True, db_column='GenreId', null=True)),
                ('composer', models.TextField(blank=True, db_column='Composer', null=True)),
                ('milliseconds', models.IntegerField(db_column='Milliseconds')),
                ('bytes', models.IntegerField(blank=True, db_column='Bytes', null=True)),
                ('unitprice', models.TextField(db_column='UnitPrice')),
            ],
            options={
                'db_table': 'tracks',
                'managed': False,
            },
        ),
    ]