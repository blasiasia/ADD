import os
def change_in_the_wild_meta(dir_meta, save_path):

    with open(save_path, "w") as fh:

        with open(dir_meta, "r") as f:
            l_meta = f.readlines()[1:]

        for line in l_meta:
            fname, spk_id, label = line.strip().split(",")
            fname = fname.replace(".wav", "")  # 확장자 .wav 제거
            fname = "In_the_wild_" + fname

            spk_id = spk_id.replace(" ", "_")

            if label == "bona-fide" : 
                label = label.replace("-", "")

            fh.write("{} {} - - {}\n".format(spk_id, fname, label))

if __name__ == "__main__":
    dir_meta = r"C:\Users\jiyoung\asvspoof5\database\In_the_wild.csv"
    save_path = r"C:\Users\jiyoung\asvspoof5\database\new_In_the_wild.trn"

    change_in_the_wild_meta(dir_meta, save_path)