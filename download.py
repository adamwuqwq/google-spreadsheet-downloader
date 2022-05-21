import sys
import csv
import os
import requests
import re

def error_exit(message):
    print(message)
    exit("There is some error, so that the program is terminated.")

# make sure the number of arguments is correct
argvs = sys.argv
if len(argvs) != 2:
    error_exit("Invalid arguments, please make sure you type the command as follows: python download.py [url]")

url = argvs[1]

# if url is not end with "pubhtml", report error
suffix = "pubhtml"

if not url.endswith(suffix):
    error_exit("URL is invalid, please make sure it ends with '" + suffix + "'!")

# get html content, convet to string
print("Step 1: Fetching html contents from given URL...")

html_content = requests.get(url).text

head_pattern = "<body class=\"docs-gm\">"
is_html_valid = re.findall(head_pattern, html_content)

if is_html_valid:
    print("Done!")
else:
    error_exit("Invalid html content!")

# find all the that match the specified pattern
print("Step 2: Matching specified pattern in HTML file...")

sheet_pattern = "<li id=\"sheet-button-[0-9]+\"><a href=\"#\">.*?</a></li>"
matched = re.findall(sheet_pattern, html_content)
print(len(matched), "matches found!")

# extract gid and name of each sheet from the matched strings
print("Step 3: Extracting name and gid for each worksheet...")

gid_pattern = "(?<=sheet-button-)[0-9]+(?=\"><a href=\"#\">)"
name_pattern = "(?<=<a href=\"#\">).*?(?=</a></li>)"
sheets = {}
if len(matched) != 0:
    for matches in matched:
        # print(matches)
        gid = re.findall(gid_pattern, matches)
        name = re.findall(name_pattern, matches)
        # print(gid, name)
        if len(gid) != 1 or len(name) != 1:
            error_exit("Invalid matched string! Please report it to developer!")
        else:
            sheets[name[0]] = gid[0]
else:
    print("It seems that the document only contains 1 sheet!")
    gid = "0"
    name = "default"
    sheets[name] = gid

print("Done!")

# download csv file (for each sheet)
print("Step 4: Downloading .csv file for each worksheet...")

for key in sheets.keys():
    print(key + ".csv", end='...')
    gid = sheets[key]
    url_csv = url[:-4] + "?output=csv&gid=" + gid
    csv_content = requests.get(url_csv).content
    fileName = key + ".csv"
    with open(fileName, 'wb') as file:
        file.write(csv_content)
    print("done!")
