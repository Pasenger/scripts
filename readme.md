# 我的脚本

## 1. python

### 1.1 shushipin.py


用于刷抖音极速版和快手极速版。

V1.0 Release:

- 自动亮屏
- 自动解锁屏幕（不能设置锁屏密码）
- 根据配置随机滑动屏幕间隔
- 刷30-60次后会退出APP，锁屏休眠3-4分钟（随机）


安装使用方法：
- 下载android sdk
    [下载参考](https://developer.android.google.cn/studio/command-line/adb?hl=zh_cn)
- 解压android sdk后，将路径添加到环境变量中
- 新建环境变量，变量名：ANDROID_PLATFORM_TOOLS， 变量值：android sdk路径
- 开启手机开发者模式，USB调试开关
- 执行脚本，输入滑动次数即可。


## 其他说明

### 1. 通过Wi-Fi连接adb
- 用USB链接手机
- 设置目标设备以监听端口5555上的TCP/IP连接
  ```
  adb tcpip 5555
  ```
- 拔掉USB线
- 查看Android设备的IP地址
- 通过IP连接到设备，命令行执行
  ```
  adb connect 设备IP
  ```
- 确认主机已连接到目标设备
  ```
    adb devices
  ```