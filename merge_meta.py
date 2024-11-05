def merge_meta_files(meta_file1, meta_file2, output_file):
    with open(output_file, "w") as outfile:
        # 첫 번째 메타 파일 읽기
        with open(meta_file1, "r") as f1:
            lines1 = f1.readlines()
            outfile.writelines(lines1)

        # 두 번째 메타 파일 읽기
        with open(meta_file2, "r") as f2:
            lines2 = f2.readlines()
            outfile.writelines(lines2)

    print(f"Merged file created at: {output_file}")

# 예시 파일 경로
meta_file1 = "/path/to/meta1.csv"
meta_file2 = "/path/to/meta2.csv"
output_file = "/path/to/merged_meta.csv"

merge_meta_files(meta_file1, meta_file2, output_file)
