# 来源与检索记录

检索日期：2026-10-11（Asia/Shanghai）。安装量与 GitHub stars 是当日快照，不代表生成质量；许可证信息取自对应仓库当时的文件与 GitHub API，不能用仓库热度代替内容检查。

## 指定参考

| 来源 | 核实结果 | 本项目对应方向 |
| --- | --- | --- |
| [Whiplashzeb/photo-to-zine-postcard](https://github.com/Whiplashzeb/photo-to-zine-postcard) | 256 stars；CLI 检索约 33 installs；仓库含 [MIT LICENSE](https://github.com/Whiplashzeb/photo-to-zine-postcard/blob/0091403bccb219d1be78c5be8552de29a6446f0a/LICENSE) | `photo-zine-postcard`：照片为主、纸面留白、小景呼应；本项目默认仅正面，背面按用户请求增加 |
| [Zeejay0/gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) | 5,364 stars；`scenes-gathered-zine-v1-3` 约 768 installs，`scene-distillation-zine-v1-3` 约 363；[LICENSE](https://github.com/Zeejay0/gathered-scenes-zine-skill/blob/b9edb836c9dd5c5d80995e89ebcaba34b75fd58f/LICENSE) 为 Personal Non-Commercial License | `photo-paper-collage`：参考实景与纸艺结合的方向，独立定义纸片层次与版面；没有引入上游 Live Photo 应用或脚本 |
| [xiaochengtong/watercolor-travel-card](https://github.com/xiaochengtong/watercolor-travel-card) | 3 stars；按该 owner 检索未找到匹配项；该版本文件树无 LICENSE | `photo-watercolor-card`：钢笔淡彩旅行卡；本项目支持用户指定语言、保留天气与色温，不猜测地点 |

核实源码版本与入口：

- 明信片：[`0091403bccb219d1be78c5be8552de29a6446f0a / SKILL.md`](https://github.com/Whiplashzeb/photo-to-zine-postcard/blob/0091403bccb219d1be78c5be8552de29a6446f0a/SKILL.md)。
- 实景拼贴：[`b9edb836c9dd5c5d80995e89ebcaba34b75fd58f / scenes-gathered-zine-v1-3`](https://github.com/Zeejay0/gathered-scenes-zine-skill/blob/b9edb836c9dd5c5d80995e89ebcaba34b75fd58f/skills/scenes-gathered-zine-v1-3/SKILL.md)。
- 水彩旅行卡：[`67ad8ee2b5dffc5eb67d7188ab048fc22a7bf498 / SKILL.md`](https://github.com/xiaochengtong/watercolor-travel-card/blob/67ad8ee2b5dffc5eb67d7188ab048fc22a7bf498/SKILL.md)。

上游来源只用于风格研究；未复制其技能正文、提示词、配置、案例图片、应用或脚本进本项目。这里的来源记录不授予上游材料的使用或再分发许可；若另外安装上游，仍需查看其当前许可。本项目没有替上游设定统一许可证。

## 补充候选

先查看 [skills.sh 榜单](https://skills.sh/)，再检索具体风格。榜单中的通用图像或设计技能不足以直接覆盖这组照片风格。

| 候选 | 质量核实 | 处理决定 |
| --- | --- | --- |
| [bergside/awesome-design-skills · riso](https://github.com/bergside/awesome-design-skills/tree/f631a09b4fcc0166f2e2c1a8c81906ef680c57e8/skills/riso) | 3,123 stars；约 1.7K installs；MIT；正文主要规定 UI 设计系统、tokens 与组件行为 | 场景不匹配，不作为照片处理 skill 安装 |
| [luckdvr/photo-riso-poster](https://github.com/luckdvr/photo-riso-poster/blob/79564228948fd393ecf58ee9aeb74fbc3c1f1deb/SKILL.md) | 52 stars；约 13 installs；MIT；正文是照片孔版海报，采用文字描述后生图 | 仅作候选研究；本项目 `photo-risograph` 保留源照片参考，不沿用其 text-only 限制 |
| 胶片与电影照片调色 | `photo film` 检索出现大量非调色结果，没有确认可直接复用的精确匹配 | 独立编写 `photo-film-grade` 与 `photo-cinematic-grade`，强调内容保留与光色依据 |
| 蓝晒印相 | `cyanotype` 返回大量词义或领域无关项，未确认精确匹配 | 独立编写 `photo-cyanotype`，区分摄影印相与物件接触印相 |
| 浮世绘木版 | `ukiyo-e` 返回泛图像或低安装量项，未确认可直接采用的照片工作流 | 独立编写 `photo-ukiyo-e`，保留真实场景和现代服饰 |

以上数字来自 CLI 与 GitHub 源仓库检查，不因候选名称或搜索排名直接推荐安装。

## 复现检索

```bash
npx --yes skills find "photo zine"
npx --yes skills find "photo film"
npx --yes skills find "watercolor"
npx --yes skills find "risograph"
npx --yes skills find "photo" --owner xiaochengtong
npx --yes skills find "cyanotype"
npx --yes skills find "ukiyo-e"
```

项目目录与调用方式参考 [OpenAI 官方技能文档](https://learn.chatgpt.com/docs/build-skills?product=breeze)。风格提示词没有锁定图像模型或外部服务，使用时以当前会话工具的参数与能力为准。
