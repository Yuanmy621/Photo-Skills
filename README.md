# Photo Skills

Photo Skills 是一个面向 Codex 的照片风格技能库，提供 14 种照片排版、调色和艺术转绘工作流。上传照片并选择风格，即可生成厚涂油画卡、纸艺拼贴、水彩纪念卡、版画、互动涂鸦或编辑海报，也可以单独获取可复用的提示词。

## 项目特点

- **风格独立**：每种风格都有专门的适用场景、视觉规则和提示词模板，可单独调用。
- **主体保真**：根据风格保留人物身份、建筑结构和关键空间关系，支持指定必须保留的细节。
- **灵活定制**：支持画幅、文字、语言、配色、风格强度及输出位置等要求。
- **可复用流程**：包含生成、检查与纠偏步骤，适合单张创作和系列照片处理。

## 八种艺术卡与海报

| Skill | 风格与用途 | 对照片的处理 |
| --- | --- | --- |
| [photo-impasto-card](.agents/skills/photo-impasto-card/SKILL.md) | 厚涂油画：凸起颜料、刮刀痕、有方向的油彩笔触 | 全幅转绘，保持主体辨识度与场景关系 |
| [photo-paper-collage](.agents/skills/photo-paper-collage/SKILL.md) | 实景纸艺拼贴：真实主角、撕纸边、粗颗粒色带 | 主体保持摄影，周围场景与纸艺连续融合 |
| [photo-watercolor-card](.agents/skills/photo-watercolor-card/SKILL.md) | 水彩旅行纪念卡：透明水彩、细穿孔、窄档案栏 | 转绘主画面，再组织纪念卡版式 |
| [photo-paper-print](.agents/skills/photo-paper-print/SKILL.md) | 纸上记忆版画：上方摄影、下方干刷与刻线小景 | 保留摄影主图，提炼同一场景的版画印迹 |
| [photo-doodle-characters](.agents/skills/photo-doodle-characters/SKILL.md) | 黑色小人涂鸦：微小线描人物沿源图轮廓互动 | 主体保持摄影，添加明确的线描装饰图层 |
| [photo-abstract-poster](.agents/skills/photo-abstract-poster/SKILL.md) | 极简抽象海报：摄影、几何小景、少量源图色样 | 用几何形与小剪影提炼原场景，下方大面积留白 |
| [photo-editorial-poster](.agents/skills/photo-editorial-poster/SKILL.md) | 现代单色编辑海报：窄色域、强字号层级、非对称网格 | 保留图像主体，用配色和文字结构重新设计版面 |
| [photo-crayon-card](.agents/skills/photo-crayon-card/SKILL.md) | 手绘蜡笔：干燥划痕、绕圈笔迹、纸白露痕 | 单幅转绘，可选摄影与蜡笔小景的对照卡 |

## 更多摄影与印刷风格

| Skill | 风格与用途 | 对照片的处理 |
| --- | --- | --- |
| [photo-zine-postcard](.agents/skills/photo-zine-postcard/SKILL.md) | 留白照片明信片：摄影主图、手绘小景，可选背面 | 完整保留摄影主图，增加安静的卡片设计 |
| [photo-film-grade](.agents/skills/photo-film-grade/SKILL.md) | 复古胶片：日系清透、暖色负片、黑白纪实 | 保留内容，调整色调与质感 |
| [photo-cinematic-grade](.agents/skills/photo-cinematic-grade/SKILL.md) | 电影调色：冷暖分离、低饱和叙事、夜景氛围 | 保留内容，依据已有光线调色 |
| [photo-risograph](.agents/skills/photo-risograph/SKILL.md) | 孔版印刷：双色或三色、网点、叠印、轻微套印偏移 | 转为有限油墨的平面印刷风格 |
| [photo-cyanotype](.agents/skills/photo-cyanotype/SKILL.md) | 普鲁士蓝晒：蓝白摄影印相，可选物件接触印相 | 转为蓝白层次，模式明确区分 |
| [photo-ukiyo-e](.agents/skills/photo-ukiyo-e/SKILL.md) | 浮世绘旅行版画：轮廓、平涂色面、木版纹理 | 全幅转绘，保留真实场景与时代元素 |

## 快速开始

克隆项目：

```bash
git clone https://github.com/Yuanmy621/Photo-Skills.git
cd Photo-Skills
```

在 Codex 中打开项目目录，上传照片或提供本地图片路径，再用 `$skill-name` 指定风格。技能位于项目内 `.agents/skills/`，也支持根据自然语言描述自动选择。

例如：

```text
用 $photo-watercolor-card 把这张照片做成水彩旅行纪念卡，
保留阴天氛围，用细穿孔分隔主画面与窄栏，中文标题“雨后”，不要日期。
```

如果技能暂未出现在列表中，重新加载 Codex，或直接指定文件：

```text
读取 .agents/skills/photo-watercolor-card/SKILL.md，
按照该 skill 将我提供的照片做成水彩旅行纪念卡。
```

## 调用示例

```text
用 $photo-impasto-card 把这张照片做成厚涂油画卡，要看见颜料堆积和刮刀笔触，保留人物姿势与场景，无字版。

用 $photo-paper-collage 做实景拼贴海报，人物保持真实摄影，背景结构融入撕纸与粗颗粒色带，不加新景物。

用 $photo-watercolor-card 做水彩旅行纪念卡，画面右侧用细穿孔分隔窄档案栏，标题“雨后”，不要日期。

用 $photo-paper-print 做纸上记忆版画卡，上方放完整照片，下方以干刷墨迹和刻线重现同一组主体，无字版。

用 $photo-doodle-characters 加几个微小黑色线描小人，让它们沿照片已有的边缘互动，主角保持摄影，不遮脸。

用 $photo-abstract-poster 做极简抽象海报，上方保留照片，下方用少量几何色面提炼同一场景，保留大面积留白。

用 $photo-editorial-poster 做现代单色编辑海报，浅蓝主色，标题“同行”，使用大字号和非对称网格，不添加日期或外文正文。

用 $photo-crayon-card 做手绘蜡笔艺术卡，保留干燥划痕和露白，不要水彩晕染与贴纸。
```

需要保存创作方案时，在请求中加上“同时给出最终 Prompt”。只需要提示词时，使用“仅输出提示词，不生成图片”。

## 创作设置

| 设置 | 使用方式 |
| --- | --- |
| 输入照片 | 上传图片或提供可访问的本地路径 |
| 画幅与构图 | 指定比例、横竖方向，以及是否允许裁切 |
| 保留内容 | 指定人物、建筑、标识、服饰或其他关键细节 |
| 风格与配色 | 指定风格方向、冷暖倾向、油墨颜色或效果强度 |
| 文字 | 提供准确的标题、语言与排版位置，或选择无字版 |
| 输出 | 指定保存目录；需要双面、多个版本或系列作品时说明数量 |

希望保持摄影主视觉，可选择留白明信片、纸上记忆版画、极简抽象海报或互动涂鸦；希望摄影与手工材料连续融合，可选择实景拼贴；希望全幅转绘，可选择厚涂油画、水彩或蜡笔；希望以字体和版式为主，可选择现代编辑海报。胶片与电影风格主要改变光色，孔版、蓝晒和浮世绘则有各自的印刷语言。

## 图像工具与输出

- 实际出图需要当前会话具备图像编辑或生成能力；也可使用提示词模式。
- 生成前读取照片内容，按所选风格处理，并检查主体、构图、文字和视觉效果。
- 文字采用指定语言，地点和日期使用提供的信息。没有这些信息时可省略相应字段。
- 项目成品默认保存到 `output/<skill-name>/`，指定目录优先。文件名保留源名称并添加风格后缀，重名增加版本号，原照片保持不变。
- 预览可直接在聊天中展示。`output/` 默认被 Git 忽略。
- 需要主照片像素保持不变时，明信片使用嵌入原图的排版流程；需要确定性调色时，可指定编辑工具和参数输出。

## 项目结构

```text
Photo-Skills/
├── .agents/
│   └── skills/
│       └── <skill-name>/
│           ├── SKILL.md
│           └── agents/
│               └── openai.yaml
├── scripts/
│   └── validate_skills.py
├── requirements-dev.txt
├── .gitignore
└── README.md
```

`SKILL.md` 定义触发场景、风格规则、执行流程、提示词与验收标准；`agents/openai.yaml` 提供技能的显示名称和简短说明。

## 校验与维护

安装校验依赖并运行：

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate_skills.py
```

校验覆盖技能命名与目录对应、YAML 元数据、描述、未完成占位符、UI 配置、重复名称和本地 Markdown 文件链接。图像效果需使用照片生成后单独检查。

仅查看本项目中可发现的技能，不执行安装：

```bash
npx --yes skills add . --list
```

## 扩展风格

1. 在 `.agents/skills/<skill-name>/` 创建风格目录，名称使用小写字母、数字和连字符。
2. 编写 `SKILL.md`，明确适用场景、保留项、风格规则、提示词模板和验收标准。
3. 添加 `agents/openai.yaml`，设置显示名称与简短说明。
4. 更新风格目录与调用示例，运行校验，并用照片检查生成效果。
