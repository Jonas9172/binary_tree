结队编程：

某部门计划通过结队编程来进行项目开发，

已知该部门有 N 名员工，每个员工有独一无二的职级，每三个员工形成一个小组进行结队编程，结队分组规则如下：

    从部门中选出序号分别为 i、j、k 的3名员工，他们的职级分贝为 level[i]，level[j]，level[k]，

    结队小组满足 level[i] < level[j] < level[k] 或者 level[i] > level[j] > level[k]，

    其中 0 ≤ i < j < k < n。

请你按上述条件计算可能组合的小组数量。同一员工可以参加多个小组。
输入描述

第一行输入：员工总数 n

第二行输入：按序号依次排列的员工的职级 level，中间用空格隔开

限制：

    1 ≤ n ≤ 6000
    1 ≤ level[i] ≤ 10^5

输出描述

可能结队的小组数量
用例1
输入

4
1 2 3 4

输出

4
