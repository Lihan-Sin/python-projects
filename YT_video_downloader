from pytube import YouTube
link = str(input("Enter the link: "))
yt = YouTube(link)
stream = yt.streams.get_highest_resolution()
stream.download()
print("Download complite!!")
