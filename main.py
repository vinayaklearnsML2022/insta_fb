
from insta_fb import bright_data

import pandas as pd



if __name__ == "__main__":


    bt_instance = bright_data()

    # instagram keyword search
    snap_shot = bt_instance.search_insta_keyword("GOAT movie")
    status = bt_instance.get_insta_fb_snapshot_initial_status(snap_shot)
    print(status)
    if status == "running":
        bt_instance.get_insta_snapshot(snap_shot)

    
    # fb keyword search
    snap_shot = bt_instance.search_fb_profile_url("BillGates")
    print(snap_shot)
    status = bt_instance.get_insta_fb_snapshot_initial_status(snap_shot)
    print(status)
    if status == "running":
        bt_instance.get_fb_snapshot(snap_shot)


 