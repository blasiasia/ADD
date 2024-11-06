import os
from melo.api import TTS

def generate_speech_from_text(input_folder, output_folder, speaker_ids, device, metadata_file_path, speed=1.0):
    # TTS 모델 인스턴스 생성
    model = TTS(language='EN', device=device)
    
    # metadata 파일을 쓰기 위한 준비
    with open(metadata_file_path, 'w') as metadata_file:
        counter = 0  # 음성 파일 이름에 사용할 카운터

        # 폴더에서 .txt 파일을 하나씩 처리
        for txt_file in os.listdir(input_folder):
            if txt_file.endswith('.txt'):  # .txt 파일만 처리
                txt_file_path = os.path.join(input_folder, txt_file)
                
                # 텍스트 파일 내용 읽기
                with open(txt_file_path, 'r') as f:
                    text = f.read().strip()

                # 음성 파일 생성 (여기서 speaker_id는 'EN-US', 'EN-BR' 등으로 설정)
                for accent, speaker_id in speaker_ids.items():
                    # 6자리 숫자를 파일명에 사용 (e.g., 000001, 000002, ...)
                    base_filename = str(counter).zfill(6)
                    output_path = os.path.join(output_folder, f'E02_{accent}_19T_{base_filename}.wav')
                    
                    # 음성 파일 생성
                    model.tts_to_file(text, speaker_id, output_path, speed=speed)
                    print(f'Generated {speaker_id} speech for "{txt_file}" at {output_path}')
                    
                    # metadata 파일에 기록
                    metadata_file.write(f'{speaker_id} E02_{accent}_19T_{base_filename} - E02_{accent} spoof')


if __name__ == "__main__":
    device = 'mps'  # 장치 설정 (mps, cpu, cuda 등)
    speaker_ids = {
        'US': 'EN-US',
        'BR': 'EN-BR',
        'IN': 'EN-INDIA',
        'AU': 'EN-AU',
        'DE': 'EN-Default'
    }

    input_folder = 'path/to/your/text/files'  # 텍스트 파일들이 들어 있는 폴더 경로
    output_folder = 'path/to/your/output/folder'  # 생성된 음성 파일을 저장할 폴더 경로
    metadata_file_path = 'path/to/your/output/folder/metadata.txt'  # metadata 파일 저장 경로
    speed = 1.0  # 음성 생성 속도 (기본 1.0)

    generate_speech_from_text(input_folder, output_folder, speaker_ids, device)
