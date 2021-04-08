from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('log-level=2')
chrome_options.add_argument("force-device-scale-factor=0.75");
chrome_options.add_argument("high-dpi-support=0.75");

path = 'D:\Data Science\Spyder\Web Scrapping\chromedriver.exe'
driver = webdriver.Chrome(path, options=chrome_options)

url =' https://shopee.co.id/Pakaian-Pria-cat.33?page=0&sortBy=sales'

page=1
links = []
while True:
    if page <=50:
        try:
            driver.get(url)
            time.sleep(8)
            driver.implicitly_wait(30)
            driver.execute_script('window.scrollTo(0, 1500);')
            driver.implicitly_wait(30)
            driver.execute_script('window.scrollTo(0, 3500);')
            driver.implicitly_wait(30)
            soup_a = BeautifulSoup(driver.page_source, 'html.parser')
            products = soup_a.find('div', class_='row shopee-search-item-result__items')
            for link in products.find_all('a'):
                links.append(link.get('href'))
        except:
                print('gagal cok')
    
        try:
            driver.find_element_by_css_selector('[class="shopee-icon-button shopee-icon-button--right "]').click()
            url = 'https://shopee.co.id/Pakaian-Pria-cat.33?page={}&sortBy=sales'.format(page)
            print('page ' + str(page))
            page+=1
        except: 
            print('udah nih')
            break
    else:
        print('dapet ' + str(len(links)) + ' links')
        break
  
data = pd.DataFrame({'nama':[''], 'kategori':[''], 'jenis':[''], 'lokasi':[''], 'harga':[''], 
                     'terjual':[''], 'rating':[''],'jumlah_review':[''], 
                     'toko':[''], 'n_produk_toko':[''], 'umur_toko':[''], 'pengikut_toko':['']})    
progres = 1
gagal = 1  

for link in links:
    try:
        url = 'http://www.shopee.co.id' + link
        driver.get(url)
        time.sleep(5)
        driver.execute_script('window.scrollTo(0, 500);')
        driver.implicitly_wait(30)
        WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'attM6y')))
        soup_b = BeautifulSoup(driver.page_source, 'html.parser')
        nama = soup_b.find('div', class_='attM6y').text
        kategori = soup_b.find_all('a', class_='_3YDLCj')[2].text
        lokasi = soup_b.find_all('div', class_='aPKXeO')[-1].text
        harga = soup_b.find('div', class_='_3e_UQT').text
        terjual = soup_b.find('div', class_='aca9MM').text
        rating = soup_b.find('div', class_='OitLRu _1mYa1t').text    
        n_review = soup_b.find_all('div', class_='OitLRu')[-1].text
        toko = soup_b.find('div', class_='_3uf2ae').text
        n_produk = soup_b.find_all('span', class_='zw2E3N _2fK6RA')[1].text
        umur = soup_b.find_all('span', class_='zw2E3N')[-2].text
        pengikut = soup_b.find_all('span', class_='zw2E3N')[-1].text
        try:
            jenis = soup_b.find_all('a', class_='_3YDLCj')[3].text
        except:
            jenis = None
        data = data.append({'nama':nama, 'kategori':kategori, 'jenis':jenis, 'lokasi':lokasi, 'harga':harga, 
                            'terjual':terjual, 'rating':rating,'jumlah_review':n_review, 'toko':toko,
                            'n_produk_toko':n_produk, 'umur_toko':umur, 'pengikut_toko':pengikut}, ignore_index=True)
        print('berhasil ' + str(progres) + '/' + str(len(links)))
        progres +=1
    except:
        print('gagal ' + str(gagal))
        gagal +=1
        pass

data = data.iloc[1:]
#data.to_csv('pakaian_pria_shopee_sales_6421.csv', index=False)
