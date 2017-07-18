### logistic regression

---

> 机器学习**三步骤**
<div  align="center"><img src="../1-Regression/imgs/1-framework-and-examples.png" alt="1.1" align="center" /></div>

---

### 0 步骤一：define a set of functions

模型定义如图1所示，其可视化展示如图2所示：

<div  align="center">
<center>
<img src="imgs/0-1 logistic regression问题定义.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图1 logistic regression模型定义</p>
</center>
</div>
<br>


<div  align="center">
<center>
<img src="imgs/0-2 问题可视化展示.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图2 可视化展示</p>
</center>
</div>
<br>

### 1 步骤二：goodness of function

完成模型定以后，下面需要将模型具体化，即寻找最优参数（此模型中的参数为`w`和`b`）。
与生成模型的思路类似，先假设训练数据服从某种分布，然后对该分布进行参数估计，过程描述如图3所示：

<div  align="center">
<center>
<img src="imgs/1-1 假设空间.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图3 过程描述</p>
</center>
</div>
<br>

> 由图3可知，目标函数为`w^*, b^* = arg max L(w, b)`。

上述目标函数是多个函数连乘，在优化时不易计算（求一阶导麻烦），因此可通过取对数将其转化为连加，如图4所示：

<div  align="center">
<center>
<img src="imgs/1-2 似然-将连乘问题变为连加问题.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图4 问题转换</p>
</center>
</div>
<br>

> 目标函数转为`w^*, b^* = arg min - ln(L(w, b))`。
> 为什么需要取负数？ 因为`L(w, b)`是一个小于1的数，因此`ln(L(w, b))  < 0`，所以在表达式中添加`-`，同时对表达式求`min`。

对目标函数深入分析，如图5所示：

<div  align="center">
<center>
<img src="imgs/1-3 总结目标函数-cross entropy 用于评价两个分布的相似程度.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图5 目标函数深入分析</p>
</center>
</div>
<br>

将`ln(L(w, b))`展开后进行变换，可得`cross entropy`公式。`cross entropy`是一种用于衡量概率分布间相似度的量，在机器学习领域经常使用。  
在`logistics regression`模型中，将`cross entropy`作为其代价函数，如图6所示：

<div  align="center">
<center>
<img src="imgs/1-4 cross entropy minimize的对象.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图6 代价函数</p>
</center>
</div>
<br>

> `cross entropy`与`logloss`的区别？

### 2 步骤三：find the best function

分别对代价函数进行求一阶导（计算梯度），如图7和图8所示：

<div  align="center">
<center>
<img src="imgs/2-1 求导1.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图7 代价函数求导-1</p>
</center>
</div>
<br>

<div  align="center">
<center>
<img src="imgs/2-2 求导2.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图8 代价函数求导-2</p>
</center>
</div>
<br>

最后将两部分的求导结果进行合并，并按照梯度下降法进行参数的迭代进化，如图9所示：

<div  align="center">
<center>
<img src="imgs/2-3 合并-梯度更新.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图9 代价函数求导合并</p>
</center>
</div>
<br>

最后对`logistic regression`与`linear regression`进行比较，如图10所示：

<div  align="center">
<center>
<img src="imgs/2-4 logistic regression与linear regression的区别.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图10 模型间的比较</p>
</center>
</div>
<br>

可知，两种模型的建模及迭代方法相同，主要不同点在于假设空间定义以及代价函数。下面，将解释为什么`logistic regression`的代价函数为什么不能是`square loss`。

### 3 代价函数比较

假设`logistic regression`模型的代价函数为`square loss`，则模型的迭代步骤如图11、图12所示：

<div  align="center">
<center>
<img src="imgs/3-1 为什么不能使用square loss作为损失函数1.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图11 使用square loss-1</p>
</center>
</div>
<br>

<div  align="center">
<center>
<img src="imgs/3-2 为什么不能使用square loss作为损失函数2.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图12 使用square loss-2</p>
</center>
</div>
<br>

可知，梯度值恒为0，即无法进行参数迭代，其可视化结果如图13所示：

<div  align="center">
<center>
<img src="imgs/3-3 cross entropy与square loss的区别.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图13 使用square loss-2</p>
</center>
</div>
<br>

### Discriminative v.s. Generative

图14总结了`Discriminative`与`Generative`两种模型间的参数估计过程：

<div  align="center">
<center>
<img src="imgs/4-1 Discriminative v.s. Generative的计算过程区别.png" width = 65% height = 65% alt="Oops..." align="center" />
<p>图14 使`Discriminative`与`Generative`模型比较</p>
</center>
</div>
<br>
