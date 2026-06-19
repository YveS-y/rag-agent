# Credit Ops Agent · knowledge_base RAG 学习旅程卡

> **单文件自包含**：任何 AI 读到本文件都能无缝接手陪学；学员自己更新进度。
> **当前阶段**：阶段 U2 — knowledge_base 源码精读（**Spec-Driven Learning 闯关式学习法** · 2026-05-08 升级）
> **🎯 终极目标**：通关后不以「读懂代码」收工，而是**能用自己写的节点 Spec 集驱动 AI 重新生成这个项目**（Vibe Coding）。学习的核心产物是 **Spec + 判断力**，不是知识点记忆。
> **源码位置**：`/Users/ys/code/ai_agent/knowledge_base/`（59 个 .py 文件）
> **配套文档**：
> - 知识地图：`docs/learning/knowledge-base-architecture.md`（阶段 U2 交付物，精读后产出）
> - 错题本：[./kb-mistake-book.md](./kb-mistake-book.md)（❌不会 / ⚠️答错 的题自动登记）
> - 进度日志：[./progress.md](./progress.md)
> - 总计划：[./plan.md](./plan.md)

---

## 🤖 AI 接手协议（切换会话后必读）

**如果你是新会话中的 AI，接到类似"继续学习 RAG / knowledge_base"的指令，请按下面 7 步执行，不要跳步**：

1. **先读本文件完整一遍**，重点看 §1 Spec-Driven 方法、§4 进度快照、§5 10 关、§8 Spec 归档集
2. **锁定当前关卡**：从 §4 拿到 `IN_PROGRESS` 关卡编号
3. **读该关卡的 Preview + Question**，并读 §4 里记录的「上次学员答案」和「遗留追问」
4. **按 §2 的 5 步循环**决定当前该抛哪个问题（优先出 Spec 型题，少出记忆型题）：
   - 学员还没开始回答 → 复述该关卡的 Question
   - 学员答了一半 → 按 §3 Feedback 规范点评 + 用「判断力 5 法」追问深层问题
   - 学员表示"过了" → 先要求学员补齐节点 Spec（50-80 字），合格后更新 §4 + §8
5. **每次回复结束**，提醒学员在 §4 手动更新：`当前关卡`、`上次提问`、`时间戳`
6. **出现 ❌ / ⚠️ 错题 → 立即登记**到 [kb-mistake-book.md](./kb-mistake-book.md) §1（一级标签 + 二级能力标签都要写）
7. **严守 §3 禁止事项**：不要代读代码、不要直接给答案、不要全是记忆型问题

> 💡 如果学员直接说"换个关卡/跳过/重做"，就按学员指令调整 §4，不要自作主张。

---

## 🧠 §1 学习方法：Spec-Driven Learning（规格驱动学习）

### 🌟 核心三角

```
  Spec（产物）         ← 节点功能 / 约束 / 取舍的结构化描述
     ↓
  判断力（能力）       ← 能看出 AI 方案在你场景下有没有坑
     ↓
  Vibe Coding（结果）  ← 用 Spec 驱动 AI 写代码 + 判断力把关 + 迭代
```

**学习目标不再是「记住代码怎么写」，而是「能描述需求 + 能判断方案」**。

### 🔄 每关的 5 步循环（原 4 步循环升级版）

```
📍 Preview    AI 给定位（源码文件 + 2-3 句背景）
       ↓
❓ Question   AI 抛 Spec 型问题（非记忆型）：为什么 / 反例 / 场景代入 / 对比
       ↓
🗣 Explain    学员用自己的话答 + 写一段节点 Spec（50-80 字）
       ↓
🔧 Feedback   AI 按「描述力」「判断力」两维度点评 + 追问 1 个反例/对比
       ↓
📐 Spec 落库   学员写的 Spec 归档（通关后所有 Spec 拼成完整 Spec 集，可喂 AI 重写项目）
       ↓
   重复直到满足通关标准 → 进下一关
```

### 📚 两类知识维度（错题本按这分二级标签）

| 维度 | 含义 | 漏洞标签 |
|---|---|---|
| **描述力** | 能清晰描述需求/约束让 AI 准确生成 | `📝描述力漏洞` |
| **判断力** | 能识别 AI 方案在特定场景的坑 | `🔍判断力漏洞` / `📐参数直觉漏洞` / `⚖️取舍盲区` |

### 🏋 判断力训练 5 法（AI 追问时按此出题）

| 方法 | 典型问法 |
|---|---|
| ① **反例法** | "如果 overlap=0 / chunk_size=200 / 没做 X 防护会怎样？" |
| ② **对比法** | "方案 A / B / C 各适合什么场景？边界在哪里？" |
| ③ **预言法** | "读源码前先预测：项目会怎么实现这里？对照后哪 3 处你没想到？" |
| ④ **场景代入法** | "这套参数代入信贷合规 / 技术博客 / 客服对话，哪里会翻车？" |
| ⑤ **失败复盘法** | 错题本回炉——每次判断失败都是一次判断力修补 |

### 📏 硬约束（AI 必须遵守）

- 每次只围绕 **1 个概念** 展开，多概念强制拆轮
- 学员说"明白了" → 回复"用你自己的话说说看"，先复述再通关
- AI 连续输出超 **3 段** 前，必须先停下抛 1 个检查问题
- **Question 种子优先出 Spec 型题**（为什么/反例/对比），**少出记忆型题**（xxx 是多少）

### 🎯 通关标准（Spec-Driven 升级版）

**必须同时满足前 2 条，第 3 条可选**：
1. ✅ 回答命中核心因果链（理解层）
2. ✅ **写出该关节点的 Spec（50-80 字，包含「做什么/不做什么/关键取舍」）**
3. ✅ 能对 AI 的反例追问给出合理回应（判断力层）

---

## 🔄 §2 每关 5 步循环（SOP）

**Preview（定位） → Question（Spec 型题） → Explain（答题 + 写 Spec） → Feedback（双维度点评 + 反例追问） → Spec 落库（归档到 §8）**

每关最少产出 1 段节点 Spec，积累到 Final 关拼成完整 Spec 集。

---

## 🤝 §3 AI 互动规范

### ✅ AI 该做的
- **Question 种子优先出 Spec 型题**（判断力 5 法：反例 / 对比 / 预言 / 场景代入 / 失败复盘），少出记忆型题
- 学员答对 → 用关键词确认，然后用「反例法」或「场景代入法」追问 1 个判断力题
- 学员答错 → 不直接给答案，用反例/对比/源码某一行提示学员自己发现问题
- **学员说"明白了"** → 回复"用你自己的话说说看"，听完复述再决定是否过关
- **每次只讲 1 个概念**，要展开多个概念时强制拆轮
- **连续输出即将超 3 段** → 先停下，问 1 个检查问题，收到回答再继续
- **每关通关前必做**：让学员写 **50-80 字的节点 Spec**（做什么/不做什么/关键取舍），AI 用「描述力 vs 判断力」两维度点评，合格后归档到 §8
- 每 3-4 关主动提出做 Mini Feynman（合上文档口述 3 分钟）
- **错题自动登记**：每轮 Feedback 结束后，如本轮出现 ❌不会 / ⚠️答错，直接写入 [kb-mistake-book.md](./kb-mistake-book.md) 的 §1，按文件内格式补全「原题 / 学员答案 / 正确答案 / 关键记忆点 / 一级标签(不会/错位/偏差/跑题) / **二级能力标签(描述力/判断力/参数直觉/取舍盲区)** 」六字段，不要漏登

### ❌ 禁止事项
- ❌ 不要把标准答案直接贴出来
- ❌ 不要跨关卡预热下一关内容
- ❌ 不要改动学员维护的 §4 进度记录
- ❌ 不要因为学员某处漏讲就自行补全——用追问让学员自己补

### 💬 Feedback 回复模板
```
【打分】✅核心对 / ⚠️部分对 / ❌偏差大
【点评】对的：xxx | 漏的：xxx | 偏的：xxx
【追问】（只问 1 个）xxx？
【建议】继续补答 / 进入下一关 / 做 Mini Feynman
```

---

## 📍 §4 当前进度快照（⚠️ 学员每次收工自己更新）

```yaml
当前关卡: L5
关卡名称: 查询图：3 路并行召回
状态: IN_PROGRESS
学习范式: Spec-Driven Learning（2026-05-08 升级）
上次提问时间: 2026-05-13
上次 AI 提的问题: ranker_weights=(0.9, 0.1)——稠密 0.9/稀疏 0.1，代入信贷合规场景合不合适？为什么？
上次学员回答摘要:
  - L5 进行中（代码逐块精读模式，学员要求先读懂每块再写 Spec）
  - step_3 ✅ 已理解：LLM 从 original_query + history_chats 提取 item_names + 重写 rewritten_query；history_chats 由主节点从 MongoDB 取（get_recent_messages limit=10）；LLM 返回 JSON 字符串，json.loads 解析成 dict_content
  - Q1 核心逻辑 ✅ 理解：分数三档（≥0.85 走三路并行 / 0.6-0.85 反问用户 / 无匹配拒答）；短路 answer 写在 step_6_deal_list；重写用途（指代消解/跨句语义）已理解
  - step_4 ✅ 已理解：输入 rewritten_query + item_names；collection = milvus_config.chunks_collection；输出 embedding_chunks（含 chunk_id/content/file_title/title/parent_title/item_name）
  - 关键纠偏：item_names 是 expr 过滤条件，不是向量化对象；向量化的是 rewritten_query；"查询向量 vs 过滤条件"区别待确认消化
遗留追问: 1. generate_embeddings 入参是 rewritten_query 还是 item_names（引导理解查询向量 vs 过滤条件）2. ranker_weights=(0.9,0.1) 代入信贷合规场景是否合适？
下一步:
  - 确认学员理解"查询向量 vs 过滤条件"的区别
  - 继续 ranker_weights 判断力题
  - step_5 → step_6 → 写 L5 节点 Spec → 归档 §8 → Q2/Q3
```

---

## 📋 §5 10 关详情

> ⭐ = 重点关卡（面试高频）｜ ⏱ 预估耗时

### ✅ 通关记录（学员自更新）

- [x] **L0** RAG 双图架构俯瞰 ⏱10min ✅ 2026-05-08
- [x] **L1** ⭐ 导入图：节点链 + 条件路由 ⏱20min ✅ 2026-05-08
- [x] **L2** PDF → Markdown（MinerU 解析）⏱15min ✅ 2026-05-08
- [x] **L3** ⭐ 2 段切片策略 ⏱20min ✅ 2026-05-09（Spec v1→v4 迭代 4 版，错题 #006/#007）
- [x] **L4** ⭐ BGE-M3 稠密+稀疏混合向量化 ⏱20min ✅ 2026-05-09（Spec v1→v2 迭代 2 版，错题 #008）
- [x] **L4.5** 导入图收尾：node_item_name_recognition + node_import_milvus ⏱15min ✅ 2026-05-12
- [ ] **L5** ⭐ 查询图：3 路并行召回 ⏱20min
- [ ] **L6** ⭐ HyDE 召回增强 ⏱15min
- [ ] **L7** ⭐ RRF 融合 + Cross-Encoder 精排 ⏱20min
- [ ] **L8** SSE 流式输出 + 客户端单例 ⏱15min
- [ ] **L9** 迁移到 credit-ops 的设计 ⏱20min
- [ ] **Final** 合上文档 5 分钟口述 ⏱10min

---

### L0 · RAG 双图架构俯瞰 ⏱10min

**📍 Preview**
knowledge_base 有完整的 59 个 .py 源文件，分为两条 LangGraph 图：**导入图**（文档 → 向量库）和**查询图**（用户问 → LLM 答）。读：
- `knowledge_base/app/import_process/agent/main_graph.py`
- `knowledge_base/app/query_process/agent/main_graph.py`

**❓ Question 种子**
1. 导入图和查询图各有几个节点？两图的起点节点叫什么？
2. RAG 整体流程分"离线"和"在线"两阶段，对应这两张图的哪一张？
3. 技术栈里 Milvus / MongoDB / MinIO 分别负责存什么？

**🎯 核心点**
- 导入图 7 节点（`node_entry → node_pdf_to_md → node_md_img → node_document_split → node_item_name_recognition → node_bge_embedding → node_import_milvus`），编译为 `kb_import_app`
- 查询图 7 节点（`node_item_name_confirm → 3 路并行 → node_rrf → node_rerank → node_answer_output`），编译为 `query_app`
- Milvus：向量存储（稠密+稀疏）；MongoDB：文档元数据；MinIO：原始文件（PDF/图片）

---

### L1 · ⭐ 导入图：节点链 + 条件路由 ⏱20min

**📍 Preview**
导入图的 `node_entry` 节点判断文件类型，决定走哪条路径。读 `knowledge_base/app/import_process/agent/main_graph.py`，重点看 `add_conditional_edges` 的路由函数。

**❓ Question 种子**
1. `node_entry` 做了什么判断？3 条路径分别走到哪里？
2. PDF 路径和 Markdown 路径最终在哪个节点合流？
3. 如果传入的文件既不是 PDF 也不是 Markdown，图会怎么处理？

**🎯 核心点**
- 路由规则：`PDF → node_pdf_to_md → node_md_img → node_document_split`；`MD → node_md_img → node_document_split`；其他 → `END`（直接结束）
- `node_md_img` 是 PDF 和 MD 两路的合流点（PDF 转 MD 后也走这里）
- 未知格式直接 END，不报错，容错设计

---

### L2 · PDF → Markdown（MinerU 解析）⏱15min

**📍 Preview**
PDF 里有表格、公式、图文混排，普通 pdfplumber 解析会乱序。读 `knowledge_base/app/import_process/agent/nodes/node_pdf_to_md.py`，看 MinerU 是如何调用的。

**❓ Question 种子**
1. MinerU 解析 PDF 的输出是什么格式？它比 pdfplumber 好在哪里？
2. 解析结果怎么写进 MongoDB / MinIO？这两个存储各负责存什么？
3. 图片（图文混排）的处理在哪个节点？MinerU 之后还需要哪步才能让图片可被检索？

**🎯 核心点**
- MinerU（VLM 多模态）输出结构化 Markdown，保留表格格式、识别公式；pdfplumber 按字符坐标拼接，复杂版式会乱序
- MinIO 存原始 PDF + 解析产生的图片文件；MongoDB 存解析元数据（文件名、节点状态、chunk 列表）
- `node_md_img`：提取 Markdown 中的图片，用 LLM 生成图片描述写回 Markdown，使图片内容可被 Embedding 索引

---

### L3 · ⭐ 2 段切片策略 ⏱20min

**📍 Preview**
切片质量直接决定 RAG 召回质量。这个项目用了"先语义后尺寸"的 2 段策略。读 `knowledge_base/app/import_process/agent/nodes/node_document_split.py`，重点看 `step_2_split_by_title` 和 `step_3_refine_chunks`。

**❓ Question 种子（Spec-Driven 升级版）**

「为什么」比「是什么」重要 — 回答时不必抠代码细节，只答设计因果链：

1. **为什么先按语义切、后按尺寸调**？一句话描述给 AI 听（≤30 字）
2. **chunk_size 落在 500-2000 的依据**？embedding token 上限 / LLM context / 召回精度三者怎么拉扯？
3. **为什么要保 overlap**？不保会丢什么？举一个具体的"丢信息"例子
4. **代码块防护 Prompt**：用一段 prompt 让 AI 实现「`#` 是类型注释还是 MD 标题」的判别，你怎么写？
5. **📐 Spec 产出**（通关硬要求）：写一段 node_document_split 的 Spec（50-80 字，含做什么 / 不做什么 / 关键取舍），归档到 §8

**🏋 判断力追问（AI 按需投放）**
- 反例：overlap=0 / chunk_size=200 / 不防护代码块 的 3 个翻车场景
- 对比：按标题切 vs 固定字数切 vs 语义聚类切的边界
- 场景代入：chunk_size=2000 在合规文档 / 技术博客 / 聊天记录各能不能用

**🎯 核心点**（仅供 AI 核对，不要直接读给学员）
- `step_2_split_by_title`：按 Markdown 标题（`#` 层级）切，代码块内遇到标题不切（防止代码块断裂）
- `step_3_refine_chunks`：`split_long_section`（chunk > 2000 chars 用 `RecursiveCharacterTextSplitter` chunk_size=2000, overlap=100 再切）+ `merge_short_sections`（chunk < 500 chars 且同一 `parent_title` 就合并到前一块）
- 一步到位的固定字数切片会割裂语义边界（如把一条政策条文从中间截断）；先按标题保证语义完整，再按尺寸控制 token 成本

---

### L4 · ⭐ BGE-M3 稠密+稀疏混合向量化 ⏱20min

**📍 Preview**
传统 Embedding 只产生一个稠密向量（无法精确匹配关键词）。BGE-M3 同时输出稠密向量（语义相似度）+ 稀疏向量（BM25 类关键词权重）。读 `knowledge_base/app/import_process/agent/nodes/node_bge_embedding.py`。

**❓ Question 种子**
1. 代码里怎么调 BGE-M3 同时得到稠密和稀疏向量？两种向量分别存进 Milvus 的哪个字段？
2. 文本格式为什么要写成 `"商品：{item_name}，内容介绍：{item_content}"` 而不是直接存 chunk 原文？
3. 批处理大小（batch_size）为什么设 5？如果设 100 会出什么问题？

**🎯 核心点**
- BGE-M3 的 `encode(return_dense=True, return_sparse=True)`，稠密向量存 `dense_vector` 字段，稀疏向量存 `sparse_vector` 字段（Milvus 原生支持 sparse float 类型）
- `item_name` 前置：BGE-M3 对前 128 token 赋予更高权重，把最重要的标识符放前面，提升检索准确率
- batch_size=5：BGE-M3 本地推理显存占用大，批量过大会 OOM；5 是在速度和显存之间取的平衡点

---

## L4.5 · 导入图收尾：item_name 识别 + Milvus 入库 ⏱15min（迷你关）

**📍 Preview**
导入图最后两个节点，课程卡原版漏讲，2026-05-11 学员质疑后补齐。
- `knowledge_base/app/import_process/agent/nodes/node_item_name_recognition.py`（LLM 从文档里识别/抽出 item_name）
- `knowledge_base/app/import_process/agent/nodes/node_import_milvus.py`（稠密+稀疏双向量写入 Milvus 的收尾）

**❓ Question 种子（Spec 型，优先判断力）**
1. `item_name` 为什么要**单独一个节点用 LLM 识别**？和在 L3 切片阶段顺手从文件名拿有什么本质差别？（反例：直接用文件名当 item_name 会出什么问题？）
2. `node_import_milvus` 要建立的 Milvus Collection schema 里至少有哪几个字段？**稠密向量字段和稀疏向量字段是同一列还是两列**？为什么？
3. 批量写 Milvus 失败（网络抖动/部分 chunk 写失败）时，这一步应该怎么兜底？（全回滚 / 跳过失败 chunk / 整批重试，你选哪个，为什么？）
4. **📐 Spec 产出**：写一段「L4.5 导入图收尾」合并 Spec（50-80 字，覆盖两节点的做什么/不做什么/关键取舍），归档 §8 L4.5

**🏋 判断力追问（AI 按需投放）**
- 反例：item_name 识别错（把目录当成知识条目）会对 L5 查询造成什么连锁污染？
- 对比：Milvus schema 里放 `item_name` 字段 vs 放 `collection = item_name`（一个 item 一个 collection）两种隔离方式
- 场景代入：信贷合规文档，item_name = 《催收管理办法》，同一份文档切成 200 个 chunk 都挂这个 item_name，查询时怎么避免"全文档误召回"？

**🎯 核心点**（仅供 AI 核对，不直接读给学员）
- item_name 独立节点的动机：文件名不等于业务知识条目名（文件名常是「v3_final_最终版.pdf」），需 LLM 从正文抽语义级条目名；一次识别全 chunk 复用，避免切片阶段 N 次调用
- Milvus schema：`id / item_name / content / dense_vector (float向量列) / sparse_vector (sparse float列)` —— 稠密和稀疏是**两列独立字段**，Milvus 原生支持两种 index（HNSW for dense, SPARSE_INVERTED for sparse）
- 失败兜底：典型做法是**跳过失败 chunk + 日志记录 + 整节点失败抛异常让 LangGraph 走错误分支**；全回滚代价高（大文档要重跑 BGE-M3），整批重试在网络抖动时有效但同一条数据永远失败会死循环

---

### L5 · ⭐ 查询图：3 路并行召回 ⏱20min

**📍 Preview**
查询图的核心设计：先确认用户问的是哪个"商品/知识条目"，再对 Milvus 发 3 路并行检索。读 `knowledge_base/app/query_process/agent/main_graph.py`，重点看 `node_item_name_confirm` 后的分支结构。

**❓ Question 种子**
1. `node_item_name_confirm` 做什么？为什么查询前先要"确认 item_name"？
2. 3 路召回分别是哪三路？LangGraph 里怎么实现"并行执行"这三路？
3. 如果用户问的问题跨多个知识条目（item_name 模糊），`node_item_name_confirm` 怎么处理？

**🎯 核心点**
- `node_item_name_confirm`：LLM 从用户问题里识别 item_name（对应知识库里的文档标识符），用于过滤 Milvus 检索范围，避免跨文档噪声
- 3 路：`node_search_embedding`（BGE-M3 稠密+稀疏混合检索）+ `node_search_embedding_hyde`（HyDE 增强检索）+ `node_web_search_mcp`（联网搜索兜底）；LangGraph 的 `fan_out` 并行节点实现
- item_name 模糊时：LLM 返回最可能的 item_name，或返回"不确定"触发用户确认交互

---

### L6 · ⭐ HyDE 召回增强 ⏱15min

**📍 Preview**
用户的问题（"X 是什么？"）和知识库里的答案（"X 是……"）在向量空间里距离可能很远。HyDE 的思路：先让 LLM 生成一个"假设答案"，再用假设答案的向量去检索。读 `knowledge_base/app/query_process/agent/nodes/node_search_embedding_hyde.py`。

**❓ Question 种子**
1. `step_1_create_hyde_doc` 里 LLM 收到什么 Prompt？生成的假设答案长度有什么要求？
2. `step_2_search_embedding_hyde` 里，向量化的输入是原始问题还是假设答案，还是两者拼接？
3. HyDE 比直接向量检索多一次 LLM 调用，什么场景下这个额外成本值得付出？

**🎯 核心点**
- Prompt 要求 LLM 直接给出一段类似知识库文档的回答（而不是说"这是个问题"），生成内容模拟文档风格
- 两者拼接：`原始问题 + "\n" + hyde_doc`，再整体向量化；拼接能同时保留查询意图和文档语言风格
- 适合"概念解释类"问题（问法和答案措辞差异大）；不适合精确关键词匹配场景（此时直接 BM25 更好）

---

### L7 · ⭐ RRF 融合 + Cross-Encoder 精排 ⏱20min

**📍 Preview**
3 路召回结果的分数量纲不同（向量相似度 vs 网页 relevance score），不能直接加权平均。RRF 按排名而非分数合并。读 `knowledge_base/app/query_process/agent/nodes/node_rrf.py` 和 `node_rerank.py`。

**❓ Question 种子**
1. RRF 的分数公式是什么？常数 60 的作用是什么（改成 10 或 200 会怎样）？
2. RRF 代码里怎么做去重？如果同一个 chunk_id 出现在 2 路召回里，它的最终得分怎么算？
3. Cross-Encoder Reranker 和 Bi-Encoder（用于召回的 BGE-M3）的核心区别是什么？为什么 Reranker 只能做精排不能做召回？

**🎯 核心点**
- RRF 公式：`score = Σ(1/(60+rank) × weight)`，60 是平滑常数，防止 rank=1 时分数过大（改小会放大头部优势，改大会趋向均匀）
- 去重：`chunk_dict.setdefault(chunk_id, 0.0)` 初始化，每次出现就累加得分；最终按 score 降序取 top_k
- Cross-Encoder：问题+文档拼接后一起送入模型，计算精确关联度（慢，O(n)）；Bi-Encoder：问题和文档分别编码，用向量距离近似（快，可预计算，适合大规模召回）；Reranker 因为慢只能对小候选集（20-50 条）精排

---

### L8 · SSE 流式输出 + 客户端单例 ⏱15min

**📍 Preview**
knowledge_base 的 API 层用 SSE 流式返回答案（和 data-agent 一样）。客户端（Milvus/MongoDB/MinIO）用单例模式避免重复连接。读 `knowledge_base/app/sse/` + `knowledge_base/app/clients/`。

**❓ Question 种子**
1. SSE 和 WebSocket 的核心区别是什么？knowledge_base 为什么选 SSE 而不是 WebSocket？
2. 客户端单例是怎么实现的？和 data-agent 里的单例实现有什么相同点？
3. `node_answer_output` 里怎么把 LLM 流式 token 转成 SSE 事件推送给前端？

**🎯 核心点**
- SSE：HTTP 单向推送（服务端 → 客户端），实现简单，适合问答流式输出；WebSocket：全双工，适合实时双向交互（如 deep_search_pro 的任务监控）
- 单例：模块级变量 + 懒加载（首次访问时初始化），和 data-agent 的 `clients/` 同样的延迟初始化模式
- `yield f"data: {token}\n\n"` 逐 token 推送，FastAPI 的 `StreamingResponse` 包装

---

### L9 · 迁移到 credit-ops 的设计 ⏱20min

**📍 Preview**
把 knowledge_base 的 RAG 能力迁移到信贷贷后场景。无特定代码，开放设计题。

**❓ Question 种子（开放）**
1. 信贷合规文档（PDF，大量表格和政策条文）用 2 段切片策略，`merge_short_sections` 的阈值 500 chars 够不够？需要调大还是调小？
2. 催收话术场景里，用户问"M2 逾期客户该说什么开场白"，3 路召回中哪路最可能找到正确答案？为什么？
3. 幻觉治理对信贷合规场景为什么特别重要？工程层面怎么加"召回为空时拒答"？

**🎯 核心点**（无标准答案，学员自由发挥）
- 合规文档段落普遍较短（一条规定 100-200 chars），建议调低合并阈值（比如 200 chars），或直接按条文编号切
- 催收话术是精确业务词，BGE-M3 稀疏向量（关键词权重）召回最可能命中；HyDE 适合概念解释型问题
- 幻觉风险：LLM 编造合规规则 → 催收员执行 → 监管处罚；工程层面：检测 `retrieved_docs` 为空时直接返回"知识库中无相关内容"，不进入 LLM 生成

**💡 这关结束后**：在 `docs/learning/knowledge-base-architecture.md` 末尾追加「我的质疑与思考」小节（≥ 3 条自己写的观点）

---

### Final · Spec 集驱动 AI 重写项目 ⏱30min（**Spec-Driven 升级版**）

**动作**（分三场）：

**场 1 · 3 分钟口述面试（原版保留）**
1. RAG 双图整体架构（60s）
2. 2 段切片策略（60s）
3. 三大面试考点各 60s：BGE-M3 稠密+稀疏 / HyDE + RRF / Cross-Encoder Reranker

**场 2 · Spec 集终极考核 ⭐**
- 打开 §8 归档的 10 段节点 Spec，合上项目源码
- 把 10 段 Spec 拼成一份完整 Spec 文档，交给一个**干净的 AI 会话**（新开窗口、没有项目上下文）
- 让 AI 根据 Spec 生成整个 knowledge_base 项目骨架（至少导入图 7 节点 + 查询图 7 节点的函数签名 + 核心逻辑）
- **检查 AI 产出**：函数签名对不对？节点顺序对不对？关键阈值/防护有没有缺？

**场 3 · Vibe Coding 对抗 ⭐**
- 准备 3 个新场景（信贷合规 / 催收话术 / 客服对话），要求 AI 基于你的 Spec 做局部调整（比如合规文档要把 chunk_size 调小）
- **你的任务**：判断 AI 给的调整方案对不对、哪里还有坑，给出 review 意见

**通关标准**（必须全中）：
- ✅ 口述不卡壳
- ✅ **AI 根据你的 Spec 产出的代码能直接 review、大方向正确（允许细节差异）**
- ✅ **3 个对抗场景里能至少指出 AI 方案的 2 处坑**

---

## 🔗 §6 关联文档

| 文件 | 作用 |
|---|---|
| `knowledge_base/app/import_process/agent/main_graph.py` | 导入图（7 节点 + 条件路由）|
| `knowledge_base/app/import_process/agent/nodes/` | 导入节点实现（切片、向量化等）|
| `knowledge_base/app/query_process/agent/main_graph.py` | 查询图（7 节点 + 3 路并行）|
| `knowledge_base/app/query_process/agent/nodes/` | 查询节点实现（HyDE、RRF、Rerank）|
| `knowledge_base/CLAUDE.md` | 项目完整文档（技术栈、目录结构、外部服务地址）|
| [./plan.md](./plan.md) | 双轨计划总览 |
| [./progress.md](./progress.md) | 进度日志 |

---

## 📝 §7 学员使用提示

1. **每次开新会话**：把本文件 @ 给 AI，说"继续学习 RAG / knowledge_base"即可
2. **每次收工**：更新 §4 进度快照
3. **每过一关**：勾选 §5 通关记录 + 把节点 Spec 归档到 §8
4. **全部通关后**：执行 Final 的 Spec 集驱动 AI 重写验证，通过后 progress.md 追加"阶段 U2 彻底收官"，切换 U3

> 💬 遇到 AI 直接给答案 → 引用本文件 §3 禁止事项提醒。
> 💬 遇到 AI 不问 Spec 型题、只问记忆型题 → 引用 §1「判断力训练 5 法」提醒升级问法。

---

## 📐 §8 Spec 归档集（学员每关通关后追加一段）

> **格式**：每关一段，50-80 字，三要素：**做什么 / 不做什么 / 关键取舍**
> **用途**：Final 关把全部 10 段拼起来喂 AI，验证能否重现项目

### L0 · RAG 双图架构（待学员补写）

### L1 · 导入图路由（待学员补写）

### L2 · node_pdf_to_md（待学员补写）

### L3 · node_document_split ✅ 2026-05-09

> 切分 md 文件，输出内容为 `title/content/parent_title`。
> 先按标题语义切分，再通过字符串长度精修，字符串长度控制在 2000~500 之间，chunk 间可相互覆盖 100 个字符串。500-2000 是召回精度(小) vs 生成质量(大) 的帕累托区间，参数不可随意调。
> 判断标题的依据是当前行以 `#` 开头，跳过代码块内的和引用的 `#` 开头，比如 ``` # 和 > #。

**迭代轨迹**：v1(150字，缺取舍) → v2(术语混淆) → v3(压缩过头丢防护) → v4(三要素齐 ✅)
**配套错题**：#006 召回精度方向（📐参数直觉）、#007 Prompt 反例必要性（📝描述力）

### L4 · node_bge_embedding ✅ 2026-05-09

> 收到切分好的 chunk，通过 BGE-M3 模型做稀疏+稠密向量化。chunk 前要拼 `item_name` 抢占前置 token 权重、并避免和其他 chunk 向量化结果相近。
> 这里不做切分、不做入库。批次大小=5，权衡 GPU 显存、吞吐效率、失败重试成本的帕累托点。

**迭代轨迹**：v1(漏失败重试成本、漏稠密+稀疏特色) → v2(3 股力全补齐、双向量特色带上 ✅)
**配套错题**：#008 batch_size 三股力漏失败重试成本 + GPU/CPU 混淆（📐参数直觉漏洞，第 2 次）

### L4.5 · 导入图收尾（node_item_name_recognition + node_import_milvus）✅ 2026-05-12

> `node_item_name_recognition`：调用 LLM 从正文语义中提取业务条目名（item_name），写入 state 供全部 chunk 复用；不用文件名（含版本/日期噪声），只调一次 LLM，不切分不搜索。
>
> `node_import_milvus`：将 chunk 及双向量写入 Milvus；若 collection 不存在则建 schema + 双索引（幂等保护）；稠密向量建图索引（HNSW，高维连续分布），稀疏向量建倒排索引（维度大量为零，只处理非零维）。不切分，不搜索。

### L5 · 查询图 3 路召回（待学员补写）

### L6 · node_search_embedding_hyde（待学员补写）

### L7 · node_rrf + node_rerank（待学员补写）

### L8 · SSE + 客户端单例（待学员补写）

### L9 · credit-ops 迁移 Spec（待学员补写）

---

> 🏁 **毕业线**：§8 的 10 段 Spec 全部补齐 + Final 关 3 场考核通过 = 阶段 U2 通关。
