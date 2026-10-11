---
name: photo-paper-print
description: 将完整摄影主图与同场景的干刷木版印迹组合成纸上记忆卡，使用有限油墨、纸白留痕与安静留白。用于纸上记忆版画、照片加版画明信片；全幅浮世绘、孔版网点和蓝晒印相不使用此技能。
---

# 纸上记忆版画

用上方的真实照片记录瞬间，下方的印迹提炼同一个场景。摄影与版画必须同时存在，不能只给照片加纸边，也不能把整张卡转成一幅插画。

## 画面结构

- 查看照片，记录原始比例、主体轮廓、人数和空间关系；选出能缩小后仍辨认的核心组合，例如屋顶与猫、禽鸟与水纹、建筑与栏杆。
- 默认竖版 2:3、浅暖白纸。上方等比放置完整摄影主图，保留纸边；下方以留白围住一幅较小的版画。横向照片不拉伸为竖图，不擅自裁切。
- 下方版画重现选出的主体组合及相对位置，弱化次要背景。它是从原场景提炼的印相，而不是无关植物小装饰或第二张照片。

## 印迹语言

- 从源图选两到三种低饱和墨色。用主体剪影、刻线和断续干刷表达，纸白成为印迹间隙；避免均匀的数码色块。
- 细纸纹、墨色缺口、轻微擦印和不齐的笔触边缘可以存在，细节集中在最有辨识度的轮廓。不要把所有边缘做成脏污破损。
- 印迹周围留出清楚的空白；可以有少量从源图提取的水纹、瓦片或枝叶，不重复主体，不增加太阳、鸟群或景物。
- 主照片保持摄影质感；下方才出现木版与干刷。无需浮世绘题签、孔版网点、蓝白滤镜或整幅古风重画。
- 默认无字；标题、语言、地点和日期按用户提供的内容使用。若要求摄影像素级不变，使用可直接嵌入原图的排版能力，否则说明生成式编辑的限制。

## 执行与验收

用 `view_image` 查看本地源图。图像编辑时明确源图是主照片与下方版画的共同内容来源。`image_gen` 的本地输入用 `referenced_image_paths`；其他输入用最小 `num_last_images_to_include`，不同时提供两者。纸底默认不透明。

检查主照片比例与身份、上下两幅内容的对应关系、印迹的纸白缺口和留白。下方只是平滑矢量图时修墨迹；摄影被转绘时恢复摄影约束；场景不对应时只重新提炼源图。仅修正可见问题。

工具不可用时说明限制并交付提示词；用户只要提示词时不生成，不切换到未经要求的额外服务。

## 提示词骨架

```text
Design a {aspect_ratio} paper-memory print card on warm pale paper.
Place the complete supplied photograph proportionally in the upper area,
preserving {identity_objects_and_spatial_relationships} as photography.
Below it, reinterpret {source_subject_group} as a small relief-print vignette
with {source_ink_colors}, carved lines, broken dry-brush ink and paper-white
gaps. Keep the original silhouettes and relative positions of that group.
Surround the print with generous quiet paper. Text: {exact_text_or_no_text}.
No stretched photograph, unrelated decorations, new scenery, duplicate
subjects, smooth vector fill, halftone grid, frame or mockup. Opaque artwork.
```

替换全部变量，无值行删除。交付图像和一句印迹说明；默认保存到 `output/photo-paper-print/`，沿用源名加风格后缀与必要版本号，不覆盖原图。指定目录优先，预览直接展示，复用时附实际提示词。
