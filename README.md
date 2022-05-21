# google-spreadsheet-downloader

## Description
Download Google spreadsheet which the URL ends in "/pubhtml" and save it as a .csv file.  
Based on Python.

## Usage
### Preparation 
1. Clone the repository using git or just download the zip file from this page.
2. Make sure you have installed python3 on your device.  
3. Install package `requests` by typing `pip install requests` or `python -m pip install requests` in your terminal.
### Use
1. Type the following command: `python download.py [url]`.  
Be careful that `[url]` must be starts with `https://` and ends with `/pubhtml`.
2. `[sheetname].csv` file(s) will appear in your working directory.

## Reference
[Reddit thread](https://www.reddit.com/r/googlesheets/comments/aymwjd/how_do_you_select_csv_output_for_individual/)