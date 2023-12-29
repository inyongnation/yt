import os
import platform
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def install_selenium():
    subprocess.run(["pip", "install", "selenium"])

def download_and_extract_chromedriver():
    platform_name = platform.system().lower()
    
    if platform_name == "linux":
        # Unduh ChromeDriver
        subprocess.run(["wget", "https://chromedriver.storage.googleapis.com/LATEST_RELEASE/chromedriver_linux64.zip"])
        # Ekstrak ChromeDriver
        subprocess.run(["unzip", "chromedriver_linux64.zip", "-d", "/usr/local/bin/"])
        # Hapus file zip setelah diekstrak
        subprocess.run(["rm", "chromedriver_linux64.zip"])

def open_youtube_video():
    # Buat objek ChromeOptions
    chrome_options = Options()

    # Aktifkan mode kiosk untuk layar penuh
    chrome_options.add_argument("--kiosk")

    try:
        while True:
            # Buat objek WebDriver dengan opsi yang telah ditentukan
            driver = webdriver.Chrome(options=chrome_options)

            # Buka halaman YouTube dengan URL yang diberikan
            youtube_url = "https://www.youtube.com/watch?v=RsRvi7YKG-8&t=4s&autoplay=1"
            driver.get(youtube_url)

            # Biarkan video berjalan selama beberapa saat
            import time
            time.sleep(600)

            # Tutup peramban ketika selesai
            driver.quit()

    except KeyboardInterrupt:
        # Tangkap penekanan Ctrl+C untuk keluar dari loop
        pass

if __name__ == "__main__":
    try:
        # Coba impor Selenium
        import selenium
    except ImportError:
        # Jika Selenium belum terinstal, instalkan
        install_selenium()

    # Cek jika ChromeDriver sudah ada
    if not os.path.isfile("/usr/local/bin/chromedriver"):
        # Jika belum, unduh dan ekstrak ChromeDriver
        download_and_extract_chromedriver()

    # Setelah instalasi dan pengunduhan selesai, jalankan skrip utama
    open_youtube_video()
