"""蓄水池抽样：随机源、样本与合并：待实现的核心模块。"""


def lcg(seed):
    """线性同余随机数。"""
    raise NotImplementedError

def sample_indices(n, k, seed):
    """抽样下标。"""
    raise NotImplementedError

def reservoir(values, k, seed):
    """抽样值。"""
    raise NotImplementedError

def probability(k, n):
    """抽样概率。"""
    raise NotImplementedError

def merge_samples(a, b, k, seed):
    """合并样本。"""
    raise NotImplementedError
