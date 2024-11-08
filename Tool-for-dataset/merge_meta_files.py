import os

def merge_meta_files(meta_dir, output_file):
    # output_file 초기화
    with open(output_file, "w") as outfile:
        # meta_dir의 모든 파일 순회
        for file_name in os.listdir(meta_dir):
            file_path = os.path.join(meta_dir, file_name)
            # 파일이 .csv 또는 .trn로 끝나는지 확인
            if os.path.isfile(file_path) and (file_path.endswith(".csv") or file_path.endswith(".trn")):
                with open(file_path, "r") as infile:
                    lines = infile.readlines()
                    outfile.writelines(lines)
                print(f"Added {file_name} to {output_file}")

if __name__ == "__main__":
    meta_dir = r'e:\ADD\DS_Ours\database01\metadata'  # 메타데이터 파일들이 들어 있는 폴더
    output_file = r'e:\ADD\DS_Ours\database01\db01_eval_meta.trn'  # 결과를 저장할 파일

    merge_meta_files(meta_dir, output_file)
