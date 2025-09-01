import requests

def download_image(url, filename):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status() 

        with open(filename, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        print(f"✅ Image downloaded successfully as {filename}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    url = input("Enter image URL: ")
    filename = input("Enter filename to save (e.g. photo.jpg): ")
    download_image(url, filename)
