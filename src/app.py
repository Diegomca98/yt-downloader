from pytube import YouTube as YT
import os

def download_video(url, out_path):
    try:
        yt = YT(url)
        print(f'Downloading: {yt.title}...')
        yt.streams.get_highest_resolution().download(out_path)
        print(f'{yt.title} downloaded successfully')

    except Exception as e:
        print(f"The video couldn\'t download the video, try later")
        print(f"Error: {str(e)}")



def main():
    video_url = input('Introduce the YouTube video URL: ')
    out_path = os.path.join(os.getcwd(), 'assets', 'downloads')

    print(f"The downloads would be saved at: {out_path}")

    download_video(video_url, out_path)

if __name__ == "__main__":
    main()