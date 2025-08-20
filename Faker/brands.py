from faker import Faker
from faker.providers import DynamicProvider
import pandas as pd

fashion_brand_names = DynamicProvider(
    provider_name = "fashion_brand",
    elements = [
        "Gucci", "Balenciaga", "Valentino", "Rick Owens",
        "Willy Chavarria", "Bottega Veneta", "Sacai", "Libertine",
        "Alaia", "Saint Laurent", "Aya Muse", "Dries Van Noten",
        "Givenchy", "Maison Margiela", "Kelly Cole"]
)

fake = Faker()

fake.add_provider(fashion_brand_names)

# Return a unique, random brand name from the list.
names = [fake.unique.fashion_brand() for _ in range(10)]
assert len(set(names)) == len(names), "Duplicate brand names found!"

num_records = 10

data = {
    'brand_name': names,
    'units_sold': [fake.random_int(min=0, max=100) for _ in range(num_records)],
    'units_received': [fake.random_int(min=1, max=100) for _ in range(num_records)]
}

df_faker = pd.DataFrame(data)

print(df_faker)
df_faker.to_csv('fashion_brands.csv', index=False)
print("DataFrame saved to 'fashion_brands.csv'.")


