import zipfile
from zipfile import ZipFile, ZIP_DEFLATED
import os

#file_zip = zipfile.ZipFile('archive_zip', 'w')


with ZipFile('resources/file_zip', 'a', compression=ZIP_DEFLATED, compresslevel=5) as myzip:
    for folder, subfolders, files in os.walk('resources'):
        for file in files:
            if file.endswith(('.csv', '.xlsx', '.pdf')):
                myzip.write(os.path.join(folder, file),
                            os.path.relpath(os.path.join(folder, file), 'resources'),
                            compress_type=zipfile.ZIP_DEFLATED)



