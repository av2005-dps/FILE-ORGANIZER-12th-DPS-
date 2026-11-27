# File Organizer

This is my Python project for school (Class 12). It is a small program that cleans up a messy folder by sorting all the files into different folders automatically.

For example, if a folder has some photos, PDFs and songs all mixed together, this program will move them into folders like `Images`, `PDFs` and `Music`.

## What it does

* Looks at every file in a folder
* Checks the file type (like .pdf, .png, .mp3)
* Moves the file into the right folder
* Makes the folder if it does not exist yet
* Puts unknown file types in a folder called `Others`
* If two files have the same name, it adds a number to the name so nothing gets deleted

## Folder setup

```
my_project/
├── file_organizer.py
└── file_organizer/
    └── files/      <- put the files you want to sort here
```

## Things I learned

* How to use the `os` module to work with files and folders
* How to use `shutil.move()` to move files
* Using a dictionary to store which extension goes to which folder
* Using loops and if/else to check every file
* How to handle files with the same name

## Ideas to improve it later

* Sort files by date
* Add more file types
* Make a simple GUI with buttons
* Add an undo option
