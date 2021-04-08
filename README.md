# pakaian_pria_shopee
analyzing fashion for men in e-commerce Shopee Indonesia from web scrapping process to Exploratory Data Analysis. 

This projects idea based on customers and seller response about  regulatory delivering system change by Shopee Indonesia in their e-commerce system who encourage some of the user to swicth the platform. [here is one of the viral threads in Twitter](https://twitter.com/ariefghozaly/status/1378040256348319744). the main idea is to get a bigger picture of man's fashion market in shopee Indonesia and compare it with another e-commerce platform to see the market opprtunity within the same category 

- Scraped over 2000 man's fashion porduct on April 6, 2021 using Selenium and BeautifulSoup

# Code and Resource Used
**Python Version:** 3.7.9

**Packages:** Selenium, BeautifulSoup, Numpy, Pandas, Matplotlib, Seaborn

**Scraper Reference:** [https://nixpoin.com/python/scraping-shopee-dengan-python/](https://nixpoin.com/python/scraping-shopee-dengan-python/)

# Web Scraping
scrape over 2000 product postings in man's fashion from [https://shopee.co.id/Pakaian-Pria-cat.33](https://shopee.co.id/Pakaian-Pria-cat.33) With each post got the following:
1. nama = name of product
2. Kategori = The category of the product
3. jenis = more detail in the category section
4. lokasi = the store location
5. harga = the product's price
6. terjual = the sales
7. rating
8. jumlah_review = number of reviews
9. toko = the store's name
10. n_produk_toko = number of the products in the particular store
11. umur_toko = the store's age
12. pengikut_toko = the store's follower
