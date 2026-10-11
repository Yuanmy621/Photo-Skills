---
name: photo-zine-postcard
description: 将用户照片设计成保留摄影主体、搭配手绘小景与大面积留白的 zine 明信片。用于照片明信片、极简旅行卡、摄影纪念卡及匹配的明信片背面；整张照片转绘或纯调色不使用此技能。
---

# 留白照片明信片

让照片成为主视觉，用从照片中提取的小景、颜色和少量文字形成可收藏的纸面作品。默认生成一张正面；只有用户要求双面或可书写背面时才增加背面。

## 输入与保留项

- 先查看源照片。记录主体、原始比例、最有辨识度的轮廓、两到三种代表颜色，以及用户给出的标题、地点、日期。
- 图片缺失时请用户提供图片。用户已指定比例、语言、文字或输出位置时沿用其选择。其余默认竖版 2:3、浅暖白纸、无标题也可成立。
- 完整保留主照片的内容和比例，默认不裁切、不拉伸。地点与日期只使用用户提供的信息，未知时省略，不能根据视觉猜测填入。

## 版式与材质

- 上半部放一张完整照片，四周保留纸边；下半部以留白为主。横向源照片按宽度等比适配，不强行填满竖框。
- 从照片中挑一个辨识度高的小景，如岸线、门窗、花枝或屋顶，用少量手绘线条与淡彩重新表达。小景为照片提供呼应，不复制一张缩小的完整风景。
- 小景与文字形成错落的视觉平衡；可加一组很小的源照片色样，但不是必需模块。纸纹保持细微，照片区域保持清晰。
- 文字采用用户选定语言，尽量短。卡片标题可以描述画面，不把未经确认的地名写成事实。需要无字版时去掉全部排版文字。
- 背面沿用纸色、线条和比例，留出主要书写区，配置地址行与邮票位。不要把正面装饰搬满背面。

## 执行

有图像编辑工具时，使用源照片作为编辑目标或明确标注的内容参考。先用 `view_image` 查看本地文件；调用 `image_gen` 时，所有目标都有本地路径则使用 `referenced_image_paths`，否则使用能覆盖所有目标的最小 `num_last_images_to_include`，不同时提供两者。遵循当前工具实际参数，纸面作品默认不透明。

先生成一张并查看结果，再只修正已观察到的问题。不要为了装饰增加照片中不存在的主体。如果用户明确要求主照片像素级不变，应选择能直接嵌入原图的排版流程：图像工具只生成纸面与手绘素材，再把原照片作为独立图层置入；如果没有这种能力，说明生成式编辑的保真限制，不承诺像素级一致。

用户只要提示词时不生成图片。图像工具不可用时交付可执行的最终提示词并说明限制，不声称已生成成品，也不擅自改用需要密钥或付费配置的服务。

## 提示词骨架

替换花括号变量；没有值的可选字段删掉整行，不把占位符送入图像工具。

```text
Design a flat zine postcard front on {aspect_ratio} pale paper.
Place the supplied photograph prominently with its full original composition
and aspect ratio intact. Preserve {photo_subject_and_spatial_relationships}.
Use generous paper margins and a quiet lower area.
Add one small hand-rendered interpretation of {source_detail}, using
{source_colors}; keep this detail subordinate to the photograph.
Typography: {exact_user_text_and_language_or_no_text}.
Paper has subtle fibers, with no heavy aging or dirt. Render as a flat artwork,
not a photographed mockup. No extra objects, stretched photo, ornate stickers,
invented location/date, or additional lettering.
```

双面请求另写背面提示词，说明相同尺寸与材质，并明确书写区、地址行、邮票位；正反面分别输出，除非用户要拼在同一页。

## 验收与交付

- 主照片内容、比例和人物身份保持一致；没有被重绘成另一处风景。
- 手绘小景确实对应源图，缩略图下仍以照片为主，纸面留白清楚。
- 文字逐字检查，未知资料未被补写；背面能正常书写。
- 照片被误改时优先修保真；版面拥挤时删装饰；文字失败时简化排版或使用可用文字排版工具，不擅自翻译。

交付图片与一句版式说明。项目内成品保存到用户指定位置，未指定时使用 `output/photo-zine-postcard/`，文件命名保留源文件名并加风格后缀，已存在时增加版本号。只保存工具实际返回的成品，不覆盖原图；预览请求直接展示。用户要求复用时附最终提示词。
