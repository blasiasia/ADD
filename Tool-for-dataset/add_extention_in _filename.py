# 파일 경로 설정
input_metadata_path = "/mnt/aix23606/jiyoung/ADD/DS_E05_Elevenlabs/meta_tts_final.txt"
output_metadata_path = "/mnt/aix23606/jiyoung/ADD/DS_E05_Elevenlabs/metadata.txt"

# 파일 열고 메타데이터 수정하기
with open(input_metadata_path, 'r') as input_file, open(output_metadata_path, 'w') as output_file:
    for line in input_file:
        # 공백을 기준으로 분리
        parts = line.strip().split(' ')
        
        # 파일명을 수정 (여기서는 예시로 '_mod' 추가)
        if len(parts) > 1:
            parts[1] = parts[1] + '.wav'
        
        # 수정된 줄을 다시 조합해서 출력 파일에 작성
        modified_line = ' '.join(parts) + '\n'
        output_file.write(modified_line)

print("파일명이 수정된 메타데이터가 저장되었습니다.")
