# VITS 纯中文微调

English Documentation Please Click [here](https://github.com/xieyuankun/VITS-chinese-finetune/blob/main/README%20-%20ENG.md)
##  该代码在[wac81/vits_chinese](https://github.com/wac81/vits_chinese)上进行了轻微修改
## 从标贝数据集进行推断

1. 您可以获取预训练模型，并将预训练模型G放在./logs/woman_csmsc/G*.pth中
2. 运行 `python infer.py`

## 重新训练一个基本模型以供微调
1. 将16000hz的biaobei数据集复制到./test/csmsc
2. 您可以通过修改./text/init.py中的chinese_mode = True来切换英语或中文。
3. 准备文本例如./test/woman_csmsc.txt.2.cleaned，该文本是提完音素后的biaobei10000句。
4. 运行`python3 train.py -c configs/woman_csmsc.json -m woman_csmsc`

## 微调
如果您需要预训练模型，请从 [百度云盘](https://pan.baidu.com/s/1xUz5TEi5aBiIhbh0gXTiSw?pwd=VITS) 进行下载，密码为VITS. 

我提供了某人的微调预训练模型，见下载链接XXXG_40000.pth。该模型继承标贝的60k保存点，使用mockingbird项目里的一个[issue](https://github.com/babysor/MockingBird/issues/721)进行微调40k得来，
由于只有66条所以质量一般。在实做中，微调1小时的效果往往就可以了，数据集质量和数量越多越佳。

需要注意的是如果是微调，G和D的检查点都需要，160k的G虽然相比100k在loss上有所下降，但个人认为从主观听感上差距不大。

微调步骤如下：

1. 请将G和D的检查点放在./logs/woman_csmsc下。100k和160k均可。
2. 准备你的微调数据集，可参考以前mockingbird众多方法准备，准备好文本类似./input.txt
3. 将input.txt通过txt2phoneme转化为output.txt样式的音素txt。
4. 音频文件放在./test/csmsc/，output.txt的内容复制到./test/woman_csmsc.txt.2.cleaned当中。
5. 运行 `python3 train.py -c configs/woman_csmsc.json -m woman_csmsc`即可开始微调。










