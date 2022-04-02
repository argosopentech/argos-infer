import argparse
import random

parser = argparse.ArgumentParser(description="Generates summarization data")
parser.add_argument(
    "datafile",
    help="A file with text data",
)
args = parser.parse_args()

with open(args.datafile, 'r') as datafile:
    data = datafile.read()
    paragraphs = data.split("\n")
    sourcelines = list()
    targetlines = list()

    for paragraph in paragraphs:
        paragraph = paragraph[:300]
        source_end_index = int(random.random() * (len(paragraph) - 1))
        source = paragraph[:source_end_index]
        target = paragraph[source_end_index:]
        target_space_index = target.find(" ")
        if target_space_index > 0:
            target = target[:target_space_index]
        sourcelines.append(source + "\n")
        targetlines.append(target + "\n")

    with open('output_data.src', "w") as sourcefile:
        sourcefile.writelines(sourcelines)
    with open('output_data.tgt', "w") as targetfile:
        targetfile.writelines(targetlines)
