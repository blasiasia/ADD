import numpy as np
import soundfile as sf
import torch
from torch import Tensor
from torch.utils.data import Dataset
import random

___author__ = "Hemlata Tak, Jee-weon Jung"
__email__ = "tak@eurecom.fr, jeeweon.jung@navercorp.com"

def genSpoof_list(dir_meta, is_train=False, is_eval=False, retain_ratio=None, seed=None):
    # retain_ratio : 전체 dataset에서 일부 샘플링
    d_meta = {}
    file_list = []

    with open(dir_meta, "r") as f:
        l_meta = f.readlines()

    if is_train:
        for line in l_meta:
            _, key, _, _, label = line.strip().split(" ")  # 불필요한 중간 열 제거
            file_list.append(key)
            d_meta[key] = 1 if label == "bonafide" else 0

    elif is_eval:
        for line in l_meta:
            _, key, _, _, label = line.strip().split(" ")
            file_list.append(key)

    else:
        for line in l_meta:
            _, key, _, _, label = line.strip().split(" ")
            file_list.append(key)
            d_meta[key] = 1 if label == "bonafide" else 0

    # Shuffle and retain a subset if specified
    if retain_ratio is not None:
        if seed is not None:
            random.seed(seed)  # Set seed for reproducibility
        random.shuffle(file_list)  # Shuffle file_list
        retain_count = max(1, int(len(file_list) * retain_ratio))  # Ensure at least 1 element
        file_list = file_list[:retain_count]  # Retain top retain_count elements

        # For train and non-eval cases, filter d_meta based on retained keys
        if not is_eval:
            d_meta = {key: d_meta[key] for key in file_list}

    return (d_meta, file_list) if not is_eval else file_list


def pad(x, max_len=64600):
    x_len = x.shape[0]
    if x_len >= max_len:
        return x[:max_len]
    # need to pad
    num_repeats = int(max_len / x_len) + 1
    padded_x = np.tile(x, num_repeats)[:max_len]
    return padded_x


def pad_random(x: np.ndarray, max_len: int = 64600):
    x_len = x.shape[0]
    # if duration is already long enough
    if x_len >= max_len:
        stt = np.random.randint(x_len - max_len)
        return x[stt:stt + max_len]

    # if too short
    num_repeats = int(max_len / x_len) + 1
    padded_x = np.tile(x, (num_repeats))[:max_len]
    return padded_x


class TrainDataset(Dataset):
    def __init__(self, list_IDs, labels, base_dir):
        """self.list_IDs	: list of strings (each string: utt key),
           self.labels      : dictionary (key: utt key, value: label integer)
           self.base_dir    : 각 오디오 파일의 전체 경로(확장자 제외) -> 리스트"""
        self.list_IDs = list_IDs
        self.labels = labels
        self.base_dir = base_dir
        self.cut = 64600  # take ~4 sec audio (64600 samples)

    def __len__(self):
        return len(self.list_IDs)

    def __getitem__(self, index):
        key = self.list_IDs[index]
        y = self.labels[key]
        file_path = self.base_dir[key]  # 딕셔너리에서 key로 경로 찾기
        
        if file_path.exists():
            X, _ = sf.read(str(file_path))
            # X의 차원이 (n_samples, n_channels)인 경우, n_channels을 1로 변환
            if X.ndim == 2 and X.shape[1] > 1:
                X = X[:, 0]  # 첫 번째 채널만 사용
            X_pad = pad_random(X, self.cut)
            x_inp = Tensor(X_pad).unsqueeze(0)
            return x_inp, y
        else:
            raise FileNotFoundError(f"File {file_path} does not exist.")


class TestDataset(Dataset):
    def __init__(self, list_IDs, base_dir):
        """self.list_IDs	: list of strings (each string: utt key),
           self.base_dir    : 각 오디오 파일의 전체 경로 -> 리스트,
        """
        self.list_IDs = list_IDs
        self.base_dir = base_dir
        self.cut = 64600  # take ~4 sec audio (64600 samples)

    def __len__(self):
        return len(self.list_IDs)

    def __getitem__(self, index):
        key = self.list_IDs[index]
        file_path = self.base_dir[key]  # 딕셔너리에서 key로 경로 찾기
        if file_path.exists():
            X, _ = sf.read(str(file_path))
            # X의 차원이 (n_samples, n_channels)인 경우, n_channels을 1로 변환
            if X.ndim == 2 and X.shape[1] > 1:
                X = X[:, 0]  # 첫 번째 채널만 사용
            X_pad = pad(X, self.cut)
            x_inp = Tensor(X_pad).unsqueeze(0)
            return x_inp, key
        else:
            raise FileNotFoundError(f"File {file_path} does not exist.")
    
''' 
class TestDataset(Dataset):
    def __init__(self, list_IDs, base_dir):
        """self.list_IDs	: list of strings (each string: utt key),
        """
        self.list_IDs = list_IDs
        self.base_dir = base_dir
        self.cut = 64600  # take ~4 sec audio (64600 samples)

    def __len__(self):
        return len(self.list_IDs)

    def __getitem__(self, index):
        key = self.list_IDs[index]
        X, _ = sf.read(str(self.base_dir / f"{key}.flac"))
        X_pad = pad(X, self.cut)
        x_inp = Tensor(X_pad).unsqueeze(0)
        return x_inp, key

'''