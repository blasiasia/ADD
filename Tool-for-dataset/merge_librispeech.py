import os
import shutil

# 원본 폴더 경로
source_dir = '/mnt/aix23606/jiyoung/ADD/DS_LibriSpeech/dev-other'

# FLAC 파일 복사 대상 폴더
destination_dir = '/mnt/aix23606/jiyoung/ADD/DS_LibriSpeech/flac'

# 메타데이터 저장 파일 경로
metadata_file_path = '/mnt/aix23606/jiyoung/ADD/DS_LibriSpeech/metadata.txt'

# 새 폴더 생성
os.makedirs(destination_dir, exist_ok=True)

# 메타데이터 파일 열기
with open(metadata_file_path, 'w') as metadata_file:
    # 첫 번째 폴더 순회
    for spk_id_folder in os.listdir(source_dir):
        spk_path = os.path.join(source_dir, spk_id_folder)

        # 폴더인지 확인
        if os.path.isdir(spk_path):
            # 두 번째 폴더 순회
            for chapter_id_folder in os.listdir(spk_path):
                chapter_path = os.path.join(spk_path, chapter_id_folder)

                # 폴더인지 확인
                if os.path.isdir(chapter_path):
                    # FLAC 파일 순회
                    for file in os.listdir(chapter_path):
                        if file.endswith('.flac'):
                            source_file_path = os.path.join(chapter_path, file)
                            destination_file_path = os.path.join(destination_dir, file)

                            # 파일 복사
                            shutil.copy2(source_file_path, destination_file_path)

                            # 메타데이터 작성
                            metadata_line = f"{spk_id_folder} {file} - - bonafide\n"
                            metadata_file.write(metadata_line)

                            print(f"Copied: {source_file_path} -> {destination_file_path}")
                            print(f"Metadata: {metadata_line.strip()}")

print("모든 FLAC 파일 복사 및 메타데이터 생성이 완료되었습니다.")