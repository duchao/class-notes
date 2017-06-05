## 线性回归

---

> 机器学习**三步骤**
<div  align="center"><img src="imgs/1-framework-and-examples.png" alt="1.1" align="center" /></div>

---

### 0 问题定义
<div  align="center">
<center>
<img src="imgs/步骤0-1-regression解决的问题.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图1 现实中的回归问题</p>
</center>
</div>
<br>

由图1可知，现实中的很多应用场景可归纳为回归问题，其显著特点是**模型的预测结果为一个连续值**。本章节以CP值预测为例对回归问题涉及到的问题展开讨论，如图2所示。

<div  align="center">
<img src="imgs/步骤0-2问题定义.png" width = 65% height = 65% alt="Oops..." align="center"/>
<p> 图2 回归问题示例：CP值预测</p>
</div>
<br>

### 1 问题求解

**STEP 1 Model**
<div  align="center">
<img src="imgs/步骤1-定义模型-描述特征与真实值的关系.png" width = 65% height = 65% alt="Oops..." align="center"/>
<p> 图3 建立模型</p>
</div>
<br>
**STEP 2 Goodness of function**
<div  align="center">
<img src="imgs/步骤2-定义loss function.png" width = 65% height = 65% alt="Oops..." align="center"/>
<p> 图4 定义损失函数</p>
</div>
<br>
**STEP 3 Best function**
<div  align="center">
<img src="imgs/步骤3-1-将loss function作用于真实的数据-选择最优模型.png" width = 65% height = 65% alt="Oops..." align="center"/>
<p> 图5 定义优化算法（更新参数w和b）</p>
</div>
<br>

### 2 优化算法：梯度下降

利用梯度下降更新参数的流程分别如图6与图7所示：
<div  align="center">
<img src="imgs/步骤3-2-对w使用穷举法-再到优化算法-GD.png" width = 65% height = 65% alt="Oops..." align="center"/>
<p> 图6 仅对参数w进行更新</p>
</div>
<br>
<div  align="center">
<img src="imgs/步骤3-3-对参数列表使用GD.png" width = 65% height = 65% alt="Oops..." align="center"/>
<p> 图7 同时对参数w和b进行更新</p>
</div>
<br>

图8为参数w和b的更新过程可视化：

<div  align="center">
<img src="imgs/步骤3-4-2维参数迭代过程可视化.png" width = 65% height = 65% alt="Oops..." align="center"/>
<p> 图8 参数w和b更新过程</p>
</div>
<br>

梯度下降的三种特殊情形：`plateau point`，`saddle point`，`local minima`，如图9所示：

<div  align="center">
<img src="imgs/步骤3-4-GD的问题-解决办法是设计更好的loss function-凸函数.png" width = 65% height = 65% alt="Oops..." align="center"/>
<p> 图9 梯度下降的三种特殊情形</p>
</div>
<br>

在以上三种情形中，现在所介绍的梯度下降算法将无法得到最优的结果，第三章节将重新对梯度下降算法进行深入讨论。

### 3 模型评价

对模型的评价需要从两个方面考虑：**训练集阶段**与**测试集阶段**，如图10所示：

<div  align="center">
<img src="imgs/步骤4-模型评价.png" width = 95% height = 95% alt="Oops..." align="center"/>
<p> 图10 模型评价</p>
</div>
<br>

- 训练集阶段：用于检测模型的拟合（学习）效果
- 测试集阶段：用于评判模型的最终性能

若模型在训练集阶段检测的效果很好，而测试集阶段效果很差，则说明所训练的模型发生**过拟合（overfit）**，如图11所示：
<div  align="center">
<img src="imgs/步骤5-5-过拟合.png" width = 65% height = 65% alt="Oops..." align="center"/>
<p> 图11 过拟合</p>
</div>
<br>

### 4 模型优化

当模型在测试集阶段检测的效果较差时，显然需要对模型进行优化，优化的思路有如下两点：

- 在训练集阶段效果怎样？是否有提升的空间？
- 是否发生过拟合？

#### 4.1 提升训练集模型效果
在不更改模型的情况下，可通过一定的数据预处理与寻找更多的有效特征来提升模型的训练效果，俗称**特征工程**。
#### 4.2 避免过拟合
过拟合的原因是模型过于复杂，一种有效避免模型过拟合的办法是添加**正则项**。
