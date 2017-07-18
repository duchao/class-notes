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

