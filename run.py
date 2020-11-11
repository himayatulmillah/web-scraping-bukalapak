import requests
import csv
from bs4 import BeautifulSoup

key = input('Masukkan keyword : ')
write = csv.writer(open('results/{}.csv'.format(key), 'w', newline=''))
header = ['Nama', 'Harga', 'Stok', 'Rating', 'Kondisi', 'Deskripsi', 'Kategori', 'Rilis', 'Kota', 'Provinsi']
write.writerow(header)

url = 'https://api.bukalapak.com/multistrategy-products'
for page in range(1,11):
    parameter = {
        'prambanan_override': True,
        'keywords': key,
        'limit': 50,
        'offset': 50,
        'page': page,
        'facet': True,
        'access_token': 'SOL1DrmPvC7sHmnmLlsn3saXrd3688DxGy5h9PtUvbAbHg'
    }

    r = requests.get(url, params=parameter).json()

    # get product field
    products = r['data']

    # collect product info
    for p in products:
        nama = p['name']
        harga = p['price']
        stok = p['stock']
        rating = p['rating']['average_rate']
        kondisi = p['condition']
        deskripsi = BeautifulSoup(p['description']).get_text()
        kategori = p['category']['structure']
        rilis = p['relisted_at']
        kota = p['store']['address']['city']
        provinsi = p['store']['address']['province']
        write = csv.writer(open('results/{}.csv'.format(key), 'a', newline=''))
        data = [nama, harga, stok, rating, kondisi, deskripsi, kategori, rilis, kota, provinsi]
        write.writerow(data)