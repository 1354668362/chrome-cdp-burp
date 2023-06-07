此为本人开发的cdp协议的burp插件版，目前为最新版
不是专业开发、插件开发为东拼西凑开发出来的，bug绝对有，但是大部分已经改了

# 使用方式：

## 前提准备：

谷歌浏览器
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --remote-allow-origins=*

![image-20230603191450951](http://weeesd22025ee9f4mniun.1winner.cn/8tTIE4Gipo/9yWbJd1Pi5/image-20230603191450951.png)

另外插件使用jython开发所以需要
python2 -m pip install pychrome
并且burp（最好使用和我一样的jython版本）
![image-20230603190826317](http://weeesd22025ee9f4mniun.1winner.cn/8tTIE4Gipo/9yWbJd1Pi5/image-20230603190826317.png)

## 使用方式一：

爆破功能

![image-20230603190922100](http://weeesd22025ee9f4mniun.1winner.cn/8tTIE4Gipo/9yWbJd1Pi5/image-20230603190922100.png)

输入要爆破的网站标题、加密功能即可

点击“获取网站爆破id值”需要在延迟时间内将目标下到断点处即可。

爆破成功之后的值需要选中右击chrome_cdp->获取解密值即可

### 例子

#### 第一步

找到加密代码

![image-20230605102359488](http://weeesd22025ee9f4mniun.1winner.cn/8tTIE4Gipo/9yWbJd1Pi5/image-20230605102359488.png)

例如：n.encrypt(t.password)

#### 第二步

将加密代码中要爆破的值替换为"%%"

强制替换"%%"不能修改为其他值

打开插件并将标题和加密代码写入

![image-20230605102629973](http://weeesd22025ee9f4mniun.1winner.cn/8tTIE4Gipo/9yWbJd1Pi5/image-20230605102629973.png)

#### 第三步

点击获取网站爆破id值之后在延迟时间内将网站断点下好直到显示网站爆破id值变为一串字符串

![image-20230605103014246](http://weeesd22025ee9f4mniun.1winner.cn/8tTIE4Gipo/9yWbJd1Pi5/image-20230605103014246.png)

#### 第四步

将要爆破的值添加之后加载插件即可爆破

![image-20230605102724443](http://weeesd22025ee9f4mniun.1winner.cn/8tTIE4Gipo/9yWbJd1Pi5/image-20230605102724443.png)

#### 第五步

成功之后选中爆破值右击点击chrome_cdp->获取解密值即可获取加密之前的值

![image-20230605103137603](http://weeesd22025ee9f4mniun.1winner.cn/8tTIE4Gipo/9yWbJd1Pi5/image-20230605103137603.png)

## 使用方式二：

网站传输过程中的加解密

![image-20230603191133512](http://weeesd22025ee9f4mniun.1winner.cn/8tTIE4Gipo/9yWbJd1Pi5/image-20230603191133512.png)

分别输入加解密代码、加解密标题即可”

获取id值“之后在第二个 tab中使用即可

![image-20230603191325224](http://weeesd22025ee9f4mniun.1winner.cn/8tTIE4Gipo/9yWbJd1Pi5/image-20230603191325224.png)

也可以在repeater右击发送到此窗口进行加解密功能（一开始也想将加解密之后的值直接弹窗但是感觉太丑了，就改成发送到ui中）

### 例子：

跟使用方式一的第一步第二步一样，找到对应的加解密代码即可使用这个就不放例子了

![image-20230605103439075](http://weeesd22025ee9f4mniun.1winner.cn/8tTIE4Gipo/9yWbJd1Pi5/image-20230605103439075.png)

开发了有一段时间，测试可能不完整，有bug请留言

最后一点，求大哥改成jar版

github地址：https://github.com/1354668362/chrome-cdp-burp

# 注意事项
## jython必须为2.7.1

不然无法正常使用

## 谷歌浏览器必须是用远程调试模式首次开启

"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --remote-allow-origins=*

不能先开一个正常的谷歌浏览器在开第二个远程调试模式的谷歌浏览器

且端口必须为9222

## 标题必须唯一：

演示：

假如有几个标题

![image-20230606135453725](http://weeesd22025ee9f4mniun.1winner.cn/8tTIE4Gipo/9yWbJd1Pi5/image-20230606135453725.png)

插件可以设置标题名为：

999、123

不能设置为456（因为456可以识别出来456.html、999456.html）888（因为888有两个窗口）
