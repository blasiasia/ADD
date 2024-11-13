import os

# 파일이 포함된 폴더 경로와 삭제할 파일 이름 접두어 지정
folder_path = '/path/to/your/folder'  # 폴더 경로
file_prefix = 'E02_US'  # 삭제할 파일 이름 접두어

# 폴더 내의 모든 파일을 확인하여, 지정한 접두어로 시작하는 파일 삭제
for filename in os.listdir(folder_path):
    if filename.startswith(file_prefix):
        file_path = os.path.join(folder_path, filename)
        try:
            os.remove(file_path)  # 파일 삭제
            print(f"Deleted: {filename}")
        except Exception as e:
            print(f"Error deleting {filename}: {e}")
