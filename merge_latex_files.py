import os
import re

def merge_latex_files(output_filename, input_filenames):
    with open(output_filename, 'w') as output_file:
        for input_filename in input_filenames:
            with open(input_filename, 'r') as input_file:
                content = input_file.read()
                # Find all \input{filename} commands and replace them with the content of the file
                content = re.sub(r'\\input{(.+?)}', lambda match: open(match.group(1)+".tex").read(), content)
                output_file.write(content)

if __name__ == "__main__":
    output_filename = "main_merged.tex"  # Change this to the desired output file name
    input_filenames = ["main.tex"]  # Add the name of your main LaTeX file

    merge_latex_files(output_filename, input_filenames)
    print(f"Processed '{input_filenames[0]}' and merged into '{output_filename}'.")