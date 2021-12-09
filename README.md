# yt-dlp-ios

> [yt-dlp][yt-dlp] for iOS, with [a-Shell][a-shell] and
[Shortcuts][shortcuts]

Download a video (or its audio track) by sharing it to a shortcut

The shortcut calls a helper script run within a-Shell. This script passes the
URL to yt-dlp to do the actual download. After the download completes, the
file is opened in a share sheet where it may be copied to any app, such as VLC.

## Install

1. Install a-Shell
2. In a-Shell, install yt-dlp

    ```sh
    $ pip install --upgrade yt-dlp --no-deps
    ```

3. Clone this repository or copy this file to any folder inside ~/Documents

    ```sh
    $ cd
    $ git clone https://github.com/tucomel/youtube-dl-ios
    ```

5. Install the shortcut: [iCloud link][shortcut]

## Usage

1. Share a video to Shortcuts and then yt-dlp-ios
2. The downloaded file opens in a share sheet: choose an app
3. (The temporary file is cleaned up)

[youtube-dl]: https://rg3.github.io/youtube-dl/
[a-shell]: https://holzschu.github.io/a-Shell_iOS/
[shortcuts]: https://support.apple.com/en-jo/guide/shortcuts/welcome/ios
[shortcut]: https://www.icloud.com/shortcuts/85f6b11f2827451da6d1f5b82b11816a
