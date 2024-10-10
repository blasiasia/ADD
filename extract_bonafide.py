import shutil
import os

def genBonafide_list(database_path, save_path):
    dir_meta = os.path.join(database_path, r"ASVspoof2019_PA_cm_protocols", "ASVspoof2019.PA.cm.dev.trl.txt")
    flac_path = os.path.join(database_path, r"ASVspoof2019_PA_dev", "flac")
    txt_save_path = os.path.join(save_path, r"ASVspoof2019.PA.cm.dev_Bonafide.trn")

    with open(txt_save_path, "w") as fh:
        with open(dir_meta, "r") as f:
            l_meta = f.readlines()

        for line in l_meta:
            spk_id, fname, _, _, label = line.strip().split(" ")  # 불필요한 중간 열 제거

            if label == "bonafide" :
                
                fh.write("{} {} - - {}\n".format(spk_id, fname, label))
                
                file_path = os.path.join(flac_path, f"{fname}.flac")
                destination_path = os.path.join(save_path, "flac", f"{fname}.flac")

                # 파일 존재 여부 확인
                if not os.path.exists(destination_path):
                    os.makedirs(os.path.dirname(destination_path), exist_ok=True)

                if os.path.exists(file_path):
                    try:
                        # 파일 이동
                        shutil.copy(file_path, destination_path)
                        print(f"파일 '{fname}'을(를) '{file_path}'에서 '{destination_path}'로 성공적으로 이동했습니다.")
                    except Exception as e:
                        print(f"파일 이동 중 오류 발생: {e}")
                else:
                    print(f"'{fname}' 파일을 '{file_path}'에서 찾을 수 없습니다.")

if __name__ == "__main__":
    database_path = r"c:\Users\jiyoung\DS_ASVspoof2019\PA"
    save_path = r"c:\Users\jiyoung\DS_ASVspoof2019\PA\ASVspoof2019_PA_dev_Bonafide"

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    genBonafide_list(database_path, save_path)