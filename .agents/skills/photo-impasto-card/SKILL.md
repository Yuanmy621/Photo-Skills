---
name: photo-impasto-card
description: 将照片转绘为有立体颜料堆积、刮刀痕和雕塑感的厚涂油画纪念卡。用于厚涂油画、油画微景观、温暖肖像或宠物艺术卡；普通油画滤镜、透明水彩和保留摄影主图的排版不使用此技能。
---

# 厚涂油画纪念卡

让照片中的人物、宠物或景物成为有触感的油画作品。风格的核心是可见的颜料厚度和有方向的笔触，画面仍须让人认出原来的主体。

## 读图与构图

- 查看照片，记录主体身份、人数、姿势、轮廓和关键背景关系；从源图提取主色及光线方向。脸部、眼神和宠物毛色是辨识锚点。
- 默认一张竖版 2:3 的暖白纸艺术卡。把场景转绘为一个连贯的画面，边缘可渐渐露出纸白，不增加与照片无关的花环、景物或人物。
- 沿用原场景的前后关系；调整画幅时通过纸面留白容纳源图，不裁掉重要主体。用户指定比例、保留项和裁切优先。

## 颜料与画面

- 用厚实、不透明的油彩色块建立形体，出现细小颜料脊、刮刀断面和层层叠压。凸起随原有光线产生细微明暗，不增加一套强烈的新灯光。
- 笔触顺着头发、毛发、衣褶、树冠或地形走；脸部用更细的色块维持五官，背景可用较宽的刮刀痕。不要把皮肤变成无纹理的塑料表面。
- 在源图配色上适度提高色彩鲜活度，暖光和冷色阴影保持自然。浅色纸白和松散画面边缘提供呼吸感，避免全幅堆满同样大小的碎笔触。
- 作品是平面的油画卡图稿；颜料可以有厚度，但不能变成树脂玩偶、3D 场景模型或装框样机。
- 默认无字。需要标题时按用户文本和语言排版；书写感可作为字形选择，不补写地点、日期、关系或故事。

## 执行与检查

先用 `view_image` 查看本地源图，再以源图为内容参考调用图像编辑工具。使用 `image_gen` 时，本地输入用 `referenced_image_paths`；无本地路径时用覆盖输入的最小 `num_last_images_to_include`，不并用。普通卡片背景不透明。

检查主体是否仍可辨认、姿势与人数是否对应原图，以及缩略图和细节图中是否都能看出油彩厚度。人物变脸先修身份；只有平滑色块时加强颜料脊和刮刀痕；像水彩时改用不透明厚色；边缘拥挤时减少背景笔触。只修正实际观察到的问题。

仅要提示词时不出图。工具不可用时交付最终提示词并说明限制，不声称已生成，也不自行改用需要额外配置的服务。

## 提示词骨架

替换观察结果与用户要求，删除没有内容的可选字段。

```text
Reinterpret the supplied photograph as a tactile impasto oil-painting card,
{aspect_ratio}, on warm ivory paper. Preserve {identities_poses_and_layout}.
Build forms with opaque sculptural paint, small raised pigment ridges and
directional palette-knife strokes following {source_shapes}.
Keep recognizable facial features and {key_details}, with finer strokes
on the subjects and broader paint marks in the source background.
Use {source_palette} and the existing {light_direction}; allow loose painted
edges to dissolve into quiet paper. Text: {exact_text_or_no_text}.
No changed faces, extra scenery, watercolor washes, smooth plastic surfaces,
3D figurines, decorative frame or photographed mockup. Flat artwork.
```

交付图像与一句颜料和配色说明。成品默认保存到 `output/photo-impasto-card/`，用户指定位置优先；保留源文件名并加风格后缀，重名增加版本号，不覆盖原图。预览直接展示，复用时附实际提示词。
