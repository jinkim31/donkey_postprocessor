# DonkeyCar Dataset Postprocessor

이 코드는 jpg, json 파일로 이루어진 tub 폴더의 내용 중 필요한 부분만 취해 수정한 뒤 1부터의 번호를 붙여 새로운 폴더에 넣어줍니다.

## 사용방법

### 1. main.py 수정

```python
# user settings
src = [
    ('C:\\Users\\User\\Downloads\\our_car\\mycar\\tub_1_no_obs', [(10, 20), (30, 40)]),
    ('C:\\Users\\User\\Downloads\\our_car\\mycar\\tub_2_obs', [(10, 20), (30, 40)]),
]
dst = 'C:\\Users\\User\\Downloads\\our_car\\mycar\\tub_1_post'
```
main.py 윗부분의 3개 변수를 수정합니다.
- src: 원본 폴더 경로와 폴더 내 png, json 파일의 index range 리스트. 위 예시의 경우 `tub_1_no_obs` 폴더에서 10\~19, 30\~39번 데이터, `Ttub_2_obs` 폴더에서 10\~19, 30\~39번 데이터를 가져오겠다는 뜻.
- dst: 결과 폴더 경로(경로가 없으면 자동으로 만들어집니다)

### 2. 실행
```shell
$ cd [project dir]
$ python main.py
``` 