from faker.providers import DynamicProvider
from faker import Faker

fashion_brand_names = DynamicProvider(
    provider_name = "fashion_brand",
    elements = [
        "Gucci", "Balenciaga", "Valentino", "Rick Owens",
        "Willy Chavarria", "Bottega Veneta", "Sacai", "Libertine"]
)

fake = Faker()

fake.add_provider(fashion_brand_names)

fake.fashion_brand()  # Return a random brand name from the list.


