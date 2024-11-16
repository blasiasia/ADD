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

    with open(meta_path, 'w') as meta_file:
        # 폴더 내 모든 파일을 순회하며 이름 변경
        for filename in os.listdir(folder_path):
            # 파일명 분리
            filename_parts = filename.split('_')
            if filename_parts[0]=='WF' :
                break

            if prefix == "CV" :
                key = filename_parts[1]
            else : 
                key = filename_parts[0]
            
            key = key.split('.')
            key = key[0]
            
            # 새 파일명 생성
            new_filename = f"WF_{prefix}_{key}"
            new_filename_wav = f"WF_{prefix}_{key}.wav"
            
            # 기존 파일의 전체 경로와 새 파일의 전체 경로
            old_file = os.path.join(folder_path, filename)
            new_file = os.path.join(folder_path, new_filename_wav)
            
            # 파일명 변경
            os.rename(old_file, new_file)
            print(f"Renamed: {filename} -> {new_filename_wav}")
            
            # 메타데이터 파일에 기록
            if prefix == "CV" :
                meta_entry = f"- {new_filename} - - spoof\n"
            else : 
                meta_entry = f"- {new_filename} - {prefix} spoof\n"

            meta_file.write(meta_entry)
    
    print("모든 파일명이 성공적으로 변경되었으며, 메타데이터 파일이 생성되었습니다.")


def write_wavefake_meta_file(folder_path, prefix, meta_path):
    
    with open(meta_path, 'w') as meta_file:
        for filename in os.listdir(folder_path):
            # 파일명 분리
            filename_parts = filename.split('.')

            meta_entry = f"- {filename_parts[0]} - {prefix} spoof\n"

            meta_file.write(meta_entry)
    
    print("메타데이터 파일이 생성되었습니다.")

def rename_WF_CV_files(folder_path):
# WF_CV_0 -> WF_CV_00000 형태로 파일명 변경하는 함수
    files = os.listdir(folder_path)
    
    for file in files:
        # 'WF_CV_'로 시작하는 파일만 필터링
        if file.startswith('WF_CV_'):
            # 기존 파일명에서 'WF_CV_'를 제외하고 숫자만 추출
            try:
                number = int(file.split('_')[2])  # 'WF_CV_' 뒤에 있는 숫자 부분
                new_name = f"WF_CV_{number:05d}"  # 5자리로 포맷팅

                # 파일의 전체 경로
                old_file_path = os.path.join(folder_path, file)
                new_file_path = os.path.join(folder_path, new_name)

                # 파일 이름 변경
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: {file} -> {new_name}")
            except ValueError:
                # 숫자가 아닌 파일은 무시
                continue

if __name__ == "__main__":
    folder_path = r'e:\ADD\DS_WaveFake\common_voices_prompts_from_conformer_fastspeech2_pwg_ljspeech\flac' 
    meta_path = r'e:\ADD\DS_WaveFake\common_voices_prompts_from_conformer_fastspeech2_pwg_ljspeech\WaveFake_CV.trn'   
    model_name = "CV"

    #파일명 변경과 메타파일 작성을 동시에
    change_wavefake(folder_path, model_name, meta_path)

    #메타파일 작성만
    #write_wavefake_meta_file(folder_path, model_name, meta_path)

    #Common Voice 파일명 재수정하는 함수
    #rename_WF_CV_files(folder_path)
