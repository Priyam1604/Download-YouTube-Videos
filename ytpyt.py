from pytube import YouTube

# Get the video from the user
link = input("Enter the YouTube video link: ")

# Create a YouTube object
yt = YouTube(link)

# Get the best resolution video
best_resolution = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

# Download the video
best_resolution.download()
