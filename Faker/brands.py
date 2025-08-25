from faker import Faker
from faker.providers import DynamicProvider
import pandas as pd
import random

def generate_brand_names():
    # Define a custom list of fashion brand names.
    fashion_brand_names = DynamicProvider(
        provider_name = "fashion_brand",
        elements = [
            "Gucci", "Balenciaga", "Valentino", "Rick Owens",
            "Willy Chavarria", "Bottega Veneta", "Sacai", "Libertine",
            "Alaia", "Saint Laurent", "Aya Muse", "Dries Van Noten",
            "Givenchy", "Maison Margiela", "Erdem", "Kelly Cole",
            "Marni", "Gallery Dept", "Nahmias", "Tom Ford"
            ]
    )

    fake = Faker()

    fake.add_provider(fashion_brand_names)

    # Return a unique, random brand name from the list.
    names = [fake.unique.fashion_brand() for _ in range(15)]
    assert len(set(names)) == len(names), "Duplicate brand names found!"
    return names


def generate_inventory_data(num_records, min_received=1, max_received=100):
    units_received = [random.randint(min_received, max_received) for _ in range(num_records)]
    units_sold = [random.randint(0, received) for received in units_received]
    return units_received, units_sold

received, sold = generate_inventory_data(15)

data = {
    'brand_name': generate_brand_names(),
    'units_received': received,
    'units_sold': sold,
    'investment': [random.randint(1000, 10000) for _ in range(15)],
    'revenue': [random.randint(2000, 20000) for _ in range(15)]
}

df_faker = pd.DataFrame(data)

print(df_faker)
df_faker.to_csv('fashion_brands.csv', index=False)
print("DataFrame saved to 'fashion_brands.csv'.")


