import os

import type_history_log as thl


def rename_file_or_folder(old_path, new_path):
    try:
        os.rename(old_path, new_path)
    except Exception as e:
        print("Rename failure, causation:", e)
        thl.trace_records(e, "Exception-", ".log")
