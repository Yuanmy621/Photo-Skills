---
name: photo-risograph
description: 将照片转为双色或三色孔版印刷海报，用专色色层、网点、叠印和轻微套印偏移表现源图。用于 risograph、riso、孔版印刷、双色复古印刷；蓝白蓝晒、普通黑白调色或网页设计系统不使用此技能。
---

# 双色孔版印刷

把摄影中的明暗与形状转换为少量油墨层，让叠印、纸色和网点共同完成画面。默认双色印刷风格的平面海报，保持源图方向与关键构图。

## 取材与色层

- 先查看照片，记录主轮廓、关键数量、遮挡、负空间和明暗层次。图片缺失时请用户提供。
- 从照片中选择一种承载结构的深色与一种承载氛围的亮色，用户有配色时优先采用。第三色仅在双色无法分清关键形状或用户要求时加入。
- 为每种油墨分配职责，如深蓝表示结构与阴影、朱红表示暖光与视觉焦点。纸白也是一个亮度层，不用灰色蒙版填满。
- 保留辨识度所需的主体轮廓、人数、相对位置与关键几何。人物允许印刷化简化，不能改变身份或随意变为匿名人形；用户要求高度抽象时才扩大简化程度。

## 印刷风格

- 色面平整但有细小油墨颗粒，明暗用疏密网点、少量线纹和叠印表达，避免连续写实渐变。
- 套印偏移只在局部色层边缘轻微出现，不能造成脸部重影、文字错位或全画面模糊。
- 两种油墨的叠色由原色关系形成更深的区域；不要偷偷加入大量未指定颜色。
- 植被、窗格和人群细节合并为可读形状，仍保留源图特有的节奏。避免变成通用太阳、山峰与圆点装饰海报。
- 默认自然浅色纸、无字、无相框。用户要海报标题时用准确文本与指定语言，文字通常用一个结构色，不能编造档案号、日期或地名。
- 这是数字模拟的孔版视觉。用户要求真实印刷分色时需另行确认尺寸、油墨与印厂要求；生成 RGB 图片不能被标为已完成可上机分色稿。

## 执行

用图像编辑或参考图生成工具，保留照片作为内容依据，而不是仅靠文字猜场景。先用 `view_image` 查看本地文件；调用 `image_gen` 时，本地参考齐全则用 `referenced_image_paths`，否则用覆盖全部参考的最小 `num_last_images_to_include`，不可并用。纸面默认不透明。

生成一张后检查色层、主轮廓与套印偏移，再修正观察到的问题。用户只要提示词时不生成。工具不可用时交付最终提示词并说明限制，不虚构成品，不擅自改用需要密钥或付费配置的服务。

## 提示词骨架

```text
Reinterpret the supplied photograph as a {two_or_three_ink} risograph print,
{aspect_ratio}, on {paper_tone} matte paper.
Preserve {source_specific_subject_counts_shapes_and_relationships}.
Assign {structural_ink} to {structure_and_shadow_regions}, and {accent_ink}
to {source_derived_accent_regions}. Use paper-white highlights and controlled
overprint where inks meet. Simplify {repetitive_details} into legible masses.
Build tonal depth through halftone density and sparse printed marks, with
fine ink grain and very slight localized registration drift.
Text: {exact_user_text_and_language_or_no_text}.
No extra colors, unrelated icons, invented metadata, continuous photographic
gradients, heavy double contours on faces, glossy mockups, or extra lettering.
```

替换全部变量；无文字请求使用 `no text`，用户要精确保留的细节写入保留项。

## 验收与交付

- 主体与空间关系对应原图；少量油墨与纸白能解释全部颜色。
- 明暗主要由印刷网点与色面构成，纸纹没有替代结构。
- 偏移足够表现印刷质感，但面部、轮廓和文字仍清楚。
- 颜色泛灰时恢复专色纯度；像普通滤镜时加强网点层次；偏移过大时只减少偏移；标题逐字复核。

交付平面图像并说明所选油墨颜色。项目内默认保存到 `output/photo-risograph/`，用户指定位置优先；保留源名与风格后缀，重名增加版本号，不覆盖原图。预览直接展示，用户要求复用时附最终提示词。
