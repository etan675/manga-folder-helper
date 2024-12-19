import os
import argparse
import shutil

parser = argparse.ArgumentParser(
    prog="flatten",
    description="Flatten the manga source's folder structure for easy converting"
)

parser.add_argument('input_path', help="path to the manga source")
parser.add_argument('-o', '--out', help="optional, specified path where the output should go")

args = parser.parse_args()

input_path = args.input_path
output_path = args.out if args.out else os.getcwd()

def generate_rel_path_filename(filename, dir_path, root_path, sep='%'):
    rel_path = os.path.relpath(dir_path, root_path)

    if (rel_path == '.'):
        # for 'root'
        rel_path = 'rt'
    else:
        rel_path = rel_path.replace('/', sep)

    return rel_path + sep + filename

for [dir_path, dirnames, filenames] in os.walk(input_path):
    if len(filenames):
        for filename in filenames:
            shutil.copy(os.path.join(dir_path, filename), output_path)

            new_filename = generate_rel_path_filename(filename, dir_path, input_path)

            copied_file_path = os.path.join(output_path, filename)
            renamed_file_path = os.path.join(output_path, new_filename)
                
            os.rename(copied_file_path, renamed_file_path)




    

            

            


        






