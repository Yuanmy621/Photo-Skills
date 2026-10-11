---
name: photo-paper-collage
description: 将真实摄影主体与撕纸、纸艺色面和粗颗粒笔迹融合成连续的拼贴海报。用于实景纸艺拼贴、撕纸 zine、人物旅行拼贴；完整照片加小装饰、上下分区抽象卡或整幅水彩转绘不使用此技能。
---

# 实景纸艺拼贴

把一张照片中的真实片段与纸艺形状融合成一幅连续海报。人物、宠物或地标保持摄影细节，周围的场景以撕纸、粗颗粒色带与局部线描重新组织。默认单张照片；多张照片只有在用户明确提供并要求合成时才进入同一画面。

## 读取照片

- 查看每张源图，确定摄影区域中必须留下的主体与关系：人物位置、建筑轮廓、岸线走向、道路或光影方向。
- 找出适合纸艺化的形状，如山脊、云带、窗格、植物团块；选择照片已有颜色建立少量色面。人物脸部、标识文字不作为可随意抽象的区域。
- 图片缺失时请用户提供。默认竖版 2:3，用户选定尺寸、方向、裁切、文字和语言优先。若换画幅影响重要主体，用留白与纸艺区容纳摄影区域，不裁掉主角。

## 拼贴规则

- 保留一个清楚的摄影锚点，主体和关键邻近关系应在这个区域内完整可见。摄影锚点可以偏向一侧，纸艺色面在另一侧形成平衡，不强制套用固定分区比例。
- 人物五官、衣服和动作保持摄影，沿源图已有的桥架、道路、山脊或植物边缘建立撕纸过渡。背景中的长线可以改成粗蜡笔或干刷色带，但它们仍指向原场景的结构，不随意画新的建筑。
- 用两到四块大小不同的纸艺形状构成视觉路径，避免等大小卡片网格。形状与源图中的线条、方向或轮廓发生呼应，不凭空增添景物。
- 纸张可以有局部撕边、纤维和薄层叠压；阴影仅用于轻微纸层厚度。输出是平面作品，不是桌面上拍摄的立体样机。
- 纸艺区合并细碎重复元素，留下大块形与空白；摄影区仍保持真实细节。不要把同一主体重复粘贴成多个人或多个地标。
- 摄影与纸艺应在同一个构图中穿插相接，不能退化为上方一张完整照片、下方几片独立纸片；需要上下对照的小景卡时使用相应版式，而不是强行把它叫作拼贴。
- 颜色优先取自源图，必要时以一个协调的强调色连接纸片。纹理服从层次，不能把全画面覆盖成砂纸噪点。
- 默认无字。需要标题时使用用户选定语言与准确文本，地名、日期仅用已知信息。多图合成先明确每张图的用途，不能把不同城市合成后声称是同一真实地点。

## 执行

用图像工具完成照片编辑或参考图合成。先用 `view_image` 查看本地图片；调用 `image_gen` 时，全部参考有本地路径则使用 `referenced_image_paths`，否则使用能包含全部参考的最小 `num_last_images_to_include`，两种方式不能并用。提示词明确哪部分必须保持摄影、哪部分转成纸艺，以及每张参考图的角色。纸面默认不透明。

先产出一张，查看摄影锚点与纸艺边界后进行针对性修正；一轮只调整一个主要问题。用户只要提示词时跳过生成。工具不可用时给出最终提示词并说明无法生成，不虚构文件或擅自切换到需要额外配置的付费服务。

## 提示词骨架

替换变量，无内容的可选文字行删掉。

```text
Transform the supplied photo into a flat paper-collage editorial poster,
{aspect_ratio}. Keep {photographic_anchor} recognizably photographic,
preserving {identity_and_key_spatial_relationships}.
Reinterpret {selected_source_shapes} as a small set of cut-paper forms with
{source_palette}. Integrate them continuously with the photographic subject,
using torn edges and coarse drawn strokes along existing scene structures.
Arrange varied paper shapes along {visual_direction}, leaving quiet paper
between them. Preserve one clear focal subject.
Use localized torn fibers, restrained layered-paper edges, and matte inks.
Text: {exact_user_text_and_language_or_no_text}.
No duplicate subjects, unrelated landmarks, dense sticker collections,
repeated photo frames, glossy 3D mockup, invented facts, or extra lettering.
```

## 验收与交付

- 摄影锚点仍能辨认原图，人物、地标与空间关系没有被拼错。
- 纸艺确实改变画面组织，不只是照片外加白边；同时没有变成整幅手绘。
- 真实主体与纸艺边缘形成连续场景，摄影身份和原有建筑走向仍可辨认。
- 主次、纸片层次和留白在缩略图下可读，撕边只发生在合理边界。
- 摄影区被画化时加强摄影约束；太杂时减少纸片；主体重复时删除重复层；文字逐字复核。

交付图片与一句取材说明。需要项目成品时保存到用户指定位置，未指定时为 `output/photo-paper-collage/`；保留源文件名、风格后缀与必要版本号，原图不覆盖。预览直接展示，复用需求附实际使用的提示词。
