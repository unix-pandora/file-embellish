import time
import background_setting as bg


def forge_note_name():
    label = bg.backup_log_label
    extension_type = bg.backup_log_extension

    timestamp = time.time()

    note_file_name = str(label).strip()
    note_file_name += str(timestamp).strip()
    note_file_name += str(extension_type).strip()
    
    return note_file_name


def gain_log_filename(label="Identify-", extension_type=".txt"):
    timestamp = time.time()

    log_file_name = str(label).strip()
    log_file_name += str(timestamp).strip()
    log_file_name += str(extension_type).strip()

    print("Identify_log_file_name: ", log_file_name)
    return log_file_name


def gain_log_filename2(label="Vestige-", extension_type=".txt"):
    timestamp = int(time.time())

    log_file_name = str(label).strip()
    log_file_name += str(timestamp).strip()
    log_file_name += str(extension_type).strip()

    print("Vestige_log_file_name: ", log_file_name)
    return log_file_name