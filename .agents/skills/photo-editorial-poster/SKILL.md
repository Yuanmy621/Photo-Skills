---
name: photo-editorial-poster
description: 将照片设计成以单色图像、强字号层级和非对称网格为核心的现代编辑海报。用于单色编辑设计、艺术展览感海报、mono-color 风格；只做黑白调色、复古拼贴或电影海报不使用此技能。
---

# 现代单色编辑海报

把照片作为编辑设计中的图像材料，用色彩限制、字号层级和版式建立视觉力度。默认现代、简洁；用户明确选择复古时才增加旧纸或旧印刷质感。

## 内容与文字

- 查看照片，记录主体身份、物件轮廓、构图焦点和可以留给版面的空白。以一张源图为基础，避免为了版式复制主角。
- 默认竖版 3:4，浅白纸底。照片按原比例置入一个非对称图块，主体关键部分可见；没有裁切授权时通过缩放与纸边容纳完整照片。
- 标题是这一风格的重要设计元素。沿用用户准确文本；未提供时可采用不含推测事实的短画面描述，如“林间”或“同行”，并在交付说明中列出实际文字。用户要无字版时移除全部文字，靠图块与色带建立层级。
- 副标题与正文只使用用户提供的内容。不能用随机外文、乱码、虚构日期、地址、展览信息或赞助商填满版面。默认中文，用户指定其他语言优先。

## 编辑设计

- 从照片选一个主色，将图像压到该色与纸白、深浅灰组成的窄色域；可用一处小面积强调色。主体仍应有层次，不能用平涂覆盖五官。
- 用一个大字号标题、少量较小信息和非对称留白形成清晰层级。可用纵向字列或局部旋转，阅读顺序仍清楚，不把所有文字都做成装饰。
- 对齐图块边缘与文字轴线，留出连贯的边距。图像、细线和矩形色带共同建立网格，避免等大小九宫格或商业宣传单式堆叠。
- 默认现代平面印刷感，保留干净纸面。单色约束作用于图像与版式，不把普通单色照片直接交付为海报。
- 用户要求主照片像素级不变或精确复杂排版时，选择可用的原图嵌入或文字排版工具；生成式编辑不承诺精确无损。

## 执行与检查

先用 `view_image` 查看源图，明确它是主体内容参考。`image_gen` 的本地参考用 `referenced_image_paths`，其他输入用覆盖输入的最小 `num_last_images_to_include`，不并用。输出为不透明平面图稿。

检查图像身份与比例、单色层次、标题阅读顺序和每一个字。文字失败时减少文案或用可用排版工具修正，不把错误文字当成设计；排版没有主次时减少图块和正文；只呈现一张调色照片时重建字号和留白层级。

只要提示词时不出图；工具不可用时提供提示词与限制，不声称已有海报，不擅自切换额外服务。

## 提示词骨架

```text
Design a contemporary editorial poster from the supplied photograph,
{aspect_ratio}, on clean pale paper. Preserve {subject_identity_and_details}
in a proportionally placed photo block. Grade the image into {primary_ink}
with paper-white and tonal greys, retaining clear facial and object detail.
Build an asymmetric grid with generous negative space, a strong oversized
headline and restrained supporting lines; align the image and typography.
Exact headline: "{chosen_exact_title}".
Supporting text: {exact_user_text_or_none}. Language: {language}.
No invented event facts, gibberish, sponsors, duplicated subjects, default
retro effects, dense flyer layout, decorative frame or photographed mockup.
```

用确定文字替换变量；无字版删去文字行并写明 no text。交付图像、实际标题与一句配色说明；默认保存到 `output/photo-editorial-poster/`，沿用源名、风格后缀与必要版本号，不覆盖原图。指定目录优先，预览直接展示，复用时附实际提示词。
