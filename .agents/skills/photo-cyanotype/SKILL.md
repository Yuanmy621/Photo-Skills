---
name: photo-cyanotype
description: 将照片转换成普鲁士蓝与纸白组成的蓝晒印相，控制明暗映射、接触印相层次与纸面边缘。用于 cyanotype、蓝晒、蓝白摄影印相；普通蓝色滤镜、蓝图线稿或多色孔版印刷不使用此技能。
---

# 普鲁士蓝晒印相

将照片转成有层次的蓝白印相。普通照片默认走摄影印相方向；白色剪影的 photogram 方向只用于用户明确要求的植物或物件接触印相。

## 输入与模式

- 先查看照片，识别轮廓、原有亮暗、细线与透光区域。保留人物身份、人数、建筑与构图关系，默认沿用原比例。
- 图片缺失时请用户提供。用户指定蓝度、边缘、纸色和文字时优先采用；未指定时为深普鲁士蓝、浅冷白纸、轻微不规则涂布边缘、无字。
- 摄影模式保持正常明暗阅读：暗部为深蓝，亮部接近纸白，中间调用蓝色浓度表达，不能把整幅图变成负片。
- 接触印相模式把被物体遮挡的主体表现为纸白或浅蓝，周围为深蓝；仅简化用户指定对象，不把人脸或建筑自动变白色剪影，也不增加原图没有的叶片。

## 视觉规则

- 色域为蓝到纸白。普鲁士蓝应有密度变化，不使用青紫霓虹、蓝橙双调或彩色阴影。
- 保留亮部边界与暗部细节，避免整片死蓝。植物细枝、建筑细线和人物五官不能被纸纹吞掉。
- 蓝色像进入纸纤维的感光层，局部边缘可轻微不匀，画面仍保持干净。不要把裂纹、咖啡渍与烧焦边当作蓝晒必要特征。
- 纸边为可选；满版或纯图请求去掉边缘处理。默认输出平面作品，不生成暗房器具、桌面或摄影样机。
- 文字与档案编号只按用户要求添加；地点、日期不猜测。不把数字模拟图称为实际经过化学曝光的实体蓝晒。

## 执行

用照片作为图像编辑目标或内容参考。先用 `view_image` 查看本地文件；调用 `image_gen` 时，所有目标有本地路径则用 `referenced_image_paths`，否则用覆盖全部目标的最小 `num_last_images_to_include`，不同时使用两者。纸张默认不透明；只有用户需要透明剪影素材时改变输出方式。

查看生成结果的蓝白映射与关键细节，针对实际失败修正。用户只要提示词时不生成。工具不可用时交付最终提示词并说明无法出图，不虚构文件，也不擅自切到需要额外配置的付费服务。

## 提示词骨架

摄影模式：

```text
Transform the supplied photograph into a photographic cyanotype print,
{aspect_ratio}. Preserve {identity_subjects_geometry_and_composition}.
Map dark values to deep Prussian blue, bright values to pale paper-white,
and midtones to graduated blue pigment density. Keep {important_fine_details}
visible with normal photographic tonal polarity.
Use a light fibrous paper surface and {edge_treatment}, with restrained
contact-print texture. Text: {exact_user_text_or_no_text}.
No colored accents, purple neon, simple blue overlay, negative inversion,
unrelated plants, cracked aging, props, 3D mockup, or extra lettering.
```

接触印相模式用以下段落替换明暗映射句，并删除 `negative inversion` 禁止项：

```text
Interpret only {user_selected_objects} as a contact photogram: opaque regions
leave light silhouettes against exposed deep-blue paper; translucent edges
remain pale blue. Preserve the source objects' count, shapes, and spacing.
```

所有变量在调用前替换，不把两种映射同时放进同一提示词。

## 验收与交付

- 摄影模式亮暗方向正确，接触模式白影对象确实是用户选定对象。
- 蓝色浓度形成层次，人物、细枝与建筑边缘仍可辨认。
- 只有蓝与纸白，材质细微，没有默认新增植物、污渍或档案信息。
- 暗部糊成蓝块时拉开蓝色浓度；像蓝色滤镜时加强纸纤维与印相边缘；极性错误时只改映射模式。

交付图像与模式说明。项目内默认保存到 `output/photo-cyanotype/`，用户指定位置优先；保留源名与风格后缀，重名增加版本号，不覆盖原图。预览直接展示，需要复用时附最终提示词。
