# zip file

import zipfile

zf = zipfile.ZipFile('data.zip', mode='w')

try:
    zf.write('datasets/train_catvnoncat.h5')
    zf.write('datasets/test_catvnoncat.h5')
finally:
    zf.close()