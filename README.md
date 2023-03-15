# File organizer
- [Default configuration](#default-organizer-configuration)
- [Features](#organizer-features)
- [Running](#running-organizer)

General use file organizer for removing all but the wanted file extentions, moving files out of subfolders and deleting empty folders.
Default file is set up for using with Plex for cleaning up torrent downloads (movies and tv shows), but extentions can simply be changed in the python script.
PS! The code needs a command line argument for the working directory.

**I AM NOT RESPONSIBLE FOR ANY DATA LOSS UPON WRONG CONFIGURATION OR CODE CHANGES!** 

Always have backups and check your code and config files.

## Default organizer configuration

Organizes the movies and tv directories placed in the folder that contains them.

```
Dir from organizer.py <path_to_folder>
├── movies
│   ├── Movie folder
│   │   ├── movie.mkv or movie.mp4
│   │   ├── other files
│   │   ├── sub.srt (might not excist)
│   │   └── subs (optional some have some don't)
│   │       └── subs.srt
│   └── movies folder 2 and so on
├── tv
│   ├── Show folder
│   │   ├── show.mkv or show.mp4
│   │   ├── other files
│   │   └── subs (optional some have some don't)
│   │       └── subs.srt
│   ├── Show folder
│   │   ├── show episode folder
│   │   │   ├── show.mkv or show.mp4
│   │   │   ├── other files
│   │   │   ├── subs.srt (might not excist)
│   │   │   └── subs (optional some have some don't)
│   │   │       └── subs.srt
│   ├── show season folder
│   │   └── show episode folder
│   │       ├── show.mkv or show.mp4
│   │       ├── subs.srt (might not excist)
│   │       └── subs (optional some have some don't)
│   │           └── subs.srt
│   └── show season folder
│       ├── show.mkv or show.mp4
│       ├── show.mkv or show.mp4
│       ├── subs.srt (might not excist)
│       └── subs (optional some have some don't)
│           └── subs.srt
└── other stuf it wont touch
```

Returns

```
Dir from organizer.py <path_to_folder>
├── movies
│   ├── Movie folder
│   │   ├── movie.mkv or movie.mp4
│   │   └── subs.srt (from folder and pre excisting)
│   └── movies folder 2 and so on
├── tv
│   ├── Show folder
│   │   ├── show.mkv or show.mp4
│   │   └── subs.srt (from folder and pre excisting)
│   ├── Show folder
│   │   ├── show episode folder
│   │   │   ├── show.mkv or show.mp4
│   │   │   └── subs.srt (from folder and pre excisting)
│   ├── show season folder
│   │   └── show episode folder
│   │       ├── show.mkv or show.mp4
│   │       └── subs.srt (from folder and pre excisting)
│   └── show season folder
│       ├── show.mkv or show.mp4
│       ├── show.mkv or show.mp4
│       └── subs.srt (from folder and pre excisting)
└── other stuf it wont touch
```

## Organizer features

* Log file in the same dir that gets organized called organizer.log (time stamp and operation) (editable in code)
* Location to the directory containing desired folders for organizing asked as command line argument
* Removes unwanted files
* Moves certain files out of subfolders
* Deletes empty folders
* Default config for torrenting uses the .!qB extention for not deleting mid download files (check qbittorrent settings for enabling it)

## Running organizer

* Download with `sudo wget https://raw.githubusercontent.com/Toomas633/File-organizer/main/organizer.py` and place it into the folder you want it to search through (see example above)
  * Run it in the backround while being in the same folder with `nohup python3 organizer.py <path_to_folder>`
  * Or run it always after reboot with cron job by adding `0 * * * * python3 /<path_to_script>/organizer.py <path_to_folder>` using `sudo crontab -e` and adding it to the end of the file

## Donate

Monero: `8Ajf5M6meNpL9TaHuDRbXjAH31LcQ9ge5BEiwMZjLaoiMDZRxaVy19FgbP4tbUKpKoeq1kqCvjyaTdmCMQGhekWoQ2KgVeV`

Bitcoin: `3NPFV9ivECdSgyCXeNk4h5Gm3q1xiDRnPV`

More options on https://toomas633.com/donate.html
