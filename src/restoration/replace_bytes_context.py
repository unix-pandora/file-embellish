import endurance_binary_content as ebc
import background_setting as bg


def alter_batch_binary(parameter_dict_list):
    for element in parameter_dict_list:
        ebc.replace_byte_string(element["origin_absolute"], bg.fringe_byte_length)
