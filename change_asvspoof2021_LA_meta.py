import os
def change_asvspoof2021_LA_meta(dir_meta, save_path):

    with open(save_path, "w") as fh:

        with open(dir_meta, "r") as f:
            l_meta = f.readlines()[1:]

        for line in l_meta:
            fname = line.strip()

            fh.write("# {} - - #\n".format(fname))

if __name__ == "__main__":
    dir_meta = r'/Volumes/Seagate Expansion Drive/ADD/asvspoof5/database/In_the_wild.csv'
    save_path = r'/Users/hongjiyoung/ADD/new_In_the_wild.trn'

    change_asvspoof2021_LA_meta(dir_meta, save_path)