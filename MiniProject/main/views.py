from django.shortcuts import render


products = [
    {
        'id': 1,
        'name': 'iPhone 13',
        'description': 'The latest iPhone with A15 Bionic chip.',
        'price': 799.00,
        'image': 'https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/iphone-13-key-features-2022?wid=1200&hei=630&fmt=jpeg&qlt=95&.v=1631810182000',
    },
    {
        'id': 2,
        'name': 'MacBook Pro',
        'description': 'Powerful laptop with M1 chip.',
        'price': 1299.00,
        'image': 'https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/mbp13touch-silver-select-202011_GEO_US?wid=904&hei=840&fmt=jpeg&qlt=90&.v=1603406905000',
    },
    {
        'id': 3,
        'name': 'iPad Air',
        'description': 'The new iPad Air with A14 Bionic chip.',
        'price': 599.00,
        'image': 'https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/ipad-air-select-wifi-green-202009?wid=940&hei=1112&fmt=png-alpha&.v=1598650647000',
    },
    {
        'id': 4,
        'name': 'Apple Watch Series 7',
        'description': 'The latest Apple Watch with larger display.',
        'price': 399.00,
        'image': 'https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/MKU63_VW_34FR+watch-44-alum-silver-nc-7s_VW_34FR_WF_CO_GEO_KR?wid=512&hei=512&fmt=jpeg&qlt=95&.v=1629920018000',
    },
    # Add more products as needed
]

def home_view(request):
    product_id = request.GET.get('product_id')
    search_query = request.GET.get('q', '')
    if product_id:
        product = next((p for p in products if p['id'] == int(product_id)), None)
        return render(request, 'main/product_detail.html', {'product': product})
    if search_query:
        filtered_products = [p for p in products if search_query.lower() in p['name'].lower()]
    else:
        filtered_products = products
    return render(request, 'main/home.html', {'products': filtered_products, 'search_query': search_query})


def contact_view(request):
    return render(request, 'main/contact.html')


