---
name: photo-watercolor-card
description: 将照片转绘为透明水彩旅行纪念卡，搭配选择性钢笔结构、穿孔分界与窄档案栏。用于水彩旅行记忆卡、穿孔水彩卡、钢笔淡彩；厚涂油画、摄影明信片和纯调色不使用此技能。
---

# 水彩旅行纪念卡

以透明水彩表达光与色，选择性钢笔结构保留照片辨识度，纸白承担高光。默认生成一张竖版 2:3 的旅行纪念卡，主画面与窄档案栏之间用穿孔线分隔；用户指定无框水彩时去掉卡片装饰。

## 输入与现实锚点

- 查看照片，记录最重要的建筑、人物或景物及其轮廓、比例、前后关系。确定适合水彩铺色的天空、水面、墙体和植被。
- 提取照片实际色温与两到四种颜色。阴天保持阴天，雪景可以清冷，夜景保持夜色；不能把所有照片改成蓝天暖阳。
- 标题、地点、日期与语言沿用用户选择。缺少地点时用不含地理事实的短标题或无字版，不从照片猜城市。图片缺失时请用户提供。

## 转绘与卡片设计

- 水彩是主视觉，钢笔线只选择性说明关键轮廓；内部排线少量即可。远景更轻，避免把每片叶子、每个砖块都描出来，或把作品变成均匀描边的漫画。
- 水彩为透明叠色、局部晕开和纸白留光；边缘有干湿变化。禁止厚重不透明涂层、塑料渐变和全幅模糊滤镜。
- 有人物时保留身份、姿势、服饰与人数；可以简化笔触，不能换脸或增添人物。建筑不能重组为别处地标。
- 旅行卡默认浅色纸底，画面占主要区域，右侧留一条较窄的档案栏；两者之间用一列细小均匀的穿孔分界。人物、建筑不能被穿孔截断，宽幅源图可改成上下分区。
- 短标题与两三个档案字段为可选项。标题与地点、日期按用户文字使用，未提供时不画空白伪字段、不编地点；无字版仍可靠水彩、纸边与细穿孔成立。用户指定邮票风格时才使用四周齿孔，纯画面时全部移除。
- 中文、英文或双语均可按要求使用。精确文字较多时优先生成画面，再使用可用排版工具叠加准确文本；没有排版能力时保留可编辑的无字成品并说明文字限制，不擅自改语言。
- 不自动清除原图中的签名、水印或重要招牌；需要调整时以用户明确的编辑要求为准。

## 执行

先用 `view_image` 查看本地照片，再使用图像编辑工具把照片作为目标或内容参考。调用 `image_gen` 时，所有参考都有本地路径则用 `referenced_image_paths`；否则使用覆盖全部目标的最小 `num_last_images_to_include`，不同时提供两者。卡片默认不透明，只有用户要透明切图时才改变背景。

完成一张并查看后，仅针对实际问题修正。用户只要提示词时直接提供提示词。工具不可用时交付最终提示词并说明限制，不声称已生成图像，也不自动切到需要密钥或付费配置的服务。

## 提示词骨架

用真实观察与用户文本替换变量，无值的可选行删掉。

```text
Repaint the supplied photograph as a pen-and-watercolor travel card,
{aspect_ratio}. Preserve {subject_identity_silhouette_pose_and_layout}.
Draw selective fine ink contours for {key_structural_features}; let distant
details remain lighter and less descriptive.
Use transparent washes of {source_palette}, with reserved white-paper
highlights, restrained pigment pooling, and a few soft wet edges.
Retain the source's {weather_light_and_temperature}.
Card treatment: {watercolor_panel_and_narrow_perforated_archive_column_or_borderless}.
Text: {exact_user_text_language_and_placement_or_no_text}.
No thick impasto, opaque acrylic, invented landmarks, changed faces,
default sunny sky, heavy grunge, or extra lettering. Flat artwork, no mockup.
```

## 验收与交付

- 主体轮廓、人数、姿势及建筑关键结构对应源图。
- 同时看得到钢笔结构与透明水彩，纸白没有被全部涂满。
- 纪念卡的水彩主画面与窄栏有清晰层级，穿孔是一条分界，不是覆盖整张图的圆点装饰。
- 天气与色温有照片依据，边缘装饰未压住主体。
- 水彩变油画时减薄色层；线条太密时删内部纹理；认不出主体时恢复关键轮廓；文字按原文核对。

交付图像与一句调色说明。项目成品默认保存到 `output/photo-watercolor-card/`，用户指定位置优先；保留源文件名与风格后缀，重名增加版本号。原图不覆盖，预览直接展示，用户要求复用时附最终提示词。
