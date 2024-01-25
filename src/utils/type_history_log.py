import os
import background_setting as bg
import gain_log_filename as glf
import search_root_path as srp


def write_content_to_file(txtfile, content):
    content = str(content).strip()

    if not os.path.exists(txtfile):
        with open(txtfile, "w") as f:
            pass
    with open(txtfile, "w") as f:
        f.write(content)


def remember_logger(content, regular_name="Excess-", extension_type=".json"):
    log_name = glf.gain_log_filename(regular_name, extension_type)

    history_filename = bg.project_root_directory + bg.separator
    history_filename += "ReportFolder"
    history_filename += bg.separator
    srp.check_create_directory(history_filename)

    history_filename += log_name
    write_content_to_file(history_filename, content)


def write_content_to_file2(txtfile, content):
    content = str(content).strip()

    if not os.path.exists(txtfile):
        with open(txtfile, "a") as f:
            pass
    with open(txtfile, "a") as f:
        f.write(content)


def trace_records(content, regular_name="Track-", extension_type=".txt"):
    log_name = glf.gain_log_filename2(regular_name, extension_type)

    history_filename = bg.project_root_directory + bg.separator
    history_filename += "ReportFolder"
    history_filename += bg.separator
    srp.check_create_directory(history_filename)

    history_filename += log_name
    write_content_to_file2(history_filename, content)
