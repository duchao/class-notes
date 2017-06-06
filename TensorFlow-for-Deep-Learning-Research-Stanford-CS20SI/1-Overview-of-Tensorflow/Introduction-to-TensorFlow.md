##  Introduction to TensorFlow

### 1 Graphs and Sessions

**TensorFlow**将计算过程分为两个阶段：`计算的定义`与`计算的执行`，其中`计算的定义`对应于`Graphs`，`计算的执行`对应于`Sessions`，如图1所示。

<div  align="center">
<img src="imgs/0-1-tf-workflow-建图-执行.png" alt="Oops..." align="center" />
<p>图1 Data Flow Graphs</p>
</div>
<br>

图2为一个`Graphs`的示例，其中`Node`表示定义的操作，`Edge`表示数据流。

<div  align="center">
<img src="imgs/0-2-一个图示例-edge-node.png" alt="Oops..." align="center" />
<p>图2 Data Flow Graphs示例</p>
</div>
<br>

图3为一个多子图的`Graphs`示例，通过`tf.Session.run()`方法可以指定计算哪几个子图。

<div  align="center">
<img src="imgs/0-3-多子图示例-run函数参数.png" alt="Oops..." align="center" />
<p>图3 sub-Graphs</p>
</div>
<br>

### 2 Distributed Computation

<div  align="center">
<img src="imgs/0-4-分布式计算示例.png" alt="Oops..." align="center" />
<p>图4 分布式计算图示</p>
</div>
<br>

<div  align="center">
<img src="imgs/0-5-分布式计算代码示例.png" alt="Oops..." align="center" />
<p>图5 分布式计算代码示例</p>
</div>
<br>

上述的分布式计算过于naive，对于模型开发者来说，其不关心如何分配GPU来完成模型的计算，**TensorFlow**需要一个基于GPU的类`Spark`系统模块。


### 3 Why graphs？

<div  align="center">
<img src="imgs/0-6-为什么设计为图结构.png" alt="Oops..." align="center" />
<p>图6 Why graphs？</p>
</div>
<br>

总结如下：

- Save computation 避免不必要的计算
- Facilitates auto-differentiation 拆分成多个子图，加快自动微分
- Facilitate distributed computation 加快分布式（异构）运算
- 直观，使计算过程更容易理解
