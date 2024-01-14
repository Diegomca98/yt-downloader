from pytube import YouTube as YT
import os

def menu():
    print("|----- DOWNLOAD OPTIONS -----|")
    print("1. Video")
    print("2. Audio")
    print("|----------------------------|")

    try:
        choice = int(input("Type the option number: "))
        return choice
    
    except Exception as e:
        return 1

def downloader(url, out_path, audio_only=False):
    try:
        yt = YT(url)
        print(f'Downloading: {yt.title}...')
        
        if audio_only == True:
            yt.streams.filter(only_audio=audio_only).first().download(out_path)
        else:
            yt.streams.get_highest_resolution().download(out_path)

        print(f'{yt.title} downloaded successfully')

    except Exception as e:
        print(f"The video/audio couldn\'t download the video, try later")
        print(f"Error: {str(e)}")

def main():
    video_url = input('Introduce the YouTube video URL: ')
    out_path = os.path.join(os.getcwd(), 'assets', 'downloads')

    print(f"The downloads would be saved at: {out_path}")

    choice = menu()
    if choice == 2:
        downloader(video_url, out_path, audio_only=True)
    else:
        downloader(video_url, out_path)

if __name__ == "__main__":
    main()