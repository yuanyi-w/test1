"""在项目根目录运行：python -m ai_test_lab。"""

from ai_test_lab.summary import summarize_results


def main():
    # 列表保存多个字符串；下一阶段会从文件读取这些结果。
    results = ["PASS", "FAIL", "PASS", "PASS", "FAIL"]
    summary = summarize_results(results)

    print("ai-test-lab | Day 1")
    print(f"总数: {summary['total']}")
    print(f"通过: {summary['passed']}")
    print(f"失败: {summary['failed']}")
    print(f"通过率: {summary['pass_rate']:.1%}")


# 只有直接运行模块时才执行 main，导入时不打印。
if __name__ == "__main__":
    main()
