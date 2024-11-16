# 파일 경로 설정
input_metadata_path = "e:\ADD\DS_ASVspoof2019\LA\ASVspoof2019_LA_eval_Bonafide\ASVspoof2019.LA.cm.eval_Bonafide.trn"
output_metadata_path = "e:\ADD\DS_ASVspoof2019\LA\ASVspoof2019_LA_eval_Bonafide\metadata.txt"

# 파일 열고 메타데이터 수정하기
with open(input_metadata_path, 'r') as input_file, open(output_metadata_path, 'w') as output_file:
    for line in input_file:
        # 공백을 기준으로 분리
        parts = line.strip().split(' ')
        
        # 파일명을 수정 (여기서는 예시로 '_mod' 추가)
        if len(parts) > 1:
            parts[1] = parts[1] + '.flac'
        
        # 수정된 줄을 다시 조합해서 출력 파일에 작성
        modified_line = ' '.join(parts) + '\n'
        output_file.write(modified_line)

print("파일명이 수정된 메타데이터가 저장되었습니다.")
