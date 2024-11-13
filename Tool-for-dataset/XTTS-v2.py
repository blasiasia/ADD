import os
from datasets import load_dataset
from TTS.api import TTS

def xtts(text_list, output_folder, metadata_file_path, speaker_list, speaker_folder):
    model = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)
    
    # metadata 파일을 쓰기 위한 준비
    with open(metadata_file_path, 'w') as metadata_file:
        counter = 0  # 음성 파일 이름에 사용할 카운터

        # 폴더에서 .txt 파일을 하나씩 처리
        for text in text_list[:5]:      
            # 음성 파일 생성 (여기서 speaker_id는 'EN-US', 'EN-BR' 등으로 설정)
            for spk_file in speaker_list :
                #메타 데이터에도 들어갈 speaker id 설정
                parts = spk_file.split('_')
                spk_id = parts[0]

                # 6자리 숫자를 파일명에 사용 (e.g., 000001, 000002, ...)
                base_filename = str(counter).zfill(6)
                output_path = os.path.join(output_folder, f'E06_{spk_id}_wiki_{base_filename}.wav')
                speaker_path = os.path.join(speaker_folder, spk_file)

                # 음성 파일 생성
                # generate speech by cloning a voice using default settings
                model.tts_to_file(text=text,
                            file_path=output_path,
                            speaker_wav=speaker_path,
                            language="en")
                print(f'Generated E06_{spk_id}_wiki_{base_filename}.wav at {output_path}')
                
                # metadata 파일에 기록
                metadata_file.write(f'{spk_id} E06_{spk_id}_wiki_{base_filename} - E06 spoof\n')
            counter +=1


if __name__ == "__main__":
    output_folder = '/Volumes/System/XTTS-v2/ours/flac'  # 생성된 음성 파일을 저장할 폴더 경로
    metadata_file_path = '/Volumes/System/XTTS-v2/ours/E06_ours_wiki.txt'  # metadata 파일 저장 경로
    speaker_folder = '/Volumes/System/XTTS-v2/speaker'

    #chatgpt prompts dataset
    #ds = load_dataset("fka/awesome-chatgpt-prompts")

    #wikipedia prompts dataset
    #ds = load_dataset("567-labs/wikipedia-bge-small-en-v1.5-full")
    #sorted_dataset = ds.sort("id")

    #rewrite_too_prompts_3k_texts
    ds = load_dataset("positivethoughts/rewrite_500_prompts_3k_texts", data_files="prompts_0_500_wiki_first_para_3000.csv")
    print(len(ds['train']['original_text']))

    speaker_list = []
    for filename in os.listdir(speaker_folder):
        # .wav 확장자로 끝나는 파일인지 확인 후 리스트에 추가
        if (filename.endswith('.wav')or filename.endswith('.m4a')) and os.path.isfile(os.path.join(speaker_folder, filename)):
            speaker_list.append(filename)

    xtts(ds['train']['original_text'], output_folder, metadata_file_path, speaker_list, speaker_folder)
