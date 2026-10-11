---
name: photo-crayon-card
description: 将照片转绘为保留蜡笔划痕、纸纹露白和轻松手绘线条的艺术卡，可选上方摄影与下方蜡笔小景的对照版。用于手绘蜡笔、油画棒旅行卡；厚涂刮刀、水彩晕染和光滑矢量插画不使用此技能。
---

# 手绘蜡笔艺术卡

用蜡笔与油画棒的笔迹记录照片中的形色。重点是可以看出一笔一笔的划痕与露白，不是把照片模糊后盖上一层纸纹。

## 画面与模式

- 查看源图，记录主体轮廓、人数、身份、姿势和空间关系；提取三到五种代表色，确定可简化的重复细节。
- 默认一张竖版 2:3、暖白纸上的单幅蜡笔转绘卡。完整保留主要主体，四周可露出自然纸边，不增添花草、景物或人。
- 用户要求照片对照卡时：上方等比放置完整摄影主图，下方用较小的蜡笔小景呼应核心主体。摄影区不转绘，两部分有明确留白间隔。
- 用户比例和构图要求优先；改变画幅时用留白容纳源图，不擅自裁掉人物或物件。

## 笔触与纸面

- 用可见的短线、绕圈和侧锋擦色表现形体；笔触方向顺着果实、树叶、人物衣褶或建筑结构。大色面由松散的叠笔组成，纸白透过笔迹。
- 保持蜡笔的干燥、颗粒状边缘与轻微涂出轮廓的手感。用少量较深线条维持识别，不勾勒每一片叶子、每一块砖。
- 配色来自源图，可更轻快鲜活，但不让脸部或白衣发蓝发绿。人物五官与表情对应原图，不改成大眼卡通。
- 纸底细微纤维、画面边缘的少量划痕可以存在；胶带、纸片等手账装饰只按用户要求添加，不能靠贴纸堆积产生风格。
- 默认无字。用户文字可用松散手写字形，实际拼写不改变，未知地点与日期省略。

## 执行与验收

先用 `view_image` 查看本地源图，再以其为内容参考做图像编辑。`image_gen` 本地输入用 `referenced_image_paths`，其他输入用覆盖目标的最小 `num_last_images_to_include`，两者不并用。纸底默认不透明。

检查主体与源图对应，放大时能看见蜡笔划线与露白，缩小时有清楚的色块和焦点。画面过于光滑时修断续笔迹；像油画时降低颜料厚度；像水彩时去掉晕染边缘；人物变卡通时优先修身份。对照版另外检查主照片比例与内容。

只要提示词时不出图；工具不可用时交付提示词并说明限制，不虚构文件，也不自行改用额外服务。

## 提示词骨架

```text
Reinterpret the supplied photograph as a hand-drawn wax-crayon art card,
{aspect_ratio}, on warm ivory paper. Preserve {subject_identity_pose_layout}.
Use {source_colors} with visible looping strokes, short directional marks,
side-rubbed pigment, dry grain and paper-white gaps. Simplify secondary
details while keeping {recognizable_features}. No smooth gradient fills.
Layout: {single_crayon_artwork_or_photo_above_crayon_vignette}.
Text: {exact_text_or_no_text}. No cartoon faces, new scenery, thick impasto,
watercolor bleeding, glossy 3D, dense stickers, decorative frame or mockup.
```

替换变量，删除无值行。交付图像与一句笔触说明；默认保存到 `output/photo-crayon-card/`，沿用源名、风格后缀和必要版本号，不覆盖原图。指定目录优先，预览直接展示，复用时附实际提示词。
