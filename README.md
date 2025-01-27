# AI-for-playing-efootball-based-on-the-DQN-model
First, I would like to thank Lanmo Digital and Yu Shangyexiaoxiao for their open-source contributions on GitHub. They have also published their training videos on Bilibili, which you can check out if you are interested. I am training an AI to play efootball, but my computer's performance is not great, and the model is quite basic, so the training results are poor. You can see the training results here: https://www.bilibili.com/video/BV1gY4y127jB/?share_source=copy_web&vd_source=cbecf36a4e43383e3427704d32860061. 
I worked on this project in 2023, and only recently did I come across the folder. At the time, I thought I had already open-sourced it. In fact, the source code is not much different from that of the two experts mentioned earlier. The main credit still goes to them.
Since efootball is a mobile game, you need to use scrcpy to connect your computer and phone. I used scrcpy-1.16. Alternatively, you can install a mobile emulator on your computer to run efootball and then train the AI.

首先要感谢蓝魔digital以及遇上雨也笑笑在github的开源，他们在bilibili上也公布了他们的训练视频，有兴趣的可以去看看。
我训练的是踢efootball的AI，但是我的电脑性能不行，模型也一般，所以训练出来的效果很差，训练效果在这里可以看：https://www.bilibili.com/video/BV1gY4y127jB/?share_source=copy_web&vd_source=cbecf36a4e43383e3427704d32860061
这个项目我在2023年就做了，最近才翻到文件夹，当时以为自己已经开源了。其实源代码和前面两位大佬的差别不大，主要还是大佬们的功劳。
因为efootball是手机游戏，所以需要用scrcpy连接电脑和手机，我用的是scrcpy-1.16。也可以在电脑上安装一个手机模拟器运行efootball然后训练AI。
【代码介绍】：该模型是基于DQN模型搭建神经网络进行训练的。Detect keyboard.py主要是用win32api获取键盘输入，Control keyboard.py模拟键盘输出，让AI操作游戏。Grabscreen.py获取屏幕图像，让AI看得见屏幕。Brain.py是神经元的搭建，卷积层和池化层获得state，然后AI执行action，接着得到DQN评分。这个文件也包含Loss曲线，模型训练和保存。全连接层，步长设置，学习率设置等都在这个文件。Others.py主要是读取比分，一开始是通过读取进球数来评分，后面为了加快训练速度，改成了人为评分，AI把球带过半场就加1分，射门加1分，进球加1分，出界减2分等。sekiro.ipynb负责前期布置，设置AI读取的屏幕范围大小，测试前后左右移动，踢球按键是否正确。
![image](https://github.com/user-attachments/assets/974d1cb1-8f6d-4606-af67-d21a10ce7c6b)

