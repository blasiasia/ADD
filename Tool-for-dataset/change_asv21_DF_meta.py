import os

# 메타데이터 파일 경로 설정
input_file = "/mnt/aix23606/jiyoung/ADD/ASVspoof2021_DF_eval/trial_metadata.txt"
output_file = "/mnt/aix23606/jiyoung/ADD/ASVspoof2021_DF_eval/metadata.txt"
directory_path = "/mnt/aix23606/jiyoung/ADD/ASVspoof2021_DF_eval/flac"

# 메타데이터 불러오기
with open(input_file, "r") as f:
    lines = f.readlines()

# 메타데이터 수정 및 파일 존재 여부 확인
modified_lines = []
for line in lines:
    parts = line.strip().split(" ")  # 각 항목 분리
    filename = parts[1]               # 두 번째 항목이 파일명
    full_path = os.path.join(directory_path, f"{filename}.flac")  # 파일의 전체 경로 생성

    if os.path.exists(full_path):  # 파일이 실제로 존재하는지 확인
        modified_line = f"- {filename}.flac - - {parts[5]}\n"  # 새로운 형식으로 작성
        modified_lines.append(modified_line)

# 수정된 메타데이터 저장
with open(output_file, "w") as f:
    f.writelines(modified_lines)

print(f"Modified metadata saved to {output_file}")