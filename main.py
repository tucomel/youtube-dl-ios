import console
import sys
import clipboard
import glob
import os
from youtube_dl import YoutubeDL

url = sys.argv[1] if len(sys.argv) == 2 else clipboard.get()
print('url: %s' % (url))

choices = (
	('Audio', 'bestaudio[ext=m4a]', 'm4a'),
	('Video', 'bestvideo[ext=mp4]', 'mp4'),
)
choice = console.alert(
	'youtube-dl', 'Version to extract:', *(c[0] for c in choices))

_, format, ext = choices[choice-1]
print('format: %s' % (format))

opts = {
	'format': format
}
with YoutubeDL(opts) as ydl:
	ydl.download([url])

file = max(glob.glob('*.'+ext), key=os.path.getctime)
if not file:
	raise IndexError('downloaded file not found')
print('downloaded: %s' % (file))

try:
	console.open_in(file)	
finally:
	os.remove(file)
	print('deleted: %s' % (file))
