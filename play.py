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
    
    # Melakukan perulangan setiap 30 detik sebanyak 5 kali
    for url in youtube_urls:
        open_chrome_as_guest(url.strip())  # Menghapus karakter newline dan spasi ekstra
        time.sleep(30)  # Menunggu 30 detik sebelum iterasi selanjutnya
