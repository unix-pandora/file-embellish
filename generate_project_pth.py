import os


def get_absolute_paths(relative_path):
    absolute_paths = []
    for root, dirs, _ in os.walk(relative_path):
        for dir in dirs:
            absolute_path = os.path.abspath(os.path.join(root, dir))
            absolute_paths.append(absolute_path)
    relative_root_path = os.path.abspath(os.path.join(relative_path))
    absolute_paths.append(relative_root_path)
    return absolute_paths


def filter_strings(prev_list, exclude_list):
    newlist = []
    for item in prev_list:
        if all(exclude not in item for exclude in exclude_list):
            newlist.append(item)
    return newlist


def write_strings_to_file(str_list, file_path):
    with open(file_path, "w") as file:
        for item in str_list:
            file.write(item + "\n")


exclusion_eles = ["vscode", "pycache", ".git"]
file_name = "necessity.pth"

paths = get_absolute_paths(".")
# print(paths)

paths2 = filter_strings(paths, exclusion_eles)
print(paths2)

write_strings_to_file(paths2, file_name)
