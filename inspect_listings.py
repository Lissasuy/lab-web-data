from bs4 import BeautifulSoup
with open('sample_listings.html', encoding='utf-8') as f:
    html = f.read()
    soup = BeautifulSoup(html, 'html.parser')

    for tag in soup.select('.price'):
        print(tag.text)

from lab_selectors import extract_listings

with open('sample_listings.html') as f:
    listings = extract_listings(f.read())
    
    for listing in listings:
        print(listing)

from lab_selectors import extract_listings
with open('sample_merchandise.html') as f:
    listings = extract_listings(f.read())
    
for listing in listings:
    print(listing['name'])

