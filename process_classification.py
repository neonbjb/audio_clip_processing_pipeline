import os
import shutil
import argparse
from tqdm import tqdm

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', metavar='in', type=str)
    parser.add_argument('basis', metavar='basis', type=str)
    parser.add_argument('out', metavar='out', type=str)
    args = parser.parse_args()
    print(f"Moving files from {args.input} to {args.out}")
    os.makedirs(args.out, exist_ok=True)

    with open(args.input) as f:
        lines = f.readlines()
        for line in tqdm(lines):
            path, cls = line.strip().split('\t')
            assert args.basis in line
            movefile = os.path.join(args.out, cls, path.replace(args.basis, '')[1:])
            print(f'{path} -> {movefile}')
            os.makedirs(os.path.dirname(movefile), exist_ok=True)
            if os.path.exists(path):
                shutil.move(path, movefile)
            else:
                print("File does not exist!")

    
    
    
