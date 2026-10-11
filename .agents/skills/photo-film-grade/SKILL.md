---
name: photo-film-grade
description: 对用户照片做保留内容的胶片风格调色，控制色温、高光肩部、黑位与细颗粒。用于复古胶片、日系清透、暖色负片或黑白纪实；换场景、插画转绘、胶片边框拼贴不使用此技能。
---

# 复古胶片调色

改变照片的色调与质感，保持照片中的人、物与空间。胶片感来自亮度曲线、颜色响应和合适的颗粒，不靠划痕与橙色遮罩。

## 读图与选择方向

先查看源图的白平衡、肤色、最亮区域、最暗区域与已有噪点。保留原始比例、构图、人数、人物身份、面部细节、文字与建筑几何；不要顺便瘦脸、美白或删杂物。图片缺失时请用户提供。

用户已指定风格时按其选择；没有具体方向时按照片光线选择一项并简短说明，不必先让用户选套餐。

| 方向 | 适合的照片 | 处理重点 |
| --- | --- | --- |
| 日系清透 | 日光街景、旅行、窗边人像 | 柔和对比，轻微冷色阴影，明亮但保留天空与皮肤层次 |
| 暖色负片 | 夕阳、室内、家庭照片 | 暖高光、适度降低绿色饱和，肤色保持自然，黑位略松 |
| 黑白纪实 | 街拍、阴雨、高反差光线 | 按主体分离亮度，黑白两端保留细节，局部对比与细颗粒 |

这些是审美方向，不声称精确模拟某个胶片型号。用户给出具体参考时优先匹配参考的可见特征。

## 调色规则

- 先纠正明显偏色和曝光问题，再加风格。原图低照度时不要靠抬曝光把夜晚变白天。
- 高光采用柔和过渡，白色可以接近纸白但不能整片剪切；暗部保留主体轮廓，避免灰雾覆盖整张图。
- 肤色、白衣和中性墙体作为颜色检查点；暖色不等于全图发黄，清透不等于青色皮肤。
- 颗粒随图像尺度保持细小，原图已有噪点时降低附加量。光晕只在真实强光边缘轻微出现，不给每条轮廓描橙边。
- 默认没有漏光、划痕、日期戳、相框或文字。这些只在用户明确要求时增加，日期不能编造。
- 同批照片保持一致色彩方向，同时按每张曝光调整，不能把同一组数值机械套给所有图。

## 执行

使用图像编辑工具处理原照片。先用 `view_image` 查看本地文件；调用 `image_gen` 时，所有目标有本地路径则用 `referenced_image_paths`，否则使用包含全部目标的最小 `num_last_images_to_include`，不可并用。提示词把人物与构图保留项放在风格描述前。通常保持不透明输出；透明原图在编辑时保留其透明性。

若用户明确要求 Lightroom、LUT 或确定性参数，输出相应调色建议或使用其指定编辑工具，并说明数值需要按原图校准；不要把生成式编辑称为无损调色。用户要精确像素保留时说明当前工具能否满足。

查看输出并与原图比较身份、内容、皮肤和高光。只修正已观察到的问题；用户只要提示词则不生成。图像工具不可用时提供最终提示词或调色方案并说明无法出图，不擅自切换到需要额外配置的服务。

## 提示词骨架

```text
Edit only the tonal and color rendering of the supplied photograph.
Preserve every person, facial identity, pose, object, readable sign, scene
geometry, composition, and aspect ratio. Do not retouch body or face shapes.
Apply a {selected_film_direction} treatment: {specific_tone_and_color_choices}.
Keep {highlight_detail} readable, retain {shadow_detail}, and maintain
natural skin tones and believable neutral surfaces.
Use fine restrained grain appropriate to the source image, soft highlight
roll-off, and only subtle glow around existing bright light sources.
No new objects, scene changes, blanket orange cast, coarse noise, scratches,
light leaks, borders, date stamps, text, or beauty retouching unless requested.
```

替换所有变量；黑白方向把肤色要求改成保留面部明暗层次，不要求黑白照片出现彩色肤色。

## 验收与交付

- 人脸、人数、文字、物体与构图没变；这是调色而非重新创作场景。
- 风格在缩略图下可见，放大后颗粒没有吞掉皮肤、发丝或细线。
- 高光与暗部主体仍有层次，中性色与肤色可信；没有默认复古装饰。
- 皮肤偏橙时减小色温偏移；黑位发灰时恢复局部对比；颗粒过重时降低质感强度；身份变化优先返修。

交付成品与所选方向。项目内默认保存到 `output/photo-film-grade/`，用户指定位置优先；文件保留源名与风格后缀，重名增加版本号，原图不覆盖。预览直接展示；需要复用时附实际提示词或实际使用的参数。
