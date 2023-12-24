import subprocess
import time

def open_chrome_as_guest(video_url):
    try:
        # Membuka Chrome sebagai tamu, memutar video YouTube, dan mengatur autoplay, mute, dan loop
        subprocess.run(["google-chrome", "--guest", "--new-window", video_url], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def read_youtube_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

if __name__ == "__main__":
    # Gantilah dengan nama file yang berisi daftar URL video YouTube
    file_path = "yt_list.txt"
    
    # Membaca daftar URL dari file
    youtube_urls = read_youtube_urls_from_file(file_path)
    
    # Melakukan perulangan setiap 5 detik sebanyak 5 kali
    for url in youtube_urls:
        url_with_params = f"{url.strip()}&autoplay=1&mute=1&loop=1"
        open_chrome_as_guest(url_with_params)  # Menghapus karakter newline dan spasi ekstra
        time.sleep(5)  # Menunggu 5 detik sebelum iterasi selanjutnya
