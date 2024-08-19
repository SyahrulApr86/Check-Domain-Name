import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Menginstal ChromeDriver yang kompatibel secara otomatis
chromedriver_autoinstaller.install()

# Mengatur opsi untuk mode headless
chrome_options = Options()
chrome_options.add_argument("--headless")  # Menjalankan secara headless
chrome_options.add_argument("--disable-gpu")  # Mengurangi penggunaan GPU
chrome_options.add_argument("--no-sandbox")  # Mencegah masalah izin
chrome_options.add_argument("--disable-dev-shm-usage")  # Menghindari masalah memori bersama

# Membuat instance driver dengan opsi headless
driver = webdriver.Chrome(options=chrome_options)

# Membaca TLD dari file
with open('tlds.txt', 'r') as file:
    tlds = [line.strip().lower() for line in file]

# File output untuk menyimpan TLD yang tersedia dan tidak tersedia
available_tlds_file = open('available_tlds.txt', 'w')
not_available_tlds_file = open('not_available_tlds.txt', 'w')

try:
    for tld in tlds:
        domain_name = f"rul.{tld}"
        print(f"Checking {domain_name}... ", end='')

        # Buka halaman Niagahoster
        driver.get("https://www.niagahoster.co.id/domain-murah")

        # Tunggu sampai elemen input dimuat
        time.sleep(3)  # Bisa diganti dengan eksplisit wait jika diperlukan

        # Temukan elemen input untuk nama domain
        search_input = driver.find_element(By.ID, "h-domain-finder-header-input")

        # Masukkan nama domain yang ingin dicek
        search_input.send_keys(domain_name)

        # Tekan Enter untuk submit
        search_input.send_keys(Keys.RETURN)

        # Tunggu beberapa saat sampai halaman selesai memuat
        time.sleep(5)

        # Periksa apakah teks yang menunjukkan domain tersedia ada di halaman
        if "Selamat! Domain yang Anda Cari Tersedia" in driver.page_source:
            print("[+] Tersedia")
            available_tlds_file.write(domain_name + '\n')
        else:
            print("[x] Tidak Tersedia")
            not_available_tlds_file.write(domain_name + '\n')
finally:
    # Tutup browser
    driver.quit()
    available_tlds_file.close()
    not_available_tlds_file.close()
