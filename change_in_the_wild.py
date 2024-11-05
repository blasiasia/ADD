import os
import shutil

def change_in_the_wild_meta(dir_meta, audio_dir, new_audio_dir, new_dir_meta):
    # 새 오디오 폴더 생성
    os.makedirs(new_audio_dir, exist_ok=True)

    with open(new_dir_meta, "w") as fh:
        with open(dir_meta, "r") as f:
            l_meta = f.readlines()[1:]

        for line in l_meta:
            fname, spk_id, label = line.strip().split(",")
            original_fname = fname  # 원본 파일명 저장
            fname = fname.replace(".wav", "")  # 확장자 .wav 제거
            new_fname = "In_the_wild_" + fname  # 새로운 파일명 생성

            # 오디오 파일의 경로 설정
            old_audio_path = os.path.join(audio_dir, original_fname)
            new_audio_path = os.path.join(new_audio_dir, new_fname + ".wav")

            # 파일 복사 후 이름 변경
            if os.path.exists(old_audio_path):
                shutil.copy(old_audio_path, new_audio_path)
                print(f"Copied and renamed: {old_audio_path} -> {new_audio_path}")
            else:
                print(f"File not found: {old_audio_path}")

            spk_id = spk_id.replace(" ", "_")
            if label == "bona-fide": 
                label = label.replace("-", "")

            # 수정된 정보로 새로운 파일에 기록
            fh.write("{} {} - - {}\n".format(spk_id, new_fname, label))

if __name__ == "__main__":
    dir_meta = r'E:\ADD\In_the_wild\In_the_wild.csv'
    audio_dir = r'E:\ADD\In_the_wild\flac'
    new_audio_dir = r'E:\ADD\new_In_the_wild\flac'
    new_dir_meta = r'E:\ADD\new_In_the_wild\In_the_wild.trn'

    change_in_the_wild_meta(dir_meta, audio_dir, new_audio_dir, new_dir_meta)


'''
import os
def change_in_the_wild_meta(dir_meta, save_path):

    with open(save_path, "w") as fh:

        with open(dir_meta, "r") as f:
            l_meta = f.readlines()[1:]

        for line in l_meta:
            fname, spk_id, label = line.strip().split(",")
            fname = fname.replace(".wav", "")  # 확장자 .wav 제거
            fname = "In_the_wild_" + fname

            spk_id = spk_id.replace(" ", "_")

            if label == "bona-fide" : 
                label = label.replace("-", "")

            fh.write("{} {} - - {}\n".format(spk_id, fname, label))

if __name__ == "__main__":
    dir_meta = r'/Volumes/Seagate Expansion Drive/ADD/asvspoof5/database/In_the_wild.csv'
    save_path = r'/Users/hongjiyoung/ADD/new_In_the_wild.trn'

    change_in_the_wild_meta(dir_meta, save_path)
    '''