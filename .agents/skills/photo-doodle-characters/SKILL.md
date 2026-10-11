---
name: photo-doodle-characters
description: 为照片中的真实人物、宠物或物件添加微小黑色线描小人，让小人沿源图的边缘玩耍、攀爬或观察。用于黑色小人涂鸦、照片互动涂鸦海报；真人动漫化、全图线稿和普通贴纸拼贴不使用此技能。
---

# 黑色小人互动涂鸦

保留主角的真实摄影形象，在它周围建立一组小小的线描互动。小人的趣味来自尺度差与动作，主角不被改造成漫画人物。

## 主体与留白

- 查看源图，锁定人物身份、宠物毛色、表情、姿势和重要物件。找出可互动的真实轮廓，例如帽檐、栏杆、花盆、树枝、肩部或草地。
- 默认竖版 2:3、白色或暖白留白。可将摄影主体及相连的小片环境保留为一个自然的摄影区域，其余背景淡出为纸白；用户要求完整背景时沿用全图并只加涂鸦。
- 保留摄影区域的自然比例、皮肤与毛发细节。不放大眼睛、不改变表情，不让文字、小人或剪切边缘遮住五官。

## 小人与互动

- 添加约三到五个小黑色线描人物，人数随可用空间减少。细线、圆头和少量动作线即可；人物高度通常不超过主摄影主体的十分之一。
- 每个小人至少与一个源图已有轮廓发生联系：坐在帽檐边缘、沿栏杆攀爬、站在草地上观察，或在主体外侧举画板。必要的梯子、画板只能作为同样细小的线描道具。
- 线描小人是明确的装饰图层，不是照片中新增的真实人物；主照片里真实人物的数量、姿势和关系不变。
- 让小人贴着表面落脚，重力与动作清楚，避免悬空、穿过人体或密集围住脸部。不使用彩色卡通贴纸、表情包和巨大漫画气泡。
- 可加一条短箭头或动作线。默认无字；手写标题只用用户给出的准确文本，不凭空写人物关系或心情。

## 执行与检查

先用 `view_image` 查看源图，再以其为图像编辑目标。`image_gen` 本地参考用 `referenced_image_paths`，其他输入用覆盖全部输入的最小 `num_last_images_to_include`，两者不并用。纸面默认不透明。

检查主体仍是摄影且身份一致、小人的动作与源图边缘是否有具体联系，以及留白能否让主角突出。主体变插画先恢复摄影；小人太大时缩小；图层遮脸时移到外围；动作不成立时删去该小人，不用增加更多涂鸦补救。

只要提示词时不生成；工具不可用时交付提示词并说明限制，不假称已有成品或擅自改用额外服务。

## 提示词骨架

```text
Edit the supplied photo into a playful black-line doodle artwork,
{aspect_ratio}. Keep {photographic_subject_identity_pose_and_details}
photorealistic and at natural proportions. Background: {paper_or_full_scene}.
Add {small_number} tiny fine black-line stick characters interacting with
the existing {source_edges_and_surfaces}: {specific_actions}.
These are graphic doodles, never extra real people. Keep their scale small,
their feet anchored, and the face clear. Text: {exact_text_or_no_text}.
No face changes, cartoonized photo, colored stickers, oversized characters,
speech bubbles, dense decorations or mockup. Opaque flat artwork.
```

替换变量，删除无值行。交付图像与一句互动说明；默认保存到 `output/photo-doodle-characters/`，沿用源名、风格后缀和必要版本号，不覆盖原图。用户目录优先，预览直接展示，复用时附实际提示词。
