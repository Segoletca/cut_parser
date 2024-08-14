import os


def one_file_parser(path, out_path="./trim_logs/", create_one_file=False) -> None:
    file_name = os.path.basename(path)
    name_out_file = out_path + "Summary" + file_name[3:-3] + "log"
    if create_one_file:
        name_out_file = out_path + "Summary_cutadapt.log"

    with open(path, "r") as file:
        line_number = 1
        file = file.readlines()
        out = f"Reads{file_name[3:]}\n"
        out += f"{file[1]}\n"
        sample_num = 1

        for line in file:
            if line == "=== Summary ===\n":
                with open(name_out_file, "a") as new_file:
                    out += f"Sample_{sample_num}\n"
                    new_file.writelines(out)
                    new_file.writelines(file[line_number - 1: line_number + 16])
                    new_file.writelines("\n\n")

                    sample_num += 1
                    out = ""

            line_number += 1


one_file_parser("./raw_logs/log_01_04.log")
