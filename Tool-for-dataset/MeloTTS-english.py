import os
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"
import sys
sys.path.append('/Users/hongjiyoung/MeloTTS')
import nltk
nltk.download('averaged_perceptron_tagger_eng')

from datasets import load_dataset
from melo.api import TTS

def generate_speech_from_text(text_list, output_folder, speaker_ids_list, device, metadata_file_path, speed=1.0):
    model = TTS(language='EN', device=device)
    speaker_ids = model.hps.data.spk2id
    
    # metadata 파일을 쓰기 위한 준비
    with open(metadata_file_path, 'w') as metadata_file:
        counter = 0  # 음성 파일 이름에 사용할 카운터

        # 폴더에서 .txt 파일을 하나씩 처리
        for text in text_list['prompt']:      
            # 음성 파일 생성 (여기서 speaker_id는 'EN-US', 'EN-BR' 등으로 설정)
            for accent, speaker_id in speaker_ids_list.items():
                # 6자리 숫자를 파일명에 사용 (e.g., 000001, 000002, ...)
                base_filename = str(counter).zfill(6)
                output_path = os.path.join(output_folder, f'E02_{accent}_{base_filename}.wav')
                
                # 음성 파일 생성
                model.tts_to_file(text, speaker_ids[speaker_id], output_path, speed=speed)
                print(f'Generated E02_{accent}_{base_filename}.wav at {output_path}')
                
                # metadata 파일에 기록
                metadata_file.write(f'{speaker_id} E02_{accent}_pmt_{base_filename} - E02 spoof\n')
            counter +=1


if __name__ == "__main__":
    speaker_ids_list = {
        'US': 'EN-US',
        'BR': 'EN-BR',
        'IN': 'EN_INDIA',
        'AU': 'EN-AU',
        'DE': 'EN-Default'
    }

    output_folder = '/Volumes/System/MeloTTS/flac'  # 생성된 음성 파일을 저장할 폴더 경로
    metadata_file_path = '/Volumes/System/MeloTTS/melotts_chatgpt.txt'  # metadata 파일 저장 경로
    speed = 1.0  # 음성 생성 속도 (기본 1.0)
    device = "cpu"
    ds = load_dataset("fka/awesome-chatgpt-prompts")

    generate_speech_from_text(ds['train'], output_folder, speaker_ids_list, device, metadata_file_path, speed)
