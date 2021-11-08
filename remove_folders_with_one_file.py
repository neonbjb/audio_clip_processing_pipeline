import os
import pathlib
import shutil

paths = pathlib.Path('books3').glob('*')
for path in paths:
    path = str(path)
    if len(list(pathlib.Path(path).glob('*'))) <= 1:
        print(f"{path} doesn't have enough files.")
        shutil.rmtree(path)