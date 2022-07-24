#!/usr/bin/env python3

import argparse
import random
import pathlib

parser = argparse.ArgumentParser(description="Generate autoregressive data")
parser.add_argument(
    "datafile",
    help="A file with text data",
)
args = parser.parse_args()

source_path = pathlib.Path("source")
target_path = pathlib.Path("target")

MAX_LINE_LEN = 50

if source_path.exists() or target_path.exists():
    print("Source or target already exists")
    exit(1)

source_file = open(source_path, "a")
target_file = open(target_path, "a")

with open(args.datafile, 'r') as datafile:
    for line in datafile:
        line = line[:MAX_LINE_LEN]
        source_end_index = int(random.random() * (len(line) - 1))
        source_line = line[:source_end_index]
        target_line = line[source_end_index:]
        source_file.write(source_line + "\n")
        target_file.write(target_line + "\n")
        
source_file.close()
target_file.close()
