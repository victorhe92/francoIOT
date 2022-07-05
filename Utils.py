control_data="db_load/db_user.txt"
status = {1, 0}

def get_last(db_file):
    with open(db_file, "r") as f:
        last_line = f.readlines()[-1]
    return last_line

def save_in_file(db_file, data):
    with open(db_file, "a") as f:
        f.writelines(data+"\n")