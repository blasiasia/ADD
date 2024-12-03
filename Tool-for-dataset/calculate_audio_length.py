from pydub import AudioSegment
import os
import librosa
import pandas as pd

# 폴더 경로: 음성 파일이 들어있는 폴더
folder_path = '/mnt/aix23606/jiyoung/ADD/DS_ASVspoof2019LA/ASVspoof2019_LA_eval/flac'

# 결과 저장 리스트 초기화
audio_lengths = []

# 총 길이를 초 단위로 저장
total_duration_seconds = 0

# 파일 목록 가져오기
file_list = [f for f in os.listdir(folder_path) if f.endswith('.wav') or f.endswith('.flac')]

# 총 파일 개수
total_files = len(file_list)
print(f"Processing {total_files} audio files...")

# 폴더 내 파일 확인 및 처리
for idx, file_name in enumerate(file_list, 1):  # 1부터 시작하는 인덱스
    file_path = os.path.join(folder_path, file_name)
    try:
        # 음성 파일 불러오기
        audio = AudioSegment.from_file(file_path)
        duration = len(audio) / 1000  # 밀리초를 초로 변환
        minutes = int(duration // 60)
        seconds = int(duration % 60)
        total_duration_seconds += duration
        audio_lengths.append({'File Name': file_name, 'Duration (min:sec)': f"{minutes}:{seconds}"})
        
        # 진행 상황 출력
        print(f"[{idx}/{total_files}] Processed: {file_name} ({minutes}m {seconds}s)")
    except Exception as e:
        audio_lengths.append({'File Name': file_name, 'Duration (min:sec)': 'Error'})
        print(f"[{idx}/{total_files}] Error processing {file_name}: {e}")

# 총 시간 계산
total_minutes = int(total_duration_seconds // 60)
total_seconds = int(total_duration_seconds % 60)

# 결과를 데이터프레임으로 저장
df_audio_lengths = pd.DataFrame(audio_lengths)

# 총 시간 계산 (이미 df 만들고 돌려야함)
# 데이터를 활용해 총 초 단위 시간 계산
total_seconds = sum(
    int(duration.split(':')[0]) * 60 + int(duration.split(':')[1])
    for duration in df_audio_lengths['Duration (min:sec)']
    if duration != 'Error'
)

# 시간, 분, 초로 변환
total_hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
total_minutes = remaining_seconds // 60
total_seconds = remaining_seconds % 60

print(f"Total Duration: {total_hours} hours {total_minutes} minutes {total_seconds} seconds")