# Image-Processing_Face-recognition-Blur-Mask

## Overview

<img src = 'https://user-images.githubusercontent.com/77375223/125083734-b6071100-e103-11eb-93ac-f9122e15e268.jpg' height = 300>

Cascade classifier를 통해 얼굴을 인식하여 블러 효과(모자이크), Mask, Edge Filter 등을
Tkinter module을 통해 사용자가 조작하여 원하는 효과를 적용할 수 있다.

## 시연 스크린샷

### Original Image
<img src = 'https://user-images.githubusercontent.com/77375223/125084848-ec915b80-e104-11eb-923c-188884e0a6b6.JPG' width = 500 height = 300>

### Blur Image
<img src = 'https://user-images.githubusercontent.com/77375223/125084858-eef3b580-e104-11eb-8488-6781854dc2a8.JPG' width = 500 height = 300>

### Edge Image
<img src = 'https://user-images.githubusercontent.com/77375223/125084870-f1560f80-e104-11eb-8a6f-679039f15fd0.JPG' width = 500 height = 300>

### Masking Image
<img src = 'https://user-images.githubusercontent.com/77375223/125084876-f31fd300-e104-11eb-8247-eefe926ef803.JPG' width = 500 height = 300>

## Code

### Cascade classifier
<img src = 'https://user-images.githubusercontent.com/77375223/125095630-5a428500-e10f-11eb-8bb7-39c3ea079ae6.JPG' width = 500 height = 100>
path 변수를 통해 각각의 이미지를 저장할 경로를 생성해줍니다.(blur, edge, mask) <br>
face_detector 변수를 통해 cascade classifier로 얼굴 인식을 할 수 있도록 설정해주었습니다. <br>

### Blur
<img src = 'https://user-images.githubusercontent.com/77375223/125087449-74786500-e107-11eb-8393-77ef913a5c03.JPG' width = 500 height = 300>
Cascade를 통하여 받은 얼굴 좌표(x,y,w,h)를 통해 subface에 저장하여 해당 좌표에 블러처리를 하여 이미지에 적용해 줍니다.

### Edge
<img src = 'https://user-images.githubusercontent.com/77375223/125087465-780bec00-e107-11eb-8994-67c64fb10557.JPG' width = 500 height = 200>

### Mask
<img src = 'https://user-images.githubusercontent.com/77375223/125087478-79d5af80-e107-11eb-81d1-e81e1966b668.JPG' width = 500 height = 300>
코드 첫 줄에 얼굴 부분의 영역만 gray scale로 바꿔주는데, threshold를 이요해 줄 것이어서 gray scale로 바꿔주었습니다. <br>
그 후 적용할 마스크를 resize해주고 threshold를 통해 특정 값을 0과 1로 바꿔준다. 이렇게 해주는 이유는 bitwise연산을 통하여 얼굴에 바로 적용할 수 있도록 하기 위함입니다. <br>
그렇게 바꾼 마스크 이미지를 bitwise연산을 통해 얼굴에 씌워주고 해당 이미지를 return해주는 코드입니다. <br>
예외 처리를 해 준 이유는 Mask가 화면 밖으로 나갔을 경우 범위 오류가 생성되면서 프로그램이 종료하는 문제를 겪었습니다. 해당 문제를 해결하기 위해 예외처리로 간단히 해결했습니다. <br>

### Image save
<img src = 'https://user-images.githubusercontent.com/77375223/125096295-f8364f80-e10f-11eb-9a0c-d83afdfe7366.JPG'>
각각 Mask(i_ga), Blur(i_blur), Edge(i_edge), Original(i_original)의 전역 변수를 생성해 주었습니다. 이미지에 numbering을 해줄 변수 입니다. <br>
그 후 맨 처음에 설정한 경로에 저장해주는 코드입니다. <br>
