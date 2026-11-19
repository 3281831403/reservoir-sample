# 蓄水池抽样：随机源、样本与合并

抽样结果不可复现、流式样本偏向前段：随机源没有固定种子，替换概率没有按已见数量，样本没有排序，概率分母用样本数，合并后超过 k，空输入崩，批量抽样只成功一半。

## 目录结构

```
README.md
conftest.py
.gitignore
probabilistic/__init__.py
probabilistic/reservoir.py
tests/test_reservoir.py
```

## 当前状态

`probabilistic/reservoir.py` 中所有函数只保留签名与文档字符串，函数体统一
`raise NotImplementedError`。`tests/test_reservoir.py` 有 15 个参数化用例，
初始全部失败。

## 需要修复的 10 个问题

1. 随机源固定种子
2. 替换概率按已见数
3. 样本排序
4. 概率分母按总数
5. 合并截断到 k
6. 空输入兜底

## 验收

```bash
python -m pytest -q
```

初始应得到 `15 failed`，且没有 collection error。实现 `probabilistic/reservoir.py`
后 15 条用例应全部通过。
