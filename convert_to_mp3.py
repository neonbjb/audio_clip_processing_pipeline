from pathlib import Path
import os
import subprocess
from do_to_files import do_to_files

def convert_to_mp3(path, output_path):
    out_f = os.path.join(output_path, os.path.basename(path)[len(inpf):-3] + "mp3")
    os.makedirs(os.path.dirname(out_f), exist_ok=True)
    print(out_f)
    subprocess.call(f'ffmpeg -y -i "{f}" "{out_f}"', shell=True)


if __name__ == '__main__':
    do_to_files(filter_no_hifreq_data)
