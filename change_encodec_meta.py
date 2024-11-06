def modify_metadata(input_metadata_path, output_metadata_path):
    # 입력 파일을 열고, 출력 파일을 준비합니다.
    with open(input_metadata_path, 'r') as infile, open(output_metadata_path, 'w') as outfile:
        for line in infile:
            # 한 줄씩 읽고, 공백 기준으로 나눕니다.
            parts = line.strip().split(' ')
            
            if len(parts) == 5:
                speaker_id = parts[0]  # 예: LA_0030
                filename = parts[1]     # 예: E01_19E_0000000

                # 파일명 변경: E01_19E_0000000 -> E01_01_19E_000000
                filename_parts = filename.split('_')
                if len(filename_parts) == 3:
                    if filename_parts[0] == "E01":
                        new_filename = f"{filename_parts[0]}_01_{filename_parts[1]}_{filename_parts[2][1:]}"  # 첫 번째 자리 숫자 제거
                        # 수정된 파일명으로 새로운 라인 작성
                        new_line = f"{speaker_id} {new_filename} {parts[2]} {parts[3]}_01 {parts[4]}\n"

                    elif filename_parts[0] == "E02":
                        new_filename = f"E01_02_{filename_parts[1]}_{filename_parts[2][1:]}"  # E02 -> E01_02로 변환
                        # 수정된 파일명으로 새로운 라인 작성
                        new_line = f"{speaker_id} {new_filename} {parts[2]} E01_02 {parts[4]}\n"
                else:
                    new_filename = filename  # 형식이 맞지 않으면 변경하지 않음

                outfile.write(new_line)  # 새로운 metadata 파일에 기록

    print("Metadata 수정 완료.")


input_metadata_path = 'E:/ADD/DS_Encodec/ASVspoof2019_LA_train_Spoof/E02_19train_spoof.csv'  # 기존 metadata 파일 경로
output_metadata_path = 'E:/ADD/DS_Encodec/ASVspoof2019_LA_train_Spoof/new_E01_02_19train_spoof.csv'  # 수정된 metadata 파일 저장 경로

modify_metadata(input_metadata_path, output_metadata_path)
