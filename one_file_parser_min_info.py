import os
import re


def one_file_parser_min_info(path, out_path="./trim_logs/", create_one_file=False) -> None:
    file_name = os.path.basename(path)
    name_out_file = out_path + "MinInfo" + file_name[3:-3] + "log"
    if create_one_file:
        name_out_file = out_path + "MinInfo_cutadapt.log"

    with open(path, "r") as file:
        line_number = 1
        file = file.readlines()
        out = f"Reads{file_name[3:]}\n"
        out += f"{file[1]}\n"
        sample_num = 1

        for line in file:

            with open(name_out_file, "a") as new_file:
                if line == "=== Summary ===\n":
                    out += f"Sample_{sample_num}\n"
                    new_file.writelines(out)
                    new_file.writelines(file[line_number + 1: line_number + 4])

                if re.findall("Total basepairs processed", str(line)):
                    new_file.writelines(file[line_number - 1])
                    new_file.writelines(file[line_number + 2])
                    new_file.writelines("\n\n")

                    sample_num += 1
                    out = ""

            line_number += 1
