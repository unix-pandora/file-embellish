import operator
import front_reception as fr


def filter_duplicate_dirs(param_dict):
    container_list = []

    for element in param_dict:
        capacity_dict = dict()
        capacity_dict["origin_folder"] = element["origin_folder"]
        capacity_dict["new_parent_directory"] = element["new_parent_directory"]
        container_list.append(capacity_dict)
    # print(container_list)
    return container_list


def merge_duplicates(dict_array):
    result = []
    for d in dict_array:
        if d not in result and d["origin_folder"] != fr.target_path:
            result.append(d)
    return result


def gain_deduplication(param_dict):
    container_list = filter_duplicate_dirs(param_dict)
    result = merge_duplicates(container_list)
    sorted_list = sorted(result, key=operator.itemgetter("origin_folder"), reverse=True)
    return sorted_list
