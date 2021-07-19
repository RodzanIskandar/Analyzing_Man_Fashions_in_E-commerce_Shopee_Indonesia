# Analyzing Man Fashions in E-commerce Shopee Indonesia
## Overview
This projects idea based on customers and seller response about  regulatory delivering system change by Shopee Indonesia in their e-commerce system who encourage some of the user to swicth the platform. [here is one of the viral threads in Twitter](https://twitter.com/ariefghozaly/status/1378040256348319744). the main idea is to get a bigger picture of man's fashion market in shopee Indonesia and compare it with another e-commerce platform to see the market opprtunity within the same category. I am scraped over 2000 product postings in sales man's fashion from [https://shopee.co.id/Pakaian-Pria-cat.33?page=0&sortBy=sales](https://shopee.co.id/Pakaian-Pria-cat.33?page=0&sortBy=sales) and answering some questions like what is the suitable sub-category market for newcomers in Shopee Indonesia?, what is the most effective store? etc.

- Scraped over 2000 man's fashion porduct on April 6, 2021 using Selenium and BeautifulSoup

## Code and Resource Used
**Python Version:** 3.7.9

**Packages:** Selenium, BeautifulSoup, Numpy, Pandas, Matplotlib, Seaborn

**Scraper Reference:** [https://nixpoin.com/python/scraping-shopee-dengan-python/](https://nixpoin.com/python/scraping-shopee-dengan-python/)

**Convert K or M to Integer thousand or Miliion Python:** [https://gist.github.com/gajeshbhat/67a3db79a6aecd1db42343190f9a2f17](https://gist.github.com/gajeshbhat/67a3db79a6aecd1db42343190f9a2f17)

## Web Scraping
Scrape over 2000 product postings in sales man's fashion from [https://shopee.co.id/Pakaian-Pria-cat.33?page=0&sortBy=sales](https://shopee.co.id/Pakaian-Pria-cat.33?page=0&sortBy=sales) With each post got the following:
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

## Data Cleaning
After scraping, I needed to clean it up so the data was usable for the next step, which is Exploratory Data Analysis (EDA). here some changes that i made:
- parsed city or district out of lokasi(location) column
- removed rows without price
- transformed price range to average price and add the value in harga_rata2(average price) column
- transformed RB(K) or JT(M) to integer thousand or million in terjual(sales), n_review(number of reviews), n_produk(number of products) and pengikut_toko(followers) columns
- transformed umur(age) into integer in months unit
- replaced shopee value in jenis(sub-category) column into None
- check and droped the duplicated table

## Exploratory Data Analysis (EDA)
Here I am answering my questions to fulfill the main idea, here are those question:
1. what is the most sales in sub-category market? What is the suitable sub-category market for newcomers in Shopee Indonesia?
2. what is the most effective store?
3. What is the most popular store and what products are they sell?

and also I am looked up at the distribution data and the correlation between the data with visualization. 
Below are a few highlights from the EDA

![](https://github.com/RodzanIskandar/analyzing_man_fashions_in_e-commerce_Shopee_Indonesia/blob/main/images/cat%20to%20sales.png) 

