import get_all_files as gaf
import batch_treat_handler as bth
import front_reception as fr
import revamp_batch_binary as rbb
import amend_new_paths as anp
import filter_duplicates as fd
import type_history_log as thl
import write_action as wa


def gain_infor_tuple():
    files_collect = gaf.get_all_files(fr.target_path)

    files_url_collect = bth.gain_files_information(files_collect)
    deduplication_list = fd.gain_deduplication(files_url_collect)

    thl.remember_logger(files_url_collect, "files_url_collect-")
    thl.remember_logger(deduplication_list, "deduplication_list-")

    return files_url_collect, deduplication_list


def opereation():
    files_url_collect, deduplication_list = gain_infor_tuple()

    # 根据获取得到的返回数据，遍历它，逐一修改文件中的二进制
    rbb.revamp_batch_binary(files_url_collect)

    # ergodic，files modifies name
    anp.amend_new_files_path(files_url_collect)

    # ergodic, directories changed name
    anp.revise_dirname(deduplication_list)

    # injects byte_string into content of file
    wa.write_cipher_in_file(fr.security_pass, files_url_collect)


# opereation()
# gain_infor_tuple()
