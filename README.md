# Exploratory Data Analysis

## Descriptive Statistics
- Kolom Reached.on.Time_Y.N seharusnya data type nya adalah object (boolean) karena variabel tersebut merupakan data kategorik yang mengartikan nilai 1 adalah no dan nilai 0 adalah yes.

- Tidak ada kolom yang memiliki nilai kosong, dapat dilihat dari output di atas bahwa seluruh kolom memiliki jumlah baris yang sama dengan jumlah data yaitu 10.999 baris/data.

- Kolom yang memiliki summary aneh:
    - Kolom Weight in gms memiliki selisih nilai mean dan median yang cukup jauh yaitu sebesar 515 yang mengartikan bahwa variabel tersebut memiliki outlier/pencilan.
    - Kolom Mode_of_Shipment memiliki distribusi yang terlalu timpang karena nilai kategori Ship mendominasi, hal tersebut menyebabkan feature tidak akan terlalu berguna dalam klasifikasi
    - Kolom Discount_offered memiliki selisih nilai mean dan median yang cukup jauh yaitu sebesar 9 yang mengartikan bahwa variabel tersebut memiliki outlier/pencilan. Selain itu dapat dilihat dari nilai min 1 dengan max 65 kalau dilihat rata-rata hanya 13 saja

## Univariate Analysis
- Warehouse Block: Persebaran pesanan pada blok A, B, C, D cukup merata sementara blok F memiliki jumlah pesanan yang jauh lebih besar yg bisa mencapai kurang lebih 2x lipat pesana di blok yang lain.

- Mode of Shipment : Mode pengirimin mengggunakan tarnsaportasi udara dan darat memiliki jumlah yang serupa sementara moda pengiriminan menggunakan transporatsi laut memiliki jumlah yang jauh lebih besar yaitu mencapai 4 x lipat dari moda pengiriman lainnya.

- Sekitar 68% keterlambatan pengiriman disebabkan karena kapal digunakan sebagai moda pengiriman. Jadi, opsi alternatif seperti layanan Penerbangan dan Jalan dapat dipertimbangkan untuk mengurangi keterlambatan pengiriman

- Persentase pengiriman tertunda yang lebih tinggi dicatat di Gudang blok F sebesar 33%.

- Pemberian rating oleh pelanggan miliki sebaran data yang mirip. Hampir 20% dari total pengiriman menerima rating 5

- Product Importance: low imporatnce dan medium importance menjadi data yg mayoritas sedangkan high importance menjadi data yg minoritas

- Gender: Kedua kelas seimbang.

- Customer Care Calls: Distribusi positively skewed dengan modus 4.

- Customer Rating:uniform distribution.

- Prior purchases: Positively skewed dengan modus 3.

- Discount Offered: Dipisahkan menjadi 2 uniform distribution: 0 hingga 10 merupakan nilai mayoritas dan kemudian nilai minoritas lebih besar dari 10 hingga 65.

- Weight in gms: terbagi jadi 3 zona: tinggi dari 1000 hingga 2000 dan dari 4000 hingga 6000. Rendah dari 2000 hingga 4000.

## Multivariate Analysis
- Insight yang menarik dapat dilihat bahwa discount dan ketepatan waktu sampainya barang saling berkorelasi, dimana semakin besar discount yang ditawarkan semakin tinggi kemungkinan barang samapi tidak tepat waktu.

- Biaya produk dan panggilan layanan pelanggan saling berkorelasi, dimana jika pelanggan kita membayar lebih banyak uang untuk produk, mereka cenderung memiliki lebih banyak melakukan customer care calls.

## Business Insight
- The data shown that 59.67% orders were not reached on time, while 40.33% of the orders were reached on time.

- Many orders were reached late on range 2000 - 4000 grams. Most orders that do not reached on time are orders with a weight in the range of 1250 - 4000 grams, at that weight the proportion that does not reached on time exceeds 90% compared to orders that reached on time

- 100% Orders with Discount Above 10% are late. This indicates that offered discount and orders that reached on time have a correlation each other. This may happen because of the amount of orders coming to warehouse increase significantly during discount season.