# Author: Olivia Jákli
# Example #5
# Clean a product description by removing HTML tags and character entities, and special characters.
import re


product_description = """
<div class="long-description">
    <p><strong>Amazing</strong> and&amp; creative  sample description of  a \
    product&trade; with <em>5-star***** reviews!!!</em></p>
</div>
"""

def clean_product_description(product_description):
    
    # Remove HTML tags.
    cleaned_description = re.sub(r'<[^>]+>', '', product_description)
    
    # Remove HTML character entities.
    cleaned_description = re.sub(r'&[a-zA-Z]+;', '', cleaned_description)
    
    # Remove special characters while keeping basic punctuation.
    cleaned_description = re.sub(r'[^\w\s.,!?-]', '', cleaned_description)
    
    # Normalize whitespace.
    cleaned_description = re.sub(r'\s+', ' ', cleaned_description).strip()
    
    return cleaned_description


print(clean_product_description(product_description))