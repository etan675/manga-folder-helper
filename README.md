### Manga Folder Helper

A console (CLI) tool that streamlines the process of converting manga from mangakatana.com into 
e-reader formats, using KCC (Kindle Comic Converter)

#### Note:

I have documented the FULL steps on downloading, converting, and transferring manga to kindle at 
the bottom of this tutorial, feel free to have a quick read of those steps first for some context.

### Description (12/12/2024):

Basically, manga sources downloaded from mangakatana.com will be organised in nested folders, 
but KCC doesn't support nested folders as input, and we definitely don't want to be manually 
picking out the files for each chapter and converting one at a time.
 
So we want to end up with just a single 'flattened' folder, with all of the manga's source files 
in its original sequence, we will then use this as the input for KCC.

```flatten.py``` is a tool/script that generates and outputs a 'flattened' version of the manga's
source for you, so that you can convert everything in one go!


### Requirements:

Mangakatana: https://mangakatana.com/
Search and download the manga you want, the website allows you to download chapters in batches of 10.

KCC: https://github.com/ciromattia/kcc
Follow instructions on their github page to install the desktop app

Python3: https://www.python.org/downloads/
If not already installed, you will need python3 as it's the programming language I used 
(run ```python3 --version``` in your terminal to check if you have it).


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


### Instructions:
Examples for mac, but instructions are the same for other OS.

1. Download (or clone) this repository to your desired folder
    - Click the green ```< > Code``` button on this page
    - Click Download ZIP (e.g. to Desktop), then unZIP

2. Open up the terminal and navigate into the folder
    - e.g. ```cd ~/Desktop/manga-folder-helper```

3. Optional: create a new folder as the output's destination

4. Get the manga source's path and the destination's path
    - To get the path of a folder: 
        - Go to ```Finder```, navigate to the location of your folder, 
        right-click the path bar at the bottom of the finder tab, and click copy as Pathname 
        (if you don't see the path bar, go to ```View```, and click ```Show Path Bar```)

5. Run the console tool
    - For assistance check the help manual using the following command:
        - ```python3 flatten.py --help```
    - To execute:
        - ```python3 flatten.py [path_of_source] -o [path_of_destination]```
            - '-o', or output, is an optional argument, if left unspecified the output 
            will just go in your current folder

### Further Resources

Here's a great tutorial on how to use KCC and transferring files to kindle:
https://www.youtube.com/watch?v=SaBTFTuD6hk&t=545s&ab_channel=LeoLabTech

FULL steps online to kindle:

1. Download manga from mangakatana (follow their steps)
2. Follow this tutorial to end up with a flattened folder with every page of your manga in it
3. Use KCC to convert it from pc (e.g. jpeg) to kindle format (mobi/AWZ3)
4. Connect your kindle to pc with an adapter cable
5. Make sure the manga files (e.g. .mobi) are all in one folder, and give this folder a proper name, e.g. the manga's name, or 'chapters0-100', 
I prefer this as it will make the entire thing appear as one 'book' in your kindle library.

6. Move your manga folder into the correct kindle drive:
    -  your kindle drive -> documents
7. Eject the kindle drive and start reading :)

