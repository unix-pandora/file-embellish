import operator

import front_reception as fr
import single_decipher as sde
import get_all_files as gaf


def gain_total_data_set():
    files_set = gaf.get_all_files(fr.target_path)
    total_list = list()

    for element in files_set:
        temp_dict = dict()
        temp_dict = sde.crack_build(element)
        total_list.append(temp_dict)
    # print("total_list", total_list)
    return total_list


def gain_pitch_data(total_array):
    absolute_url_array = list()
    folders_collect = list()

    for index in total_array:
        temp_dict = dict()
        temp_dict1 = dict()

        temp_dict["origin_absolute"] = index["origin_absolute"]
        temp_dict["real_absolute_path"] = index["real_absolute_path"]
        temp_dict["transition_absolute"] = index["transition_absolute"]

        temp_dict1["origin_folder"] = index["origin_folder"]
        temp_dict1["real_parent_folder"] = index["real_parent_folder"]

        absolute_url_array.append(temp_dict)
        folders_collect.append(temp_dict1)
    return absolute_url_array, folders_collect


def filter_repetitive_folder(repetitive_folders):
    unique_dir_list = list()

    for index in repetitive_folders:
        if index not in unique_dir_list:
            unique_dir_list.append(index)
    # print(unique_dir_list)
    for ele in unique_dir_list:
        ele.update({"origin_folder_length": len(ele["origin_folder"])})
        ele.update({"real_parent_folder_length": len(ele["real_parent_folder"])})

    sorted_list = sorted(
        unique_dir_list,
        key=operator.itemgetter("real_parent_folder_length"),
        reverse=True,
    )
    return sorted_list


def test():
    total_array = gain_total_data_set()
    elements_tuple = gain_pitch_data(total_array)
    dir_list = filter_repetitive_folder(elements_tuple)
    print(dir_list)


# test()
