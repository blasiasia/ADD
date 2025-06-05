'''
from huggingface_hub import hf_hub_download

# 모델 이름과 파일 이름 지정
repo_id = "facebook/voxpopuli"  # 예: "facebook/wav2vec2-base"
filename = "en"  # 다운로드할 특정 파일

# 저장할 경로 지정
downloaded_file = hf_hub_download(
    repo_id=repo_id,
    filename=filename,
    repo_type = "dataset",
    local_dir="/mnt/aix23606/jiyoung/ADD",       # 원하는 로컬 폴더
    local_dir_use_symlinks=False         # 실제 복사로 저장
)

print(f"파일이 저장된 위치: {downloaded_file}")
'''
from datasets import load_dataset

# 전체 VoxPopuli 데이터셋 중 영어(en) 부분만 다운로드
dataset = load_dataset(
    "facebook/voxpopuli", 
    name="en",                   # 언어 지정
    split="train",              # split 지정 ("train", "validation", "test" 중 하나)
    cache_dir="/mnt/aix23606/jiyoung/ADD/huggingface"  # 원하는 경로
)

print(dataset)
