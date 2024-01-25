import rename_files_tool as rft


def amend_new_files_name(param_dict_collect):
    for element in param_dict_collect:
        rft.rename_file_or_folder(
            element["origin_absolute"], element["transition_absolute"]
        )


def revise_dir_url(param_dict_collect):
    for element in param_dict_collect:
        rft.rename_file_or_folder(
            element["origin_folder"], element["real_parent_folder"]
        )
