import os
from pydub import AudioSegment

# ffmpeg 경로를 pydub에서 사용할 수 있도록 지정
AudioSegment.converter = "/opt/homebrew/bin/ffmpeg"


def slice_audio_files_from_metadata(metadata_file, input_folder, output_folder, segment_duration=10, new_metadata_file="new_metadata.txt"):
    """
    메타데이터 파일에서 파일명을 읽어와서 지정된 폴더 내의 wav 파일을 10초 단위로 자르고 저장하며,
    새로운 파일명으로 메타데이터를 업데이트합니다.

    Args:
    - metadata_file (str): 오디오 파일명이 저장된 메타데이터 파일 경로.
    - input_folder (str): 원본 wav 파일들이 있는 폴더 경로.
    - output_folder (str): 잘라낸 오디오 파일을 저장할 폴더 경로.
    - segment_duration (int): 잘라낼 구간의 길이(초 단위).
    - new_metadata_file (str): 새로 작성할 메타데이터 파일 경로.
    """
    # 출력 폴더가 없으면 생성
    os.makedirs(output_folder, exist_ok=True)
    counter = 0  # 음성 파일 이름에 사용할 카운터
    new_metadata_lines = []  # 새로운 메타데이터를 저장할 리스트

    # 메타데이터 파일을 읽어서 파일명 리스트를 가져옵니다.
    with open(metadata_file, 'r') as f:
        file_list = f.readlines()

    # 메타데이터 파일에서 파일명을 하나씩 처리
    for line in file_list:
        parts = line.strip().split()  # 공백 기준으로 나누기
        if len(parts) < 3:
            continue  # 잘못된 형식일 경우 건너뛰기

        # 기존 메타데이터에서 spk_id, model, spoof 값을 가져옵니다.
        spk_id = parts[0]

        # 두 번째 항목이 실제 파일명입니다.
        filename = parts[1]

        print(f"Processing: {filename}")
        filepath = os.path.join(input_folder, f'{filename}.wav')
        
        # 파일이 존재하는지 확인
        if not os.path.exists(filepath):
            print(f"File {filename} not found in {input_folder}. Skipping...")
            continue
        
        audio = AudioSegment.from_wav(filepath)
        
        # 파일명을 '_' 기준으로 분리
        parts = filename.split('_')
        # 10초 = 10000ms
        segment_duration_ms = segment_duration * 1000
        audio_length = len(audio)
        
        # 10초씩 잘라서 저장
        for i in range(0, audio_length, segment_duration_ms):
            segment = audio[i:i+segment_duration_ms]
            segment_filename = str(counter).zfill(6)
            new_filename = f'{parts[0]}_{parts[1]}_{parts[2]}_{segment_filename}'
            segment_filepath = os.path.join(output_folder, f'{new_filename}.wav')
            segment.export(segment_filepath, format="wav")
            print(f"Saved: {segment_filepath}")
            counter += 1
            
            # 새로운 메타데이터에 새 파일명 추가
            new_metadata_lines.append(f"{spk_id} {new_filename} - {parts[0]} spoof\n")

    # 새로운 메타데이터 파일로 저장
    with open(new_metadata_file, 'w') as f:
        f.writelines(new_metadata_lines)


metadata_file = "/Volumes/System/MeloTTS/wikipedia/old_melotts_wiki_meta.txt"  # 기존 메타데이터 파일 경로
input_folder = "/Volumes/System/MeloTTS/wikipedia/flac2"  # 원본 파일들이 있는 폴더 경로

output_folder = "/Volumes/System/MeloTTS/wikipedia/flac"  # 잘라낸 파일들을 저장할 폴더 경로
new_metadata_file = "/Volumes/System/MeloTTS/E02_wiki.txt"  # 새로운 메타데이터 파일 경로

slice_audio_files_from_metadata(metadata_file, input_folder, output_folder, segment_duration=10, new_metadata_file=new_metadata_file)
