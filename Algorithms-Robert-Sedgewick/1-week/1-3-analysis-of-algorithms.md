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


### 2 观察

**观察**方法主要分为两步：通过足够的实验记录数据并结规律；然后利用规律对未知输入大小时算法的性能进行预测，分别如图3与图4所示。

<div  align="center">
<img src="imgs/1-1-读取数据.png" alt="Oops..." align="center" />
<p>图3 规律总结</p>
</div>

<div  align="center">
<img src="imgs/1-1-读取数据.png" alt="Oops..." align="center" />
<p>图4 预测</p>
</div>

**观察**法直观且易理解，图5展示了**观察**法的优缺点。

<div  align="center">
<img src="imgs/1-1-读取数据.png" alt="Oops..." align="center" />
<p>图5 优缺点分析</p>
</div>

### 3 数学模型

Knuth指出一个程序的运行总时间主要与两点有关：

- 执行每条语句的耗时
- 执行每条语句的频率

前者取决于计算机、Java编辑器和操作系统，后者取决于程序本身算法和输入，如图6所示。

<div  align="center">
<img src="imgs/1-1-读取数据.png" alt="Oops..." align="center" />
<p>图6 运行时长的数学模型</p>
</div>

图7以1-sum为例进行分析：

<div  align="center">
<img src="imgs/1-1-读取数据.png" alt="Oops..." align="center" />
<p>图7 1-sum运行时长分析</p>
</div>

<div  align="center">
<img src="imgs/1-1-读取数据.png" alt="Oops..." align="center" />
<p>图8 简化时长的数学模型</p>
</div>


### 4 增长数量级

为算法建立时长数学模型的意义在于提供了一种可靠的办法比较不同算法间的性能差异。事实上，时长数学模型使得这个比较过程更为简单，因为常见的算法时长模型都可以归纳为图9所示的几个类别中。

<div  align="center">
<img src="imgs/1-1-读取数据.png" alt="Oops..." align="center" />
<p>图8 简化时长的数学模型</p>
</div>

图9展示了增长数量级类别与实例的对应关系：

<div  align="center">
<img src="imgs/1-1-读取数据.png" alt="Oops..." align="center" />
<p>图9 类别与实例的对应关系</p>
</div>

下面以二分查找为例，对其增长数量级进行分析，如图10与图11所示：

<div  align="center">
<img src="imgs/1-1-读取数据.png" alt="Oops..." align="center" />
<p>图10 二分查找代码实现</p>
</div>

<div  align="center">
<img src="imgs/1-1-读取数据.png" alt="Oops..." align="center" />
<p>图11 二分查找算法性能分析</p>
</div>

