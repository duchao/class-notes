<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>

## Analysis of Algorithms

涉及到的主要内容如下：

- **introduction** ： 简介
- **observations** ： 运行算法，建立数据量与运行时间之间的数学模型
- **mathematical models** ： 在代码层面进行数学分析
- **order-of-growth classifications** ： 常见算法的增长级别分类
- **theory of algorithms** ： 算法理论
- **memory** ： 内存分析

### 1 简介

主要介绍为什么需要算法分析与优化以及算法优化的案例。

<div  align="center">
<img src="imgs/1-1-读取数据.png" alt="Oops..." align="center" />
<p>图1 为什么需要对算法进行分析</p>
</div>

由图1可知，算法分析主要围绕**`performance`**，也就是算法性能展开，其目的是为了避免因算法的性能问题导致系统瘫痪。

图2展示了FFT算法将离散傅里叶变换的计算步骤由<img src="https://latex.codecogs.com/gif.latex?N^2" title="N^2" />降低到<img src="https://latex.codecogs.com/gif.latex?NlogN" title="NlogN" />。


<div  align="center">
<img src="imgs/1-1-读取数据.png" alt="Oops..." align="center" />
<p>图2 算法分析应用</p>
</div>
