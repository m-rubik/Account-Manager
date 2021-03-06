"""!
All functions related to the generation and storing of AlphaVantage keys.

# https://www.alphavantage.co/documentation/
# https://github.com/RomelTorres/alpha_vantage
# https://alpha-vantage.readthedocs.io/en/latest/genindex.html
# https://alpha-vantage.readthedocs.io/en/latest/source/alpha_vantage.html#module-alpha_vantage.timeseries
"""

from pytrademl.utilities.object_utilities import import_object, export_object
from pathlib import Path
root_dir = Path(__file__).resolve().parent.parent

def add_key(key):
    """!
    Add a new key to the list.
    """
    key_list = import_object(root_dir / "KEYS")
    if key_list:
        if key in key_list:
            print("Key", key, "already stored.")
            flag = 0
        else:
            key_list.append(key)
            flag = export_object(root_dir / "KEYS", key_list)
    else:
        print("Generating new key list.")
        key_list = list()
        key_list.append(key)
        flag = export_object(root_dir / "KEYS", key_list)
    return flag

def load_key(index=0):
    """!
    Load a key in the list by index
    """
    print(root_dir)
    key_list = import_object(root_dir / "KEYS")
    if key_list:
        print("Found available keys:", key_list)
        return key_list[index]
    else:
        return None

def remove_key(key):
    key_list = import_object(root_dir / "KEYS")
    if key_list:
        if key in key_list:
            key_list.remove(key)
            flag = export_object(root_dir / "KEYS", key_list)
        else:
            print("Key", key, "not found.")
            flag = 0
    else:
        flag = 1
    return flag

def unittest():
    add_key("test")
    print(load_key())
    remove_key('test')

if __name__ == "__main__":
    # add_key("XXXXXXXXXXXXXXXXX")
    print(load_key())
