import os
def change_asvspoof2021_LA_meta(dir_meta, save_path):

    with open(save_path, "w") as fh:

        with open(dir_meta, "r") as f:
            l_meta = f.readlines()[1:]

        for line in l_meta:
            fname = line.strip()

            fh.write("# {} - - #\n".format(fname))

if __name__ == "__main__":
    dir_meta = r'E:\ADD\DS_ASVspoof2021\ASVspoof2021_LA_eval/ASVspoof2021.LA.cm.eval.trl.txt'
    save_path = r'E:\ADD\DS_ASVspoof2021\ASVspoof2021_LA_eval/new_ASVspoof2021.LA.cm.eval.trl.txt'

    change_asvspoof2021_LA_meta(dir_meta, save_path)