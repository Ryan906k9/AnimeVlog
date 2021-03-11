# AnimeGAN一键生成日系动漫Vlog

## 引子
作为日本动漫的爱好者，特别是对宫崎骏、新海诚的童鞋们有福了。

本项目基于 PaddleHub 的动漫风格的转换模型，可以一键将视频转动漫哦！——>{日系风Vlog就在这}。

PaddleHub已将定制打造的街景动漫化模型[animegan_v2_hayao_99](https://www.paddlepaddle.org.cn/hubdetail?name=animegan_v2_hayao_99&en_category=GANs)、[animegan_v2_shinkai_53](https://www.paddlepaddle.org.cn/hubdetail?name=animegan_v2_shinkai_53&en_category=GANs)、[animegan_v2_paprika_98](https://www.paddlepaddle.org.cn/hubdetail?name=animegan_v2_paprika_98&en_category=GANs)等多个优质模型开源。可以自行切换转换风格！

## 效果展示图

<iframe style="width:80%;height: 450px;" src="//player.bilibili.com/player.html?aid=459563081&bvid=BV195411A7GQ&cid=308693816&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>

### 动漫化结果

![](./test_1.jpg)

![](./test_2.jpg)

## 使用方法

- 首先安装依赖：
- paddlepaddle
- paddlehub
- moviepy

然后把需要转换的视频放到指定位置，运行 main.py 即可！

# 致谢
* PaddleHub 官方项目集合：https://aistudio.baidu.com/aistudio/personalcenter/thirdview/79927
* PaddleHub AnimeGAN动漫化模型一键应用（含动漫化小程序体验）项目：https://aistudio.baidu.com/aistudio/projectdetail/1308514
