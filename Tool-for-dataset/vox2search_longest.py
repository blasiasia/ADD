import os
import shutil
import csv
import subprocess
from collections import defaultdict

root_dir = "/mnt/aix23606/jiyoung/ADD/DS_VoxCeleb/vox2/dev/aac"
destination_dir = "/mnt/aix23606/jiyoung/ADD/DS_VoxCeleb/longest_one"
metadata_path = os.path.join(destination_dir, "metadata_aac2.txt")

os.makedirs(destination_dir, exist_ok=True)

duration_summary = defaultdict(int)
metadata_records = []

def get_duration_ffprobe(file_path):
    """ffprobe를 사용해 정확한 duration(초)을 구함"""
    try:
        result = subprocess.run(
            [
                "ffprobe", "-v", "error", "-show_entries",
                "format=duration", "-of", "default=noprint_wrappers=1:nokey=1",
                file_path
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return float(result.stdout.strip())
    except Exception as e:
        print(f"ffprobe 오류: {file_path}, 에러: {e}")
        return 0.0

for id_folder in os.listdir(root_dir):
    length = len(id_folder)
    count = 1

    id_path = os.path.join(root_dir, id_folder)
    if not os.path.isdir(id_path) or id_folder == "longest_one":
        continue

    max_duration = 0
    max_file_path = ""

    for subdir, _, files in os.walk(id_path):
        for file in files:
            if file.endswith(".m4a"):
                file_path = os.path.join(subdir, file)
                duration = get_duration_ffprobe(file_path)
                if duration > max_duration:
                    max_duration = duration
                    max_file_path = file_path

    if max_file_path:
        file_name = os.path.basename(max_file_path)
        print(f"[{count}/{length}]{id_folder} 폴더 내 최대 길이 파일: {file_name}, {int(max_duration)}초")

        relative_path = os.path.relpath(max_file_path, root_dir)
        new_file_name = f"{id_folder}.m4a"
        new_file_path = os.path.join(destination_dir, new_file_name)

        try:
            shutil.copy2(max_file_path, new_file_path)
        except Exception as e:
            print(f"파일 복사 실패: {max_file_path} → {new_file_path}, 에러: {e}")

        metadata_records.append([relative_path, new_file_name, int(max_duration)])

        if max_duration >= 90:
            duration_summary["90초 이상"] += 1
        else:
            bin_key = f"{int(max_duration // 10) * 10}초대"
            duration_summary[bin_key] += 1
    count += 1

with open(metadata_path, "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["original_file_path","new_file_name","duration(s)"])
    writer.writerows(metadata_records)

print("\n📊 전체 요약:")
for key in sorted(duration_summary.keys(), key=lambda x: int(x.split('초')[0]) if '이상' not in x else 999):
    print(f"{key} 파일: {duration_summary[key]}개")
