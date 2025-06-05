import pandas as pd
from datasets import load_dataset
import random
import re

# 시드 고정 (재현성 확보)
random.seed(42)

# 텍스트 정제 함수
def clean_text(text):
    # 줄바꿈, 탭 등을 공백으로 대체
    text = re.sub(r"[\n\r\t]", " ", text)
    # 영어, 숫자, 공백, 일반적인 구두점 외 제거
    text = re.sub(r"[^a-zA-Z0-9\s.,!?;:'\"()-]", "", text)
    # 연속된 공백을 하나로 줄이기
    text = re.sub(r"\s+", " ", text)
    return text.strip()

# metadata.csv 경로
csv_path = "/mnt/aix23606/jiyoung/ADD/DS_VoxCeleb/dev_longest_one_wav/metadata_wav.txt"
df = pd.read_csv(csv_path)

# Huggingface 데이터셋 로드
dataset = load_dataset("Amod/mental_health_counseling_conversations", split="train")
responses = dataset["Response"]

print("metadata_wav.txt에서 읽은 행 수:", len(df))
print("Response 개수:", len(responses))

# manifest.tsv에 들어갈 행 생성
rows = []
for _, row in df.iterrows():
    audio_name = row["new_file_name"]
    speaker = audio_name.replace(".wav", "")
    duration = row["duration(s)"]

    # responses에서 랜덤하게 2개 선택
    sampled_responses = random.sample(responses, 2)

    for i, response in enumerate(sampled_responses):
        cleaned_response = clean_text(response)  # 정제된 텍스트 적용
        rows.append({
            "audio_name": audio_name,
            "text": cleaned_response,
            "prompt_end_sec": duration,
            "speaker": speaker,
            "save_name": f"E06_{speaker}_mhcc_{i+1}.wav",
            "word_indices": "0"
        })

# DataFrame으로 만들고 저장
manifest_df = pd.DataFrame(rows)
manifest_df.to_csv("manifest.csv", index=False, encoding="utf-8", sep="\t")

print(f"✅ manifest.tsv 파일이 생성되었습니다. 총 {len(manifest_df)}개의 행이 저장되었습니다.")


'''
import pandas as pd
from datasets import load_dataset
import random

# 시드 고정 (재현성 확보)
random.seed(42)

# metadata.csv 경로
csv_path = "/mnt/aix23606/jiyoung/ADD/DS_VoxCeleb/dev_longest_one_wav/metadata_wav.txt"
df = pd.read_csv(csv_path)

# Huggingface 데이터셋 로드
dataset = load_dataset("Amod/mental_health_counseling_conversations", split="train")
responses = dataset["Response"]

print("metadata_wav.txt에서 읽은 행 수:", len(df))
print("Response 개수:", len(responses))

# manifest.tsv에 들어갈 행 생성
rows = []
for _, row in df.iterrows():
    audio_name = row["new_file_name"]
    speaker = audio_name.replace(".wav", "")
    duration = row["duration(s)"]

    # responses에서 랜덤하게 2개 선택
    sampled_responses = random.sample(responses, 2)

    for i, response in enumerate(sampled_responses):
        rows.append({
            "audio_name": audio_name,
            "text": response,
            "prompt_end_sec": duration,
            "speaker": speaker,
            "save_name": f"E06_{speaker}_mhcc_{i+1}.wav",
            "word_indices": "0"
        })

# DataFrame으로 만들고 저장
manifest_df = pd.DataFrame(rows)
manifest_df.to_csv("manifest.tsv", index=False, encoding="utf-8", sep="\t")

print(f"✅ manifest.tsv 파일이 생성되었습니다. 총 {len(manifest_df)}개의 행이 저장되었습니다.")
'''