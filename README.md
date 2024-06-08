> Completed project, which is now archived 완료된 프로젝트로서, 아카이브화 되었습니다.

<img src= 'https://github.com/daanta-real/exifRemover/assets/84055731/522dd28d-b6c6-4327-bb4c-7e9bbce8a2b2' alt=titleimage width=350 height=350>

# What's exifRemover? 이게 머꼬?

Remove EXIF infoes of all pics in the location of the executed folder. 지정된 폴더와 그 하위 모든 그림파일의 EXIF를 지워 줍니다.




# ANNOYED TO KNOW WOW TO RUN. 사용법 알기 귀찮.

Just double-click the app to run. 그럼 걍 실행파일 더블클릭하셈.

For the executed folder root and its all subfolders, all the image will be have no EXIF after run this. 실행되는 폴더와 모든 서브폴더에 있는 그림들의 EXIF를 지워줌.




# Detailed Usage. 상세 사용법

On the command prompt(or powershell, etc.) run the cmd below. 명령프롬프트 또는 파워쉘에서 아래 명령어를 입력해서 실행하세요.

```bash

> exifRemover [path] [file name suffix]

```





Arg. 1) path 경로

Target folder path, which is the path to remove EXIF infoes of the pics in of this path and the all subfolders of this path. 대상 경로입니다. 지정한 폴더와 그 하위폴더 전체를 EXIF 제거 대상으로 삼습니다.

If you don't write anything, it will be automatically the executed folder by default. 지정하지 않으면, 기본적으로 파일이 실행되는 그 폴더를 대상으로 삼습니다.

And if you want to put the file name suffix with the default path you should put ./(dot slash) here. 만약 경로는 그대로 두고 파일명 suffix만 붙이시려면 여기 옵션을 ./ 라고 주세요.





Arg. 2) file name suffix 파일명 뒷쪽에 붙일 문구(=접미어)

File name suffix word for attach at the end of the EXIF-removed files' name. 프로그램이 EXIF를 지우고 새로 저장할 파일 끝에 붙일 접미어입니다.

Notice that if blank then no suffix & OVERWRITE the original ones. 옵션 안주면 원본파일을 그대로 덮어쓰니 주의






# Extensions Supported 지원 확장자

1. With "Pillow" library: .jpg, .jpeg, .png, .gif, .bmp, .tiff, .tif

2. With "PyExifTool" library: .avif, .webp, .raw, .dds, .psd, .apng, .dng, .exr, .pcx, .rgb, .tga

3. No .apng supported 다른건 다 돼도 APNG(애니메이션 PNG)는 안됩니다.








# Development Info

Pythons 3.11, Pillow, PyExifTool, VSCode

제작 by 단타(daanta)

e-mail: daanta@naver.com

GitHub: http://github.com/daanta-real
