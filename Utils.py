import datetime

control_data="db_load/db_user.txt"
status = {1, 0}

def get_last(db_file):
    with open(db_file, "r") as f:
        last_line = f.readlines()[-1]
    return last_line

def save_in_file(db_file, data):
    with open(db_file, "a") as f:
        f.writelines(data+"\n")

def get_date():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def check_user(name, password):
    with open(control_data, "r") as f:
        data = f.readlines()
    for line in data:
        if name in line and password in line:
            return True 
    return False

def get_plot_data(db_file):
    with open(db_file, "r") as f:
        data = f.readlines()
    return data

def register_lote(db_file, lote):
    with open(db_file, "a") as f:
        f.writelines(lote+"\n")

def get_data(db_file):
    with open(db_file, "r") as f:
        data = f.readlines()
    return data

def delete_data(db_file, data):
    with open(db_file, "w") as f:
        for line in data:
            if line != data:
                f.writelines(line)


