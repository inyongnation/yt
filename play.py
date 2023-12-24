import subprocess

def open_chrome_as_guest(video_url):
    try:
        # Membuka Chrome sebagai tamu, memutar video YouTube, dan mengatur autoplay dan mute
        subprocess.run(["google-chrome", "--guest", "--new-window", video_url], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Gantilah URL dengan URL video YouTube yang ingin Anda buka
    youtube_video_url = "https://www.youtube.com/watch?v=XvkEiIwt-UU&autoplay=1&mute=1"
    
    # Melakukan perulangan 5 kali
    for _ in range(5):
        open_chrome_as_guest(youtube_video_url)
