import os
from pathlib import Path

def rename_encodec_file_name(directory):
    # Path 객체로 폴더 지정
    directory = Path(directory)
    print(f"Checking directory: {directory}")
    # 폴더 안의 모든 파일 탐색
    for file_path in directory.glob("*.wav"):
        file_name = file_path.stem  # 확장자를 제외한 파일명만 추출
        ext = file_path.suffix      # 확장자 (.wav)
        
        # 파일명이 "E01_19D0000000" 형식인지 확인
        if file_name.startswith("E") and len(file_name) == 14 :
            # 새로운 파일명 생성: "E01_19D_0000000" 형식
            new_name = f"{file_name[:7]}_{file_name[7:]}{ext}"
            new_file_path = file_path.parent / new_name
            
            # 파일명 변경
            file_path.rename(new_file_path)
            print(f"Renamed: {file_path} -> {new_file_path}")
        else:
            print(f"Skipped: {file_path} (format already correct or unmatched)")

# 파일명이 있는 폴더 경로 지정
directory = r"e:\ADD\DS_SeRes2net\database01\flac_E"
rename_encodec_file_name(directory)
