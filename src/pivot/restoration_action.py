import batch_restoration_handler as brh
import type_history_log as thl
import write_action as wa
import front_reception as fr
import change_path_methods as cpm
import replace_bytes_context as rbc


def gain_information_list():
    total_array = brh.gain_total_data_set()

    elements_tuple = brh.gain_pitch_data(total_array)
    files_array = elements_tuple[0]
    folder_set = elements_tuple[1]

    filter_dir_list = brh.filter_repetitive_folder(folder_set)

    wa.write_cipher_in_file(fr.security_pass, total_array)
    thl.remember_logger(total_array, "total_array-")
    thl.remember_logger(filter_dir_list, "filter_dir_list-")
    thl.remember_logger(files_array, "files_array-")

    return total_array, files_array, folder_set, filter_dir_list


def performance():
    total_arr, files_arr, folder_set, filter_dirs = gain_information_list()

    # modify binary content in file
    rbc.alter_batch_binary(total_arr)

    # rename files name
    cpm.amend_new_files_name(files_arr)

    # rename directory name
    cpm.revise_dir_url(filter_dirs)


# performance()
# gain_information_list()
