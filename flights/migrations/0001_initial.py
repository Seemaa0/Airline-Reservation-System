# Generated by Django 4.2.7 on 2023-11-02 08:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import flights.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aircraft_type', models.CharField(max_length=50)),
                ('seating_capacity', models.PositiveIntegerField()),
                ('manufacturer', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_percentage', models.BooleanField(default=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('min_tickets', models.PositiveIntegerField(default=1)),
                ('min_flights', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='FamilyMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_number', models.CharField(max_length=10)),
                ('departure_airport', models.CharField(max_length=3)),
                ('arrival_airport', models.CharField(max_length=3)),
                ('available_seats', models.PositiveIntegerField()),
                ('ticket_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField(validators=[flights.models.Flight.arrival_time_must_be_after_departure_time])),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('passport_number', models.CharField(max_length=15)),
                ('date_of_birth', models.DateField()),
                ('frequent_flyer_number', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_date', models.DateTimeField()),
                ('seat_number', models.CharField(max_length=5)),
                ('is_paid', models.BooleanField(default=False)),
                ('family_members', models.ManyToManyField(blank=True, to='flights.familymember')),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.flight')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(choices=[('credit_card', 'Credit Card'), ('debit_card', 'Debit Card'), ('cash', 'Cash'), ('paypal', 'PayPal')], max_length=20)),
                ('payment_date', models.DateTimeField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('reservation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='flights.reservation')),
            ],
        ),
        migrations.CreateModel(
            name='AirportConnection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connecting_flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.flight')),
                ('destination_airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination_connections', to='flights.airport')),
                ('source_airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_connections', to='flights.airport')),
            ],
        ),
    ]
