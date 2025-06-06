# Author: Olivia Jákli
# Example #3 for Medium article on real-world use cases for regular expressions.
import re

product_description = """
<div class="long-description">
    <p><strong>Amazing</strong> sample description of an overpriced product with <em>5-star reviews!!!</em></p>
</div>
"""

# Remove HTML tags.
cleaned_description = re.sub(r'<[^>]+>', '', product_description)

# Replace HTML character entities.
cleaned_description = re.sub(r'&[a-ZA-Z]', '', cleaned_description)

# Remove special characters while keeping basic punctuation.
cleaned_description = re.sub(r'[^\w\s.,!?-]', '', cleaned_description)

# Normalize whitespace.
cleaned_description = re.sub(r'\s+', ' ', cleaned_description).strip()

print(cleaned_description)