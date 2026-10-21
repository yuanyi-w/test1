# ai-test-lab

从 Python 零基础开始，逐步构建测试结果统计、测试日志分析和 AI 测试工具的学习型作品集。GitHub 仓库名称暂保留 `test1`，项目名称为 `ai-test-lab`。

当前实现：内存中的 PASS/FAIL 统计和命令行输出。尚未实现日志文件解析、模型调用或 GPU/NPU 测试；后续功能见 [路线图](docs/roadmap.md)。

## 5 分钟运行

准备 Python 3.10 或更高版本和 Git。在终端运行（不要输入 Python 交互窗口）：

```bash
git clone https://github.com/yuanyi-w/test1.git
cd test1
```

如果正在查看尚未合并的初始化 PR，请先切换到该 PR 的分支：

```bash
git switch feat/ai-test-lab-starter
```

Windows 推荐用 `py`，macOS/Linux 用 `python3`。以下示例使用 `python`；如果提示找不到命令，替换成对应命令即可。先检查版本：

```bash
python --version
python -m ai_test_lab
```

预期输出：

```text
ai-test-lab | Day 1
总数: 5
通过: 3
失败: 2
通过率: 60.0%
```

本阶段只使用 Python 标准库，无需 `pip install`、API key、网络或 GPU。请始终在含 README 的项目根目录运行命令，否则可能出现 `No module named ai_test_lab`。

运行自动检查：

```bash
python -m unittest discover -s tests -v
```

## 目录与阅读顺序

| 路径 | 用途 |
| --- | --- |
| `ai_test_lab/__main__.py` | 命令行入口，先看这里 |
| `ai_test_lab/summary.py` | 第一个可复用函数：统计 PASS/FAIL |
| `tests/test_summary.py` | 检查统计行为及输入边界 |
| `data/samples/` | 可公开的合成日志，下一阶段使用 |
| `data/local/` | 本地日志放这里，已被 Git 忽略 |
| `reports/` | 将来生成的报告，不提交生成内容 |
| `docs/stage-1.md` | 第一阶段目标、逐日练习、验收标准 |
| `docs/roadmap.md` | 后续扩展方案和日志格式约定 |
| `docs/original-README.md` | 初始化前 README 的完整副本 |

## 第一次学习任务

1. 打开 `ai_test_lab/__main__.py`，找出保存测试结果的列表。
2. 先预测新增一个 `FAIL` 后输出会如何变化，再修改并运行。
3. 阅读 [第一阶段学习指南](docs/stage-1.md)，逐步完成练习。

记录“我的预测 / 实际输出 / 为什么不同”，能解释代码比单纯跑通更重要。遇到报错时保留完整命令和报错文本。

## 迭代习惯

每次只改一个小功能：修改 → 运行 → 检查 → 提交。提交前用 `git diff` 查看改动，用 `git status` 检查新增文件。只提交合成或获准公开的数据；客户日志、身份信息和密钥不要提交，`.gitignore` 不能代替内容检查。

当前仓库保留原有 Git 历史，不包含就业结果承诺。作品集将以可运行代码、边界处理和真实学习记录逐步积累。
