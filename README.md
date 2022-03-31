# Python版植物大战僵尸
  一个简单的植物大战僵尸游戏。
  
  `仅供个人学习和非商业用途。如果这个游戏侵犯了版权，请告诉我。`
  
* 已有的植物： 向日葵, 豌豆射手, 坚果墙, 寒冰豌豆射手, 樱桃炸弹, 三向豌豆射手, 食人花, 喷射蘑菇, 土豆地雷, 杂草地刺, 胆小菇, 南瓜, 愤怒辣椒, 阳光菇, 寒冰菇, 魅惑菇。
* 已有的僵尸: 普通僵尸, 旗帜僵尸, 路障僵尸, 铁桶僵尸, 读报僵尸。
* 使用 JSON 格式的文件存储进度数据 (例如僵尸出现的位置和时间, 背景信息)。
* 支持选择植物卡片。
* 支持白昼模式,夜晚模式,传送带模式和坚果保龄球模式。

# 系统要求
* Python >= 3.7 
* Python-Pygame >= 1.9

# 怎样开始游戏
```shell
python main.py
```

# 怎样玩
* 使用鼠标收集阳光,收集植物卡片和植物的种子。
* 你可以通过更改 source/constants.py 中的 START＿LEVEL＿NUM 的数值来更改起始关卡：
  * 1 和 2：白昼模式
  * 3: 夜晚模式
  * 4: 传送带模式
  * 5: 坚果保龄球模式

# 截屏
![截屏1](https://raw.githubusercontent.com/marblexu/PythonPlantsVsZombies/master/demo/demo1.jpg)
![截屏2](https://raw.githubusercontent.com/marblexu/PythonPlantsVsZombies/master/demo/demo2.jpg)
![截屏3](https://raw.githubusercontent.com/marblexu/PythonPlantsVsZombies/master/demo/demo3.jpg)
