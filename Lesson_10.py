# | Задание 44 |
# | --- |
# | В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести
#  его в one hot вид. Сможете ли вы это сделать без get_dummies?


# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI'lst})
# data.head() |

import pandas as pd
import random

# создаем DataFrame с 1 столбцом
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# переводим столбец в one hot вид
one_hot_data = pd.get_dummies(data, columns=['whoAmI'])
one_hot_data.head()

	whoAmI_human	whoAmI_robot
0	0	1
1	1	0
2	0	1
3	0	1
4	0	1