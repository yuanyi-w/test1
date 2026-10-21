"""纯统计逻辑：不读取文件，方便后续被日志分析程序复用。"""


def summarize_results(results):
    """接受 PASS/FAIL 字符串序列，返回统计字典。

    大小写和首尾空白会被归一化；未知状态或非字符串抛出 ValueError。
    空输入的通过率定义为 0.0，通过率范围为 0.0 到 1.0。
    """
    passed = 0
    failed = 0

    for result in results:
        if not isinstance(result, str):
            raise ValueError("测试结果必须是 PASS/FAIL 字符串")
        status = result.strip().upper()
        if status == "PASS":
            passed += 1
        elif status == "FAIL":
            failed += 1
        else:
            raise ValueError(f"未知测试结果: {result!r}，仅支持 PASS/FAIL")

    total = passed + failed
    pass_rate = passed / total if total else 0.0
    return {
        "total": total,
        "passed": passed,
        "failed": failed,
        "pass_rate": pass_rate,
    }
