import subprocess
import time
import pyautogui

def open_chrome_as_guest(video_url):
    try:
        # Membuka Chrome sebagai tamu, memutar video YouTube, dan mengatur autoplay, mute, dan loop
        subprocess.run(["google-chrome", "--guest", "--new-window", video_url], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def minimize_chrome():
    # Mencari proses Chrome dan mengirimkan sinyal untuk meminimalkan
    try:
        chrome_pid = int(subprocess.check_output(["pgrep", "chrome"]))
        os.kill(chrome_pid, signal.SIGUSR1)  # Mengirimkan sinyal untuk meminimalkan
    except (subprocess.CalledProcessError, ValueError):
        print("Error minimizing Chrome")

def resize_chrome(width, height):
    # Menyesuaikan ukuran jendela Chrome dengan menggunakan pyautogui
    pyautogui.hotkey('alt', 'space', 'r')  # Mengaktifkan menu jendela
    time.sleep(0.5)
    pyautogui.typewrite('s')  # Memilih opsi "Size"
    time.sleep(0.5)
    pyautogui.press('enter')  # Menjalankan perintah "Size"
    time.sleep(0.5)
    pyautogui.typewrite(f"{width},{height}")  # Menulis ukuran yang diinginkan
    time.sleep(0.5)
    pyautogui.press('enter')  # Menjalankan perintah "Size"

def read_youtube_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

if __name__ == "__main__":
    # Gantilah dengan nama file yang berisi daftar URL video YouTube
    file_path = "yt_list.txt"
    
    # Mengatur ukuran jendela Chrome
    resize_chrome(300, 100)

    while True:
        # Membaca daftar URL dari file
        youtube_urls = read_youtube_urls_from_file(file_path)

        # Memeriksa apakah daftar URL kosong
        if not youtube_urls:
            print("Daftar URL kosong. Mulai dari awal.")
            continue

        # Melakukan perulangan setiap 30 detik sebanyak 5 kali
        for url in youtube_urls:
            minimize_chrome()  # Meminimalkan jendela Chrome sebelum membuka URL berikutnya
            url_with_params = f"{url.strip()}&autoplay=1&mute=1&loop=1"
            open_chrome_as_guest(url_with_params)  # Menghapus karakter newline dan spasi ekstra
            time.sleep(30)  # Menunggu 30 detik sebelum iterasi selanjutnya

        # Setelah selesai membaca seluruh daftar, kembali ke awal
        print("Selesai membaca daftar. Mulai dari awal.")
