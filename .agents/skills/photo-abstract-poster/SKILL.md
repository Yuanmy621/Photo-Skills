---
name: photo-abstract-poster
description: 将摄影主图与同场景的极简几何小景组成抽象艺术海报，使用轮廓提炼、少量色面和大面积留白。用于极简抽象旅行海报、照片加抽象小景；纸艺撕边、木版墨迹和人物全幅插画不使用此技能。
---

# 极简抽象艺术海报

让一张真实照片与它的极简视觉摘要形成上下呼应。提炼场景的形与色，让观看者能在两种表达之间建立联系。

## 照片与提炼

- 查看源图，确定三到五个构图锚点及相对位置，例如气球团、楼体、栏杆、人群和天空。人物身份及背景结构首先在摄影主图中得到保留。
- 默认竖版 2:3 的暖白海报：上方完整摄影，下方一个较小的抽象小景。照片按原比例适配宽度，不裁切、不拉伸；用户要求独立抽象画时才去掉摄影区。
- 抽象小景保留锚点的相对大小和布局，把复杂楼体归纳为几个色面，把气球归纳为不等大的圆形，把远处人物归纳为小剪影。不能将原场景替换为随意摆放的几何装饰。

## 视觉语言

- 使用源图中的三到五种柔和颜色与一组清晰的轮廓。允许轻微纸纹，但色面以平涂为主；不用撕纸边、强烈网点、厚颜料和写实 3D 阴影。
- 主体之外保持大面积留白，抽象区面积通常明显小于摄影区。细节只用于识别，不重新画出完整照片的所有纹理。
- 可放一小组源图色样，位置服从版式，不做成占据主视觉的色卡网格。几何的边线可与源图栏杆、地平线或建筑轴线呼应。
- 默认无字；标题、字幕和语言按用户文本处理。地点、日期未知时省略，不从地标猜测。
- 用户要求摄影像素级不变时使用原图嵌入能力；没有可用能力时明确生成式编辑限制。

## 执行与验收

用 `view_image` 查看本地照片，以它为摄影区和抽象区的共同内容参考。`image_gen` 本地输入用 `referenced_image_paths`，否则使用最小 `num_last_images_to_include`，不同时提供两者。纸面默认不透明。

验收先看缩略图：真实主图清楚，下方小景简洁，同一组主体在两处位置对应。再核对人物身份、原图比例和几何小景是否引入了不存在的物件。小景过密时删细节；像随机形状时恢复原场景的主要轮廓；摄影变化时优先修主图。

用户只要提示词时不出图，工具不可用时提供提示词并说明限制，不虚构成品或切换到未经要求的服务。

## 提示词骨架

```text
Design a minimal abstract photo poster on {aspect_ratio} warm pale paper.
Keep the supplied complete photograph proportionally in the upper area,
preserving {photographic_invariants}. Below it, create a small flat geometric
summary of {source_anchor_group}, retaining its relative positions and scale.
Reduce forms to {specific_shapes} with {source_palette}, quiet silhouettes
and very few lines. Leave abundant paper around this summary.
Optional palette marks: {source_swatches_or_none}.
Text: {exact_text_or_no_text}. No invented scenery, random geometry,
torn collage, dense detail, heavy textures, drop shadow or mockup.
```

替换变量，无内容行删除。交付图像与一句形色提炼说明；默认保存到 `output/photo-abstract-poster/`，沿用源名、风格后缀与必要版本号，不覆盖原图。用户目录优先，预览直接展示，复用时附实际提示词。
