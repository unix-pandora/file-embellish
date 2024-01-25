import endurance_binary_content as ebc
import background_setting as bg
import front_reception as fr


def gain_new_bytes():
    new_bytes_data = ebc.process_string(fr.security_pass, bg.fringe_byte_length)
    return new_bytes_data


def revamp_batch_binary(parameter_dict_array):
    new_bytes_data = gain_new_bytes()

    for element in parameter_dict_array:
        ebc.insert_bytes_at_start(element["origin_absolute"], new_bytes_data)
