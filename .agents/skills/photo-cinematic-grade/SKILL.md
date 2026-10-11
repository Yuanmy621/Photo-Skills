---
name: photo-cinematic-grade
description: 依据照片已有光线做保留身份与场景的电影氛围调色，处理冷暖分离、明暗层次与饱和度。用于电影感、电影剧照、低饱和氛围或夜景电影调色；电影海报排版、换景和插画转绘不使用此技能。
---

# 电影氛围调色

从源照片的光线和叙事焦点建立电影感。默认只改调色与局部明暗，不新增灯光、雨水、烟雾、霓虹招牌或剧情元素。

## 读图与方向

- 查看主光方向、现有光源颜色、主体与背景明度、画面焦点及反射关系。人物身份、服饰、人数、建筑几何、文字、空间关系与原图比例均为保留项。
- 照片缺失时请用户提供。用户已有电影参考或情绪说明时依其可见特征处理；未指定时从以下方向选一个与原光线相符的方案并说明。

| 方向 | 可用的源图条件 | 核心变化 |
| --- | --- | --- |
| 冷暖分离 | 画面有暖主光与较冷环境 | 暖光主体与偏冷阴影分离，肤色中性自然 |
| 低饱和叙事 | 阴天、室内、普通街景 | 降低次要颜色，柔化高光，靠亮度保持主体可读 |
| 夜景电影感 | 已有路灯、室内灯或霓虹 | 保护灯源颜色与招牌细节，控制溢光，保留暗部空间 |

用户要晴天明亮电影感时保持明亮。电影感不要求暗黑，也不要求所有照片套青橙。

## 调色原则

- 保留已有照明方向，局部提亮或压暗只强化现有体积感；不把没有背光的主体改成强轮廓光。
- 使用有层次的阴影与平滑高光，允许深暗区域，但重要脸部和衣物不消失在黑块里。
- 冷暖分离控制在光源与环境合理的区域；皮肤不因青色阴影整体发绿，白衣不变成荧光蓝。
- 夜景强光可轻微扩散，灯牌字形仍可读；没有现成霓虹时不凭空添加灯牌。
- 原图比例默认保留。只有用户要求宽银幕裁切时才裁切，并检查人物、招牌和关键景物；黑边仅按明确要求添加。
- 默认不添加字幕、片名、片尾、日期、电影海报文字或胶片边框。多张照片统一色彩逻辑，分别适应曝光。

## 执行

以原图为图像编辑目标。先用 `view_image` 查看本地文件；调用 `image_gen` 时，目标都有本地路径则用 `referenced_image_paths`，否则用覆盖全部目标的最小 `num_last_images_to_include`，不并用。提示词明确“调色编辑”与全部保留项。保持原图透明性，普通照片输出不透明。

如果用户需要确定性调色参数或无损流程，使用其指定的编辑工具或给出相应参数方案，不把生成式重绘称为精确无损处理。查看结果后针对可见失败修正。用户只要提示词时不生成；工具不可用时给出提示词或方案并说明限制，不虚构成品或擅自改用额外配置的付费服务。

## 提示词骨架

```text
Color-grade the supplied photograph as a {selected_cinematic_direction} still.
Keep the original people, facial identity, poses, clothing, objects, signs,
geometry, composition, and aspect ratio unchanged.
Work from the existing {light_sources_and_light_direction}; create
{specific_color_separation_and_contrast_choices} without adding new lights.
Preserve detail in {important_highlights_and_shadows}, natural skin rendering,
and the source's time-of-day impression. Keep saturation intentional.
Use subtle localized contrast and controlled highlight roll-off.
No new neon signs, rain, fog, objects, altered faces, crushed facial shadows,
uniform teal-orange wash, captions, titles, letterbox bars, or crop unless asked.
```

替换全部变量，把用户明确要求的裁切或光效写入提示词，同时删除相矛盾的禁止项。

## 验收与交付

- 身份、物体、文字、构图与真实照明方向没有被改写。
- 色彩与明暗帮助看见主体，夜景灯牌与暗部空间仍可读。
- 风格与照片条件相符，肤色自然，没有为了电影感增加景物。
- 全图发青时减少阴影染色；脸部太暗时恢复局部亮度；光晕吞字时减弱扩散；人物变化优先返修。

交付成品与一句光色说明。项目内默认保存到 `output/photo-cinematic-grade/`，用户指定位置优先；保留源名与风格后缀，重名增加版本号，不覆盖原图。预览直接展示，需要复用时附实际提示词或调色参数。
