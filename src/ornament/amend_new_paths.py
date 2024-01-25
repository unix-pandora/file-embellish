import rename_files_tool as rft


def amend_new_files_path(parameter_dict_array):
    for element in parameter_dict_array:
        rft.rename_file_or_folder(element["origin_absolute"], element["file_new_path"])


def revise_dirname(parameter_dict_array):
    for element in parameter_dict_array:
        rft.rename_file_or_folder(
            element["origin_folder"], element["new_parent_directory"]
        )
