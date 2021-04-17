import os
import time
import random

# key: appName, vlaue: start adb command
dict_app = {
    ## 抖音极速版
    'douyin_lite': 
    {
        # 启动APP命令
        'bootstrap': 'adb shell am start -n com.ss.android.ugc.aweme.lite/com.ss.android.ugc.aweme.splash.SplashActivity',
        # 滑动间隔随机数最小值
        't_s': 5,
        # 滑动间隔随机数最大值
        't_e': 10
    },

    ## 快手极速版
    'kuaishou_lite': {
        'bootstrap': 'adb shell am start -n com.kuaishou.nebula/com.yxcorp.gifshow.HomeActivity',
        't_s': 5,
        't_e': 10
    }
}

# android sdk路径
android_sdk_dir = 'D:/Apps/platform-tools'

if __name__ == '__main__':
    ##切换到adb所在目录可以自己修改
    os.chdir(android_sdk_dir)
    print("已连接设备名称如下:")
    os.system('adb version')
    fun = os.system('adb devices')
    count = input('输入次数需要滑动的次数：')
    count = int(count)

    # 点亮屏幕
    fun = os.system('adb shell input keyevent 224')
    time.sleep(2)

    # 解锁
    fun = os.system('adb shell input swipe 300 1000 300 500')
    time.sleep(2)

    for app in dict_app.keys():
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "开始任务：", app)

        # 回到桌面
        fun = os.system('adb shell input keyevent 3')

        time.sleep(3)

        #　启动app
        fun=os.system(dict_app[app]['bootstrap'])

        # 完成次数
        finish_count = 0

        # 滑动休眠次数
        sleep_count = random.randint(30, 60)

        #　开始刷
        while finish_count < count:
            finish_count = finish_count + 1
            fun=os.system('adb shell input swipe 300 600 300 100')  ##坐标根据需要自己修改
            
            time.sleep(random.randint(dict_app[app]['t_s'], dict_app[app]['t_e']))

            if finish_count % sleep_count == 0:
                # 重置滑动休眠次数
                sleep_count = random.randint(30, 60)

                # 回到桌面
                fun = os.system('adb shell input keyevent 3')

                # 息屏
                fun = os.system('adb shell input keyevent 223')

                # 休眠3-4分钟
                time.sleep(random.randint(180, 240))

                # 亮屏
                fun = os.system('adb shell input keyevent 224')

                # 滑动解锁
                fun = os.system('adb shell input swipe 300 1000 300 500')

                #　启动app
                fun=os.system(dict_app[app]['bootstrap'])
            
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "任务[", app, "]完成", finish_count ,"次")

        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "任务[", app, "]完成")

    # 回到桌面
    fun = os.system('adb shell input keyevent 3')

    # 息屏
    fun = os.system('adb shell input keyevent 223')

    # 推出adb
    fun = os.system('adb kill-server') 

    exit()
   