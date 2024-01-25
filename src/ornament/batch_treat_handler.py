import single_handle_name as shn


def gain_files_information(paths_list):
    url_infor_dict = []
    for index in paths_list:
        new_url = shn.assemble_data(index)
        url_infor_dict.append(new_url)
    return url_infor_dict
