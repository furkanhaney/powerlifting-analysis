import shutil
import zipfile
import os.path
import urllib.request

ROOT = "https://openpowerlifting.gitlab.io/opl-csv/files/"
FILE = "openpowerlifting-latest.zip"

download_uri = os.path.join(ROOT, FILE)
save_uri = os.path.join("data/original", FILE)
extract_uri = "data/extracted"

## Download the latest Open Powerlifting data.
with urllib.request.urlopen(download_uri) as response:
    with open(save_uri, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)

## Extract the contents of the file.
with zipfile.ZipFile(save_uri, 'r') as zip_ref:
    zip_ref.extractall(extract_uri)