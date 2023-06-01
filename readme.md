# DonkeyCar Dataset Postprocessor

이 코드는 jpg, json 파일로 이루어진 tub 폴더의 내용 중 필요한 부분만 취해 수정한 뒤 1부터의 번호를 붙여 새로운 폴더에 넣어줍니다.

## 사용방법

### 1. main.py 수정

```python
# user settings
src_dir = 'C:\\Users\\User\\Downloads\\our_car\\mycar\\tub_1_no_obs'
dst_dir = 'C:\\Users\\User\\Downloads\\our_car\\mycar\\tub_1_processed'
ranges = [[10, 20], [30, 40]]
```
main.py 윗부분의 3개 변수를 수정합니다.
- src_dir: 원본 폴더 경로
- dst_dir: 결과 폴더 경로(없으면 자동으로 만들어집니다)
- ranges: 취하고자 하는 이미지, json파일 범위, 여러 범위를 지정 가능. 위 예시의 경우 10\~19, 30\~39 범위를 지정

### 2. 실행
```shell
$ cd [project dir]
$ python main.py
```
실행하면 다음을 해줍니다.
- 범위에 맞는 jpg 파일 복사
- 범위에 맞는 json 파일 내용 중 `'cam/image_array'` 수정 후 복사