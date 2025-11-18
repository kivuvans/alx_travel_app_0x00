from django.core.management.base import BaseCommand
from faker import Faker
from random import randint
from listings.models import Listing, Booking, Review
from datetime import timedelta, date
import random

fake = Faker()

class Command(BaseCommand):
    help = "Seed the database with sample listings, bookings, and reviews"

    def handle(self, *args, **kwargs):

        # Clear existing data
        Review.objects.all().delete()
        Booking.objects.all().delete()
        Listing.objects.all().delete()

        # Seed Listings
        listings = []
        for _ in range(10):
            listing = Listing.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.text(),
                location=fake.city(),
                price_per_night=randint(50, 500),
                host_name=fake.name(),
            )
            listings.append(listing)

        # Seed Bookings
        for _ in range(20):
            listing = random.choice(listings)
            check_in = fake.date_between(start_date="-1y", end_date="today")
            check_out = check_in + timedelta(days=randint(1, 10))
            Booking.objects.create(
                listing=listing,
                guest_name=fake.name(),
                check_in=check_in,
                check_out=check_out,
                total_price=randint(100, 3000)
            )

        # Seed Reviews
        for _ in range(30):
            listing = random.choice(listings)
            Review.objects.create(
                listing=listing,
                reviewer_name=fake.name(),
                rating=randint(1, 5),
                comment=fake.paragraph()
            )

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))
