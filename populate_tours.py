from tours.models import Tour

# Sample Tours Data
tours = [
    {
        "name": "New Zealand Highlights",
        "location": "New Zealand",
        "description": "Explore the breathtaking landscapes and vibrant cities of New Zealand.",
        "price": 2500.00,
    },
    {
        "name": "South Island Adventure",
        "location": "South Island, NZ",
        "description": "A thrilling adventure through the stunning South Island.",
        "price": 3000.00,
    },
    {
        "name": "North Island Explorer",
        "location": "North Island, NZ",
        "description": "Discover the unique culture and natural beauty of the North Island.",
        "price": 2700.00,
    },
    {
        "name": "Kiwi Wildlife Tour",
        "location": "Fiordland National Park",
        "description": "Experience the rich wildlife and pristine wilderness of New Zealand.",
        "price": 3200.00,
    },
    {
        "name": "Auckland City Tour",
        "location": "Auckland, NZ",
        "description": "A comprehensive tour of Auckland's iconic landmarks and hidden gems.",
        "price": 1500.00,
    },
]

# Create tours
for tour_data in tours:
    Tour.objects.create(
        name=tour_data["name"],
        location=tour_data["location"],
        description=tour_data["description"],
        price=tour_data["price"],
    )
