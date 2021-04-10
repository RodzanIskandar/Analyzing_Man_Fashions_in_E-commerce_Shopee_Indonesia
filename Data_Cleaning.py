import pandas as pd

data1 = pd.read_csv('pakaian_pria_shopee_sales_1_6421.csv')
data2 = pd.read_csv('pakaian_pria_shopee_sales_2_6421.csv')
data3 = pd.read_csv('pakaian_pria_shopee_sales_3_6421.csv')
data4 = pd.read_csv('pakaian_pria_shopee_sales_4_6421.csv')
data5 = pd.read_csv('pakaian_pria_shopee_sales_5_6421.csv')

df = pd.concat([data1,data2,data3,data4,data5], ignore_index=True)

#df.to_csv('pakaian_pria_shopee_sales_6421.csv', index=False)

#lokasi parsing
kota = df['lokasi'].apply(lambda x: x.split('-')[0])
simp_kota = kota.apply(lambda x: x.lower().replace('dikirim darikota ', '').replace('dikirim darikab. ', ''))
df['lokasi'] = simp_kota

#harga
df = df[df['harga'].notna()]
min_rp = df['harga'].apply(lambda x: x.replace('Rp', ''))
df['harga_min'] = min_rp.apply(lambda x: int(x.split('-')[0].replace('.','')))
df['harga_max'] = min_rp.apply(lambda x: int(x.split('-')[1].replace('.','') if '-' in x else x.split('-')[0].replace('.','')))
df['harga_rata2'] = (df.harga_max+df.harga_min)/2

#RB, RB+, JT pada kolom terjual, jumlah_review, n_produk, pengikut_toko   #referensi: https://gist.github.com/gajeshbhat/67a3db79a6aecd1db42343190f9a2f17
def convert_str_to_number(x):
    total_stars = 0
    num_map = {'RB':1000, 'RB+':1000, 'JT':1000000}
    if x.isdigit():
        total_stars = int(x)
    else:
        if ',' in x:
            total_stars = float(x.replace(',','.')[:-2]) * num_map.get(x[-2:].upper())
        elif 'RB+' in x:
            total_stars = float(x[:-3]) * num_map.get(x[-3:].upper())
        else:
            total_stars = float(x[:-2]) * num_map.get(x[-2:].upper())
            
    return int(total_stars)

terjual_min_rp = []
for x in df['terjual']:
    min_rp = convert_str_to_number(x)
    terjual_min_rp.append(min_rp)
    
n_review_min_rp = []
for x in df['jumlah_review']:
    min_rp = convert_str_to_number(x)
    n_review_min_rp.append(min_rp)
    
n_produk_min_rp = []
for x in df['n_produk_toko']:
    min_rp = convert_str_to_number(x)
    n_produk_min_rp.append(min_rp)
    
follower_min_rp = []
for x in df['pengikut_toko']:
    min_rp = convert_str_to_number(x)
    follower_min_rp.append(min_rp)

df['terjual'] = terjual_min_rp
df['jumlah_review'] = n_review_min_rp
df['n_produk_toko'] = n_produk_min_rp
df['pengikut_toko'] = follower_min_rp

#umur parsing
def convert_umur(x):
    jml_bulan = 0
    if 'bulan lalu' in x:
        jml_bulan = int(x.split(' ')[0])
    else:
        jml_bulan = int(x.split(' ')[0])*12
        
    return jml_bulan

umur = [] 
for x in df['umur_toko']:
    thn_bln = convert_umur(x)
    umur.append(thn_bln)
    
df['umur_bulan_toko'] = umur

#fix shopee di kolom jenis
min_shopee = df['jenis'].apply(lambda x: x.lower().replace('shopee', 'NaN'))
df['jenis'] = min_shopee

#ambil tabel yang diperlukan
df = df[['nama', 'kategori', 'jenis', 'lokasi', 'harga_rata2', 'terjual', 
         'rating', 'jumlah_review', 'toko', 'umur_bulan_toko', 'n_produk_toko',
         'pengikut_toko']]

#cek duplicate
cek_dup = df[df.duplicated(subset=['nama', 'toko'], keep=False)]
df = df.drop_duplicates(subset=['nama', 'toko'], keep='last')

#df.to_csv('pakaian_pria_shopee_sales_cleaning.csv', index=False)
