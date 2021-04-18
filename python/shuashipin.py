import os
import time
import random

# key: appName, vlaue: start adb command
dict_app = {
    ## 火山极速版
    'huoshan_lite': {
        # 启动APP命令
        'bootstrap': 'adb shell am start -n com.ss.android.ugc.livelite/com.ss.android.ugc.live.main.MainActivity',
        # 停止命令
        'stop_cmd': 'adb shell am force-stop com.ss.android.ugc.livelite',
        # 滑动间隔随机数最小值
        't_s': 5,
        # 滑动间隔随机数最大值
        't_e': 10
    },
   
    ## 快手极速版
    'kuaishou_lite': {
        'bootstrap': 'adb shell am start -n com.kuaishou.nebula/com.yxcorp.gifshow.HomeActivity',
        # 停止命令
        'stop_cmd': 'adb shell am force-stop com.kuaishou.nebula',
        't_s': 5,
        't_e': 10
    },
 
    ## 抖音极速版
    'douyin_lite': {
        # 启动APP命令
        'bootstrap': 'adb shell am start -n com.ss.android.ugc.aweme.lite/com.ss.android.ugc.aweme.splash.SplashActivity',
        # 停止命令
        'stop_cmd': 'adb shell am force-stop com.ss.android.ugc.aweme.lite',
        # 滑动间隔随机数最小值
        't_s': 5,
        # 滑动间隔随机数最大值
        't_e': 10
    }

    # 'xiaoshuo_fanqie': {
    #     'package': 'com.dragon.read',
    #     'bootstrap': 'adb shell am start -n com.dragon.read/.reader.ReaderActivity',
    #     'stop_cmd': 'adb shell am force-stop com.dragon.read',
    #     # 滑动间隔随机数最小值
    #     't_s': 4,
    #     # 滑动间隔随机数最大值
    #     't_e': 7
    # }
}

# android sdk路径
# android_sdk_dir = 'D:/Apps/platform-tools'
android_sdk_dir = os.getenv('ANDROID_PLATFORM_TOOLS')


# 运行APP
def run(app, run_time_seconds):
    '''
        app: appName
        run_time_seconds: 运行时常
    '''
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), '开始任务：', app, ', 运行时长：', run_time_seconds, '秒')

    # 回到桌面
    fun = os.system('adb shell input keyevent 3')

    time.sleep(2)

    #　启动app
    fun = os.system(dict_app[app]['bootstrap'])

    # 完成次数
    finish_count = 0

    # 已完成时间
    finish_run_seconds = 0

    # 滑动多少次后返回桌面
    sleep_number = random.randint(30, 60)
    sleep_count = 0

    #　开始刷
    while finish_run_seconds < run_time_seconds:
        finish_count += 1
        sleep_count += 1

        ##坐标根据需要自己修改
        fun = os.system('adb shell input swipe 300 600 300 100') 
        
        # 滑动后随机休眠一段时间
        sleep_second = random.randint(dict_app[app]['t_s'], dict_app[app]['t_e'])
        time.sleep(sleep_second)
        
        finish_run_seconds += sleep_second

        sleep_number = sleep_number + 1

        # 滑动到一定次数后休眠一段时间
        if sleep_count == sleep_number:
            # 重置滑动休眠次数
            sleep_number = random.randint(30, 60)
            sleep_count = 0
            
            sleep_seconds = random.randint(20, 40)
            run_seconds = run_seconds + sleep_seconds

            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), '任务[', app, ']已完成', finish_count ,'次, 休息 ', sleep_seconds, ' 秒...')

            # 回到桌面
            fun = os.system('adb shell input keyevent 3')

            # 息屏
            fun = os.system('adb shell input keyevent 223')

            # 休眠
            time.sleep(sleep_seconds)

            # 亮屏
            fun = os.system('adb shell input keyevent 224')

            # 滑动解锁
            fun = os.system('adb shell input swipe 300 1000 300 500')

            #　启动app
            fun=os.system(dict_app[app]['bootstrap'])
        
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), '任务[', app, ']完成', finish_count ,'次')

    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), '任务[', app, ']完成')   

    # 回到桌面
    fun = os.system('adb shell input keyevent 3')

    # 停止
    fun = os.system(dict_app[app]['stop_cmd'])

    # 息屏
    fun = os.system('adb shell input keyevent 223') 


if __name__ == '__main__':
    ##切换到adb所在目录可以自己修改
    os.chdir(android_sdk_dir)

    print('已连接设备名称如下:')
    os.system('adb version')
    fun = os.system('adb devices')
    # count = input('输入次数需要滑动的次数：')
    # count = int(count)

    # 点亮屏幕
    fun = os.system('adb shell input keyevent 224')
    time.sleep(2)

    # 解锁
    fun = os.system('adb shell input swipe 300 1000 300 500')
    time.sleep(2)

    while True:
        localtime = time.localtime(time.time())
        cur_hour = localtime.tm_hour
        # 凌晨1点到6点不执行
        if cur_hour > 1 and cur_hour < 6:
            print('休息时间: ', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
            time.sleep(600)
        else:
            for app in dict_app.keys():
                run_time_seconds = random.randint(600, 1200)
                run(app, run_time_seconds)

    # # 回到桌面
    # fun = os.system('adb shell input keyevent 3')

    # # 息屏
    # fun = os.system('adb shell input keyevent 223')

    # # 推出adb
    # fun = os.system('adb kill-server') 

    # exit()
   