import os
import shutil
import sys
import exiftool
from PIL import Image



################ 전역변수 ################
# 이미지 파일 확장자 목록
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.avif', '.webp',
                    '.raw', '.dds', '.psd', '.apng', '.dng', '.exr', '.pcx', '.rgb', '.tga']
suffix = ""



################ 함수부 ################
# 이미지 파일의 EXIF 데이터를 제거하는 함수 - Pillow 사용
def remove_exif_with_pillow(file_path):
    global suffix # 전역 변수로 선언
    try:
        with Image.open(file_path) as img:
            data = list(img.getdata())
            img_without_exif = Image.new(img.mode, img.size)
            img_without_exif.putdata(data)
            img_without_exif.save(file_path) # 원본 파일을 덮어씁니다.
        print(f"EXIF 태그가 제거된 이미지: {file_path}")
    except Exception as e:
        print(f"이미지를 처리하는 중 오류 발생: {file_path} - {e}")



# 이미지 파일의 EXIF 데이터를 제거하는 함수 - PyExifTool 사용
def remove_exif_with_exiftool(file_path):

    # 전역 변수로 선언
    global suffix

    try:

        # 복제할 파일 경로 생성
        new_file_path = file_path + suffix
        # 파일 복제
        shutil.copy(file_path, new_file_path)

        # ExifTool을 사용하여 복제된 파일의 EXIF 데이터 제거
        with exiftool.ExifTool() as et:
            et.execute(b"-all=", bytes(new_file_path, 'utf-8'))
        
        print(f"EXIF 태그가 제거된 이미지: {new_file_path}")
        return  # 제거 성공 시 함수 종료

    except Exception as e:
        
        print(f"이미지를 처리하는 중 오류 발생: {new_file_path} - {e}")
        # 오류 발생 시 복제된 파일 삭제
        if os.path.exists(new_file_path):
            os.remove(new_file_path)
        return  # 함수 종료



# 경로 및 하위 모든 디렉토리 내의 그림파일을 찾아가며 EXIF 제거를 요청하는 함수
def remove_exif_from_images(directory):
    # os.walk(directory)는 다음을 반환합니다:
    # - root: 현재 탐색 중인 디렉토리의 경
    # - dirs: 현재 탐색 중인 디렉토리(여긴 root) 내의 하위 디렉토리 목록.
    #         이건 여기서는 사용하지 않으며, 관례적으로 _를 사용하여 무시합니다.
    # - files: root 디렉토리 내의 파일 목록
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif')):
                    # PILLOW를 이용한 제거: '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif'
                    remove_exif_with_pillow(file_path)
                elif any(file.lower().endswith(ext) for ext in image_extensions):
                    # ExifTool을 이용한 제거: '.avif', '.webp', '.raw', '.dds', '.psd', '.apng', '.dng', '.exr', '.pcx', '.rgb', '.tga'
                    remove_exif_with_exiftool(file_path)
            except Exception as e:
                print(f"이미지를 처리하는 중 오류 발생: {file_path} - {e}")
    print("모든 이미지 파일의 EXIF 태그 제거가 완료되었습니다.")




################ 실행부 ################
def main():
    
    # 첫 번째 인수로 디렉토리를 받음. 없으면 현재 디렉토리
    directory = sys.argv[1] if len(sys.argv) > 1 and len(sys.argv[1]) > 0 else os.getcwd()
    
    # 두 번째 인수가 존재하고 비어 있지 않은 경우 suffix 변수에 할당합니다.
    if len(sys.argv) >= 3:
        suffix = sys.argv[2]
    
    # 주어진 디렉토리 및 하위 모든 그림의 EXIF 태그를 제거
    remove_exif_from_images(directory)

    # 종료
    input("엔터 키를 누르면 종료됩니다...")



if __name__ == "__main__":
    main()