# Photo Skills

面向用户照片的 8 种后期与生成风格 skill。每个目录都包含独立的 `SKILL.md` 和 `agents/openai.yaml`，可单独使用，不依赖本仓库中的其他风格。

## 风格目录

| Skill | 风格与用途 | 对照片的处理 |
| --- | --- | --- |
| [photo-zine-postcard](.agents/skills/photo-zine-postcard/SKILL.md) | 留白照片明信片：摄影主图、手绘小景、纸面排版，可选背面 | 完整保留摄影主图，增加卡片设计 |
| [photo-paper-collage](.agents/skills/photo-paper-collage/SKILL.md) | 实景纸艺拼贴：摄影锚点、纸片层次、抽象色面 | 局部保持摄影，其他区域重新设计 |
| [photo-watercolor-card](.agents/skills/photo-watercolor-card/SKILL.md) | 钢笔水彩旅行卡：线稿、透明水彩、可选齿孔与档案栏 | 全幅转绘，保留主体与空间关系 |
| [photo-film-grade](.agents/skills/photo-film-grade/SKILL.md) | 复古胶片：日系清透、暖色负片、黑白纪实 | 保留内容，调整色调与质感 |
| [photo-cinematic-grade](.agents/skills/photo-cinematic-grade/SKILL.md) | 电影调色：冷暖分离、低饱和叙事、夜景氛围 | 保留内容，依据已有光线调色 |
| [photo-risograph](.agents/skills/photo-risograph/SKILL.md) | 孔版印刷：双色或三色、网点、叠印、轻微套印偏移 | 转为有限油墨的平面印刷风格 |
| [photo-cyanotype](.agents/skills/photo-cyanotype/SKILL.md) | 普鲁士蓝晒：蓝白摄影印相，可选物件接触印相 | 转为蓝白层次，模式明确区分 |
| [photo-ukiyo-e](.agents/skills/photo-ukiyo-e/SKILL.md) | 浮世绘旅行版画：轮廓、平涂色面、木版纹理 | 全幅转绘，保留真实场景与时代元素 |

## 使用

技能放在项目内 `.agents/skills/`，采用 Codex 的本地发现目录与默认自动选择方式；无需安装到用户全局目录。可以用 `$skill-name` 明确指定，也可以用自然语言描述风格。发现规则见 [OpenAI 官方技能文档](https://learn.chatgpt.com/docs/build-skills?product=breeze)。若技能列表未更新，重启 Codex；当前聊天也可以直接指定下方示例中的 skill 文件路径让 agent 读取。

附上照片或提供可访问的本地路径，然后使用以下示例：

```text
用 $photo-zine-postcard 把这张照片做成留白明信片，保留完整照片，标题写“秋日散步”，只要正面。

用 $photo-paper-collage 将这张湖边照片做成实景纸艺海报，保留岸线和人物，无字版。

用 $photo-watercolor-card 做钢笔水彩旅行卡，保留阴天氛围，中文标题“雨后”，不要日期。

用 $photo-film-grade 调成日系清透胶片感，保留人物身份、皮肤纹理和原始构图。

用 $photo-cinematic-grade 给这张夜景做电影调色，保留招牌文字，不添加灯光和雨水。

用 $photo-risograph 做深蓝与朱红双色孔版海报，保持原图比例，不要文字。

用 $photo-cyanotype 做摄影模式蓝晒印相，保持正常明暗方向，保留细枝和纸白。

用 $photo-ukiyo-e 将现代街景做成木版旅行画，保留现代建筑和服饰，不加日文题签。
```

如果当前会话暂未发现新技能，可以明确要求：

```text
读取 .agents/skills/photo-watercolor-card/SKILL.md，按照该 skill 将我提供的照片做成水彩旅行卡。
```

每个 skill 都有可替换变量的提示词骨架、风格约束、纠偏与验收标准。需要可复用提示词时直接要求“同时给出最终 Prompt”；只需要提示词时说明“仅输出提示词，不生成图片”。

## 图像工具与输出

- 默认使用可用的图像编辑/生成工具，并把照片作为内容依据。实际出图需要当前会话有相应能力，skill 本身不包含生图模型、API 密钥或第三方付费服务配置。
- 本地照片先查看再编辑，区分编辑目标与风格参考；没有照片时先收集照片。图像工具不可用时明确说明限制并交付提示词，不声称已生成成品。
- 用户指定的比例、语言、文字和输出位置优先。未知地点、日期不补写，中文不被强制改成英文。
- 普通生成式编辑无法承诺像素级无损。明信片需要主照片像素不变时使用直接嵌入原图的排版流程；调色需要无损或确定性参数时按用户指定编辑工具处理。
- 项目成品默认保存到 `output/<skill-name>/`，源文件名加风格后缀，重名增加版本号；用户指定目录优先。原照片不覆盖，预览可只在聊天展示。`output/` 默认被 Git 忽略。
- 只有工具支持时才交付指定格式与尺寸。数字印刷风格图不被标成已完成实际印刷分色或实体工艺。

## 校验与维护

安装校验依赖并运行：

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate_skills.py
```

校验覆盖技能命名与目录对应、YAML 元数据、描述、未完成占位符、UI 配置、重复名称和本地 Markdown 文件链接。它验证文件结构，不证明图像生成效果。新增风格应放到 `.agents/skills/<skill-name>/`，同时更新上方目录和 [来源记录](SOURCES.md)。

当前 8 个技能已通过结构校验及 `skill-creator` 的官方快速校验；Skills CLI 也已发现全部 8 项。校验脚本已在临时目录检查正常样例及空描述、错误 YAML、目录名不匹配、错误 UI 配置、缺失入口、断开链接与空技能库的失败路径。尚未用真实用户照片进行出图验收。

仅查看本项目中可发现的技能，不执行安装：

```bash
npx --yes skills add . --list
```

## 参考与发现

本项目使用 `find-skills` 检索技能生态、使用 `skill-creator` 初始化与验证技能。三个指定仓库的风格参考、补充候选、检索热度、源码版本与许可证信息见 [SOURCES.md](SOURCES.md)。项目内正文与提示词为独立编写，未直接安装或打包上游技能。
