# youtube-dl-ios

> [youtube-dl][youtube-dl] for iOS, with [Pythonista][pythonista] and
[Shortcuts][shortcuts]

A video (or its audio track) is downloaded by sharing it to a shortcut

The shortcut calls a helper script run within Pythonista. This script passes the
URL to youtube-dl to do the actual download. After the downloads completes, the
file is opened in a share sheet where it may be copied to any app, such as VLC.

## Install

1. Install Pythonista
2. In Pythonista, install [StaSH][stash]
3. In a StaSH console, install youtube-dl:

    ```
    $ pip install youtube-dl
    ```

4. and clone this repository (note: `git` is only available if StaSH is run in
   Python 2):

    ```
    $ cd
    $ git clone https://github.com/Roman2K/youtube-dl-ios
    ```

5. Install the shortcut: [iCloud link][shortcut]

## Usage

1. Share a video to Shortcuts and then youtube-dl-ios
2. The downloaded file opens in a share sheet: choose an app
3. (The temporary file is cleaned up)

[youtube-dl]: https://rg3.github.io/youtube-dl/
[pythonista]: http://omz-software.com/pythonista/
[shortcuts]: https://support.apple.com/en-jo/guide/shortcuts/welcome/ios
[stash]:https://github.com/ywangd/stash
[shortcut]: https://www.icloud.com/shortcuts/85f6b11f2827451da6d1f5b82b11816a
