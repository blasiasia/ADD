import csv
import os

def update_metadata_to_wav(csv_path, new_csv_path):
    with open(csv_path, 'r', newline='', encoding='utf-8') as infile, \
         open(new_csv_path, 'w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            old_name = row['new_file_name']
            row['new_file_name'] = os.path.splitext(old_name)[0] + '.wav'
            writer.writerow(row)
        print(f"✅ 새 metadata 저장 완료: {new_csv_path}")

# 사용 예시
csv_path = '/mnt/aix23606/jiyoung/ADD/DS_VoxCeleb/dev/longest_one/merged_metadata.txt'
new_csv_path = '/mnt/aix23606/jiyoung/ADD/DS_VoxCeleb/dev_longest_one_wav/metadata_wav.txt'

update_metadata_to_wav(csv_path, new_csv_path)
