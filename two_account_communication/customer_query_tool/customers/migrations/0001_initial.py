# Generated by Django 2.2.3 on 2021-02-17 15:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountBalance',
            fields=[
                ('account_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('currency', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_type', models.CharField(max_length=50)),
                ('discount_value', models.IntegerField()),
                ('discount_description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LatLong',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=8)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('NaPTAN', models.CharField(max_length=50)),
                ('other', models.CharField(max_length=50)),
                ('other_type', models.CharField(max_length=50)),
                ('accuracy', models.IntegerField()),
                ('lat_long', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='customers.LatLong')),
            ],
        ),
        migrations.CreateModel(
            name='LocationFrom',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('NaPTAN', models.CharField(max_length=50)),
                ('other', models.CharField(max_length=50)),
                ('other_type', models.CharField(max_length=50)),
                ('accuracy', models.IntegerField()),
                ('lat_long', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location_from', to='customers.LatLong')),
            ],
        ),
        migrations.CreateModel(
            name='LocationTo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('NaPTAN', models.CharField(max_length=50)),
                ('other', models.CharField(max_length=50)),
                ('other_type', models.CharField(max_length=50)),
                ('accuracy', models.IntegerField()),
                ('lat_long', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location_to', to='customers.LatLong')),
            ],
        ),
        migrations.CreateModel(
            name='Mode',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('short_desc', models.CharField(max_length=50)),
                ('long_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Monetary_Value',
            fields=[
                ('money_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('currency', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('homepage', models.URLField()),
                ('api_url', models.URLField()),
                ('default_language', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('modes', models.ManyToManyField(blank=True, to='customers.Mode')),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=50)),
                ('reference_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(max_length=100)),
                ('unit', models.CharField(max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service', to='customers.Monetary_Value')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('number_usages', models.IntegerField()),
                ('reference', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('reference_type', models.CharField(max_length=50)),
                ('medium', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TravelLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('reference', models.CharField(max_length=100)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='travel_location', to='customers.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('included', models.CharField(max_length=3)),
                ('reference', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('vehicle_type', models.CharField(max_length=50)),
                ('condition', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usage',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('travel_class', models.CharField(max_length=50)),
                ('purchase_id', models.CharField(max_length=50)),
                ('usage_date_time', models.DateTimeField()),
                ('route_via_avoid', models.CharField(max_length=50)),
                ('pre_paid', models.BooleanField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usage', to='customers.Customer')),
                ('mode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usage', to='customers.Mode')),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usage', to='customers.Operator')),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usage', to='customers.Monetary_Value')),
                ('reference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usage', to='customers.Reference')),
                ('services', models.ManyToManyField(related_name='usage', to='customers.Service')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usage', to='customers.Ticket')),
                ('travel_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usage_from', to='customers.TravelLocation')),
                ('travel_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usage_to', to='customers.TravelLocation')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('date_time', models.DateTimeField()),
                ('reference', models.CharField(max_length=4, primary_key=True, serialize=False, unique=True)),
                ('payment_type', models.CharField(max_length=10)),
                ('payment_method', models.CharField(max_length=50)),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction', to='customers.Monetary_Value')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('travel_class', models.CharField(max_length=50)),
                ('booking_date_time', models.DateTimeField()),
                ('agent', models.CharField(max_length=50)),
                ('passenger_number', models.IntegerField()),
                ('passenger_type', models.CharField(max_length=100)),
                ('route', models.CharField(max_length=100)),
                ('travel_from_date_time', models.DateTimeField()),
                ('travel_to_date_time', models.DateTimeField()),
                ('conditions', models.CharField(max_length=50)),
                ('concession', models.CharField(max_length=50)),
                ('restrictions', models.CharField(max_length=50)),
                ('reserved_position', models.CharField(max_length=50)),
                ('service_request', models.CharField(max_length=100)),
                ('account_balance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase', to='customers.AccountBalance')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase', to='customers.Customer')),
                ('location_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase', to='customers.LocationFrom')),
                ('location_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase', to='customers.LocationTo')),
                ('mode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase', to='customers.Mode')),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase', to='customers.Operator')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase', to='customers.Ticket')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase', to='customers.Transaction')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase', to='customers.Vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='LinkedAccount',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('operator', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('token', models.CharField(max_length=100)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LinkedAccount', to='customers.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Concession',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('valid_from_date_time', models.DateTimeField()),
                ('valid_to_date_time', models.DateTimeField()),
                ('conditions', models.CharField(max_length=100)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='concession', to='customers.Customer')),
                ('discount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='concession', to='customers.Discount')),
                ('mode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='concession', to='customers.Mode')),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='concession', to='customers.Operator')),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='concession', to='customers.Monetary_Value')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='concession', to='customers.Transaction')),
            ],
        ),
    ]
