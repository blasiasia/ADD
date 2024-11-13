# 파일 경로 지정
file_path = '/Volumes/System/MeloTTS/wikipedia/E02_wiki.txt'  # 메타데이터 파일 경로

# E02_US로 시작하는 파일의 개수 세기
count = 0

# 파일을 열어서 읽기
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        # 각 행에서 두 번째 열이 'E02_US'로 시작하는지 확인
        if line.split()[1].startswith("E02_DE"):
            count += 1

print(f"E02_US로 시작하는 파일의 개수: {count}")
