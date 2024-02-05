import os
import search_root_path as srp
import gain_log_filename as glf


redundant_chars = [
    "，",
    "/",
    " ",
    "|",
    "【",
    "】",
    "（",
    "）",
    "！",
    "~",
    "、",
    "。",
    "！",
    "？",
    "《",
    "》",
    "；",
    "：",
    "“",
    "”",
    "……",
    "#",
    "～",
    "~",
    "–",
    "[",
    "]",
    "(",
    ")",
]

sign_array = [["+", "_p_"], ["=", "_e_"], ["/", "_s_"]]

shift_number = 25

backup_log_label = "Mission-"
backup_log_extension = ".txt"

root_file_sign = "background_setting.py"
root_file_path = srp.find_file(root_file_sign)
project_root_directory = os.path.dirname(root_file_path)

json_file_name = glf.forge_note_name()

keylength_upper_limit = 16

lock_pattern = 0
unlock_pattern = 1

separator = str(os.path.sep)

fringe_byte_length = 30

name_len_limit = 60
