import numpy as np

def categorical_sample(probabilities, rng):
    """
    从给定的概率分布中进行采样
    :param probabilities: 概率分布，例如 [0.1, 0.4, 0.5]
    :param rng: 随机数生成器
    :return: 采样的结果，例如 0, 1, 2
    """
    return np.argmax(rng.multinomial(1, probabilities, 1))

# 示例用法
probabilities = [0.2, 0.3, 0.5]
np_random_generator = np.random.default_rng()  # 使用 NumPy 随机数生成器
sampled_value = categorical_sample(probabilities, np_random_generator)
print(np_random_generator)
print(sampled_value)
