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
<img src = 'https://user-images.githubusercontent.com/77375223/125087434-717d7480-e107-11eb-85b3-7faae9e7cce8.JPG' width = 500 height = 100>
Cascade classifier를 통해 얼굴을 인식을 하여 사용자가 원하는 처리를 할 수 있도록 해주는 코드 입니다.


### Blur
<img src = 'https://user-images.githubusercontent.com/77375223/125087449-74786500-e107-11eb-8393-77ef913a5c03.JPG' width = 500 height = 300>
Cascade를 통하여 받은 얼굴 좌표(x,y,w,h)를 통해 subface에 저장하여 해당 좌표에 블러처리를 하여 이미지에 적용해 줍니다.

### Edge
<img src = 'https://user-images.githubusercontent.com/77375223/125087465-780bec00-e107-11eb-8994-67c64fb10557.JPG' width = 500 height = 300>

### Mask
<img src = 'https://user-images.githubusercontent.com/77375223/125087478-79d5af80-e107-11eb-81d1-e81e1966b668.JPG' width = 500 height = 300>

