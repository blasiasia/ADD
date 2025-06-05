import os
import subprocess

def convert_m4a_to_wav(source_dir, target_dir):
    # 타겟 디렉토리가 없다면 생성
    os.makedirs(target_dir, exist_ok=True)

    # source_dir 내 모든 파일 탐색
    for filename in os.listdir(source_dir):
        if filename.lower().endswith('.m4a'):
            m4a_path = os.path.join(source_dir, filename)
            wav_filename = os.path.splitext(filename)[0] + '.wav'
            wav_path = os.path.join(target_dir, wav_filename)

            # ffmpeg 명령 실행
            command = ['ffmpeg', '-y', '-i', m4a_path, wav_path]
            try:
                subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                print(f"변환 완료: {filename} → {wav_filename}")
            except subprocess.CalledProcessError:
                print(f"⚠️ 변환 실패: {filename}")

# 사용 예시
source_folder = '/mnt/aix23606/jiyoung/ADD/DS_VoxCeleb/dev/longest_one/flac'  # .m4a 파일이 있는 폴더
target_folder = '/mnt/aix23606/jiyoung/ADD/DS_VoxCeleb/dev_longest_one_wav/flac'  # 변환된 .wav를 저장할 폴더

convert_m4a_to_wav(source_folder, target_folder)
