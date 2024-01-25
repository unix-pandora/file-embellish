import endurance_binary_content as ebc
import background_setting as bg
import front_reception as fr


def get_new_bytes():
    new_bytes_data = ebc.process_string(fr.security_pass, bg.fringe_byte_length)
    return new_bytes_data


def alter_batch_binary(parameter_dict_list):
    new_bytes_data = get_new_bytes()

    for element in parameter_dict_list:
        ebc.replace_byte_string(
            element["origin_absolute"], new_bytes_data, bg.fringe_byte_length + 10
        )
