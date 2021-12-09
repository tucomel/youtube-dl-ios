import console
import dialogs
import clipboard
import sys
import glob
import os
from yt_dlp import YoutubeDL
from objc_util import on_main_thread

#Screen always on.
on_main_thread(console.set_idle_timer_disabled)(True)

url = clipboard.get()
print('url: %s' % (url))

#List formats
with YoutubeDL() as ydl:
	meta = ydl.extract_info(url, download=False) 
	formats = meta.get('formats', [meta])
	
formats_string = ['bestaudio[ext=m4a] AudioOnly m4a', 'best[ext=mp4] BestVideo mp4'] + [item['format_id']+' '+item['format_note']+' '+item['ext']+' '+item['vcodec'] for item in formats]

#Select AVC format to preview on iOS.
format_choise = dialogs.list_dialog(title = 'Formats', items = formats_string)
	
opts = {
	'format': format_choise.split()[0]
}

with YoutubeDL(opts) as ydl:
	ydl.download([url])

#Share file
file = max(glob.glob('*.'+format_choise.split()[2]), key=os.path.getctime)
if not file:
	raise IndexError('downloaded file not found')
print('downloaded: %s' % (file))

try:
	if format_choise.split()[2] == 'webm':
		console.open_in(file)
	else:
		console.quicklook(file)
finally:
	os.remove(file)
	print('deleted: %s' % (file))
