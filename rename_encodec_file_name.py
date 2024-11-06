import os
from pathlib import Path


def rename_encodec_file_name(folder_path):
    # 폴더 안의 모든 파일 읽기
    for filename in os.listdir(folder_path):
        if filename.endswith('.wav') or filename.endswith('.flac'):  # 오디오 파일만 처리
            # 파일명 예시: E01_19D_0000000.wav
            parts = filename.split('_')  # '_' 기준으로 분리
            
            if len(parts) == 3 :  # 올바른 형식의 파일명인지 확인
                # 기존 형식: ['E01', '19D', '0000000']
                # 새로운 형식으로 변경
                if parts[0] == "E01" : 
                    new_filename = f"{parts[0]}_01_{parts[1]}_{parts[2][1:]}"  # '01'을 앞에 추가
                elif parts[0] == "E02" : 
                    new_filename = f"E01_02_{parts[1]}_{parts[2][1:]}"  # '01'을 앞에 추가
                
                # 파일 경로 변경
                old_file_path = os.path.join(folder_path, filename)
                new_file_path = os.path.join(folder_path, new_filename)
                
                # 파일 이름 변경
                os.rename(old_file_path, new_file_path)
                print(f'Renamed: {filename} -> {new_filename}')


''' #E01_19D0000000 --> E01_19D_0000000으로 rename
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
'''

# 파일명이 있는 폴더 경로 지정
directory = r"e:\ADD\DS_SeRes2net\database01\flac_E"
rename_encodec_file_name(directory)
