### Manga Folder Helper

A CLI tool that assists with converting manga into e-reader formats using KCC (Kindle Comic Converter)

Note:

The bottom of this tutorial has further information on the full process of downloading, converting, and transferring manga onto your e-reader, from internet to kindle.


### Description:

(12/12/2024)
This is a quick script that flattens the folder structure of manga downloaded from mangakatana.com.
The purpose of this is so we can convert the whole manga in one go with KCC. The format of the manga downloaded fom mangakatana will have lots of nested folders, KCC doesn't
support nested folders as input, so if you try to do this manually, you will have to convert each chapter one by one.


### Requirements:

KCC: https://github.com/ciromattia/kcc (follow instructions on their github page to install the desktop app)

MangaKatana: https://mangakatana.com/ (search and download the manga you want, the website allows you to download in 10 chapter increments)

Python3.13 (or any version of python3 should be ok)


### Function:

    Example Input:
    - your-manga (dir)
        - ch1-10 (dir) 
            - ch1 (dir)
                - pg1 (jpeg)
                - pg2 (jpeg)
                - pg3 (jpeg)
                - ...
            - ch2
            - ch3

    Example Output:
    - your-manga (dir)
        - ch1-10-ch1-pg1 (jpeg)
        - ch1-10-ch1-pg2 (jpeg)
        - ch1-10-ch1-pg3 (jpeg)
        - ...


### Usage:
(instructions for mac)

1. Download (or clone) the repo to your desired path
    - To download: 
        - click the green ```< > Code``` button on this page
        - click Download ZIP (e.g. select desktop as download path), then unZIP

2. Open up the terminal and navigate to the app's path
    - e.g. ```cd ~/Desktop/manga-folder-helper```

3. Create a new folder as the output's destination

4. Get the manga source's path and the destination's path
    - to get the path of a folder: 
        - go to ```Finder```, navigate to the location of your folder, right-click the path bar at the bottom of the finder tab, and click copy as Pathname (if you don't see the path bar, go to ```View```, and click ```Show Path Bar```)

5. Run the console app
    - For assistance check the help manual using the following command:
    - ```python3 flatten.py --help```
    - To execute:
    - ```python3 flatten.py [path_of_source] -o [path_of_destination]```

6. Now you can select the output folder in KCC and convert everything in one go!

### Further Resources

Here's a great tutorial on how to use KCC and transferring files to kindle:

https://www.youtube.com/watch?v=SaBTFTuD6hk&t=545s&ab_channel=LeoLabTech

Full steps (internet to kindle):

1. Download manga from mangakatana (follow their steps)
2. Follow this tutorial to end up with a flattened folder with every page of your manga
3. Use KCC to convert manga from pc format to kindle format (mobi/AWZ3)
4. Connect your kindle to pc with an adapter cable
5. Make sure the manga files (e.g. .mobi) are all in one folder, and give this folder a proper name, e.g. the manga's name, or 'chapters0-100'

    5.5. The content's structure should align with how kindle interprets its file system. Organising the content this way makes sure the downloaded manga will appear as one 'book', I personally prefer it this way as it just looks cleaner in the kindle library.

6. Move your manga folder into the correct kindle drive:
    -  your kindle drive -> documents
7. Eject the kindle drive and start reading :)

