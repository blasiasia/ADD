import os

def change_wavefake(folder_path, prefix, meta_path):
    """
    폴더 내 오디오 파일들을 새 파일명 형식으로 일괄 변경하고, 메타데이터 파일을 생성하는 함수입니다.
    
    Parameters:
    - folder_path (str): 오디오 파일이 있는 폴더의 경로
    - prefix (str): 파일명에 추가할 사용자 입력 단어
    - meta_path (str): 메타데이터를 저장할 파일 경로
    
    Example:
    change_wavefake('path/to/folder', 'FB', 'path/to/meta.txt')
    """
    
    # 메타데이터 파일을 쓰기 모드로 엽니다.
    with open(meta_path, 'w') as meta_file:
        # 폴더 내 모든 파일을 순회하며 이름 변경
        for filename in os.listdir(folder_path):
            # 파일명 분리
            filename_parts = filename.split('_')
            if prefix == "CV" :
                key = filename_parts[1]
            else : 
                key = filename_parts[0]
            
            # 새 파일명 생성
            new_filename = f"WF_{prefix}_{key}"
            
            # 기존 파일의 전체 경로와 새 파일의 전체 경로
            old_file = os.path.join(folder_path, filename)
            new_file = os.path.join(folder_path, new_filename)
            
            # 파일명 변경
            os.rename(old_file, new_file)
            print(f"Renamed: {filename} -> {new_filename}")
            
            # 메타데이터 파일에 기록
            meta_entry = f"# {new_filename} - {prefix} spoof\n"
            meta_file.write(meta_entry)
    
    print("모든 파일명이 성공적으로 변경되었으며, 메타데이터 파일이 생성되었습니다.")


folder_path = '파일이_저장된_폴더_경로' 
meta_path = '메타데이터_파일_경로'   
model_name = "FB"
change_wavefake(folder_path, model_name, meta_path)
