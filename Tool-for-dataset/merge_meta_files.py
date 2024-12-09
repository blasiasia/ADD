import os

def merge_meta_files(meta_dir, output_file):
    # output_file 초기화
    with open(output_file, "w") as outfile:
        # meta_dir의 모든 파일 순회
        for file_name in os.listdir(meta_dir):
            file_path = os.path.join(meta_dir, file_name)
            # 파일이 .csv 또는 .trn로 끝나는지 확인
            if os.path.isfile(file_path) and not file_name.startswith("._") and (file_path.endswith(".csv") or file_path.endswith(".trn")or file_path.endswith(".txt")):
                with open(file_path, "r", encoding='iso-8859-1') as infile:
                    lines = infile.readlines()
                    outfile.writelines(lines)
                print(f"Added {file_name} to {output_file}")

if __name__ == "__main__":
    meta_dir = r'/mnt/aix23606/jiyoung/ADD/DS_Ours/db04_2/metadata'  # 메타데이터 파일들이 들어 있는 폴더
    output_file = r'/mnt/aix23606/jiyoung/ADD/DS_Ours/db04_2/train_meta.txt'  # 결과를 저장할 파일

    merge_meta_files(meta_dir, output_file)
