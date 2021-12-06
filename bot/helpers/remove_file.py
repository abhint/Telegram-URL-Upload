import os


def remove_file(path):
    try:
        os.remove(path)
    except FileExistsError or FileNotFoundError as err:
        print(err)
