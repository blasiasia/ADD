import csv

# 병합할 두 파일 경로
metadata_file_1 = "/mnt/aix23606/jiyoung/ADD/DS_VoxCeleb/longest_one/metadata_aac1.txt"
metadata_file_2 = "/mnt/aix23606/jiyoung/ADD/DS_VoxCeleb/longest_one/metadata_aac2.txt"

# 병합 결과 저장할 경로
merged_metadata_path = "/mnt/aix23606/jiyoung/ADD/DS_VoxCeleb/longest_one/merged_metadata.txt"

# 결과를 저장할 리스트
merged_records = []

# 헤더 포함 여부
header_written = False

with open(merged_metadata_path, "w", newline='', encoding="utf-8") as outfile:
    writer = csv.writer(outfile)

    for file_path in [metadata_file_1, metadata_file_2]:
        with open(file_path, "r", encoding="utf-8") as infile:
            reader = csv.reader(infile)
            header = next(reader)  # 첫 줄은 헤더
            if not header_written:
                writer.writerow(header)
                header_written = True
            for row in reader:
                writer.writerow(row)

print(f"✅ 병합 완료: {merged_metadata_path}")
