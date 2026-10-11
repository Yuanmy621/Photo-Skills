---
name: photo-ukiyo-e
description: 将旅行或风景照片转绘成浮世绘木版视觉，使用轮廓、有限平涂色面、层叠空间和细木版纹理。用于浮世绘旅行版画、日式木版风景；动漫人物化、水彩、孔版网点或纯照片调色不使用此技能。
---

# 浮世绘旅行版画

用木版的轮廓、色面与空间节奏重述用户的照片。现代街道、建筑和服饰仍属于原场景，不因为采用版画风格就自动改成古代日本。

## 读图与取舍

- 查看照片，记录主体轮廓、地平线、前中后景、主要斜线、关键建筑结构、人物身份与人数。
- 图片缺失时请用户提供。默认沿用源图比例与方向，无字、无边框；用户要旅行海报比例、题签或纸边时才加入。
- 提取四到六种有层次的颜色，兼顾浅底、中间色和深色轮廓。用户指定配色时优先，不能默认给所有照片加海浪、红日或富士山。
- 风景与建筑可以合并重复细节，保留该地点最有辨识度的结构。人物保留姿势、身份和服饰，不能自动变成和服人物或动漫脸。

## 木版语法

- 使用干净但有轻微手工变化的轮廓，粗细帮助区分前后景，不把每条线都画成等宽黑线。
- 色块以平涂为主，局部天空或水面可使用克制的版画渐层；体积不靠摄影高光或三维渲染。
- 前景细节相对清楚，远景简化为层叠色面与轮廓。保留原图重要透视关系，不把建筑压扁到无法识别。
- 木纹、纸纤维和边缘轻微套色变化作为低强度材质，不覆盖人物五官、招牌与结构线。
- 水、云、植物使用来源于照片的形状节奏；没有这些元素的照片不新增装饰浪花、云团或樱花。
- 题签与印章不是必需。需要文字时使用准确的用户文本与语言，不编造日文书法、作者签名、印章或“古代版画”出处。

## 执行

把照片作为内容参考使用图像编辑工具。先用 `view_image` 查看本地照片；调用 `image_gen` 时，本地参考齐全则用 `referenced_image_paths`，否则用覆盖全部目标的最小 `num_last_images_to_include`，不并用。纸面默认不透明。

生成后对照源图的地标、人物与构图，针对实际失败修正。用户只要提示词时不生成。工具不可用时提供最终提示词并说明限制，不虚构成品，不擅自改用需要密钥或付费配置的服务。

## 提示词骨架

```text
Reinterpret the supplied photograph as an ukiyo-e-inspired woodblock artwork,
{aspect_ratio}. Keep {source_specific_subjects_identity_clothing_and_geometry},
with the original {foreground_midground_background_relationships}.
Use expressive controlled contours, a limited palette of {source_palette},
flat printed color planes, and restrained tonal gradation in
{source_region_suitable_for_gradation}. Simplify {repetitive_details} while
keeping {distinctive_landmark_features} recognizable.
Add subtle paper fibers and low-intensity woodblock texture. Flat artwork.
Text: {exact_user_text_and_language_or_no_text}.
No invented waves, mountains, red sun, blossoms, kimono, anime faces,
fake calligraphy, artist signatures, seals, photographic gloss, or 3D mockup.
```

替换全部变量；不适用的渐层段落删掉。用户明确要求额外元素时将其写为新增创作元素，同时删掉相应禁止项，不把新增内容描述为原图事实。

## 验收与交付

- 原场景、地标、人数、衣着和空间关系可辨认，没有被替换成通用日式景观。
- 轮廓与平涂色面建立风格，既不是动漫截图，也不是照片加纸纹。
- 木版材质轻微，前后景层次清楚，文字与题签无伪造信息。
- 像动漫时减少软渐变和面部夸张；木纹过强时减材质；地标变形时恢复关键轮廓；新增浪花等无依据元素时删除。

交付图像与一句版画取舍说明。项目内默认保存到 `output/photo-ukiyo-e/`，用户指定位置优先；保留源名与风格后缀，重名增加版本号，不覆盖原图。预览直接展示，用户要求复用时附最终提示词。
