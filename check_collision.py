import argparse
import os
from collections import defaultdict

def check_filename_collisions(input_file):
    filename_dict = defaultdict(list)
    
    with open(input_file, 'r') as file:
        for line in file:
            full_path = line.strip()
            filename = os.path.basename(full_path)
            filename_dict[filename].append(full_path)
    
    collisions = {filename: paths for filename, paths in filename_dict.items() if len(paths) > 1}
    
    if collisions:
        print("Filename collisions found:")
        for filename, paths in collisions.items():
            print(f"\nFilename: {filename}")
            for path in paths:
                print(f"  - {path}")
    else:
        print("No filename collisions found.")

def main():
    parser = argparse.ArgumentParser(description="Check for filename collisions in a list of files.")
    parser.add_argument("--input-list", required=True, help="Path to the input text file containing the list of files.")
    args = parser.parse_args()
    
    check_filename_collisions(args.input_list)

if __name__ == "__main__":
    main()