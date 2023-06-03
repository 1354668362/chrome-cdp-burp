# coding=utf-8
# -*- coding: utf-8 -*- 
from burp import IBurpExtender
from burp import ITab
from burp import IHttpListener
from burp import IMessageEditorController
from burp import IProxyListener
from burp import IContextMenuFactory
from burp import IHttpRequestResponse
from burp import IContextMenuInvocation
from burp import IMessageEditorTabFactory
from burp import IMessageEditorTab
from burp import IParameter
from javax.swing import JSplitPane;
from javax.swing import JLabel;
from javax.swing import JButton;
from javax.swing import JPanel;
from javax.swing import JOptionPane;
from javax.swing import JTextField;
from javax.swing import JMenuItem;
from javax.swing import JMenu;
from javax.swing import JScrollPane;
from javax.swing import JTabbedPane;
from javax.swing import JTextArea;
from javax.swing.table import AbstractTableModel;
from javax.swing import BoxLayout;
from java.awt import BorderLayout
from java.awt import FlowLayout
from burp import IBurpExtender
from burp import IIntruderPayloadGeneratorFactory
from burp import IIntruderPayloadProcessor
from java.awt import GridBagLayout, GridBagConstraints
#from java.lang import System
import sys,pychrome,time,re,os,urllib,io,re
from threading import Thread
#设置utf-8不然会报错
reload(sys)
sys.setdefaultencoding("utf8")
class BurpExtender(IBurpExtender, ITab, IMessageEditorTabFactory,IMessageEditorTab,IParameter,IHttpListener,IContextMenuInvocation, IMessageEditorController, AbstractTableModel, IIntruderPayloadGeneratorFactory, IIntruderPayloadProcessor, IProxyListener, IContextMenuFactory, IHttpRequestResponse):

    def	registerExtenderCallbacks(self, callbacks):
        # keep a reference to our callbacks object
        self._callbacks = callbacks
        #缓存文件
        self.url_tmp = ''
        self.cc = os.popen("whoami").read()
        #print self.cc.split("\\")[1]
        self.file_name = "C:\Users\\"+self.cc.split("\\")[1].replace("\n","")+"\AppData\Local\Chrome_rdp\log.log"
        if not os.path.exists(self.file_name):
            os.mkdir(self.file_name.replace("\\log.log",""))
            print "不存在"+self.file_name
            io.open(self.file_name,'a+',encoding="utf-8")
        else:
            io.open(self.file_name,'a+',encoding="utf-8").close()
        #prnit "成功清空"+self.file_name+"文件内容"
        #初始化
        self.callFrameId_str = ''
        
        print '通过谷歌浏览器cdp协议越过加密逻辑\n使用时需要先将chrome打开远程调试模式\nchrome.exe --remote-debugging-port=9222 --remote-allow-origins=*\nversion:1.0\t                         2023-05-25 22:40\n                                                by 1winner\n bug大全版'
        self._helpers = callbacks.getHelpers()
        # 设置约束
        self.constraints = GridBagConstraints()
        self.constraints.anchor = GridBagConstraints.WEST  # 左对齐
        self.constraints.insets.set(5, 5, 5, 5)  # 设置边距

        # 添加组件到面板中
        self.constraints.gridx = 0
        self.constraints.gridy = 0
        self.layout = GridBagLayout()
        #panel.setLayout(self.layout)
        #这是上下滑动页
        self._splitpane = JSplitPane(JSplitPane.VERTICAL_SPLIT)
        self.tabs2 = JPanel()
        #垂直布局
        self.tabs2.setLayout(BoxLayout(self.tabs2, BoxLayout.Y_AXIS))
        #尝试title
        self.tabs3 = JPanel()
        self.tabs3.setLayout(self.layout)
        self.callFrameId_str_list_tmp = JLabel(u'\u7206\u7834\u529f\u80fd\u6807\u9898\uff1a')
        self.Website_title1 = JTextField('',20)
        self.tabs3.add(self.callFrameId_str_list_tmp,self.constraints)
        self.constraints.gridx = 1
        self.tabs3.add(self.Website_title1,self.constraints)
        #self.tabs2.add(self.tabs3)
        
        #这是加密代码
        self.encryption_code_tmp = JLabel(u'\u7206\u7834\u529f\u80fd\u4ee3\u7801\uff1a')
        self.encryption_code = JTextField('',20)
        self.constraints.gridx = 0
        self.constraints.gridy = 1
        self.tabs3.add(self.encryption_code_tmp,self.constraints)
        self.constraints.gridx = 1
        self.constraints.gridy = 1
        self.tabs3.add(self.encryption_code,self.constraints)
        self.tabs2.add(self.tabs3)
        #这是time
        self.Interval_time_tmp = JLabel(u'\u5ef6\u8fdf\u65f6\u95f4\uff1a')
        self.Interval_time = JTextField('10',20)
        self.constraints.gridx = 0
        self.constraints.gridy = 2
        self.tabs3.add(self.Interval_time_tmp,self.constraints)
        self.constraints.gridx = 1
        self.constraints.gridy = 2
        self.tabs3.add(self.Interval_time,self.constraints)
        #这是str,这是按钮1
        self.callFrameId__tmp = JLabel(u'\u7f51\u7ad9\u7206\u7834\u0049\u0064\u503c\uff1a')
        self.Button = JButton(u'\u83b7\u53d6\u7f51\u7ad9\u7206\u7834\u0049\u0064\u503c')
        self.Button.addActionListener(self.getbuuton)
        self.constraints.gridx = 0
        self.constraints.gridy = 3
        self.tabs3.add(self.callFrameId__tmp,self.constraints)
        self.constraints.gridx = 1
        self.constraints.gridy = 3
        self.tabs3.add(self.Button,self.constraints)
        #self.tabs2.add(self.tabs3)
        #这是清空缓存文件
        self.Button3 = JButton(u'\u6e05\u7a7a\u6587\u4ef6\u7f13\u5b58')
        self.Button3.addActionListener(self.clear_file)
        self.constraints.gridx = 3
        self.constraints.gridy = 0
        self.tabs3.add(self.Button3,self.constraints)
        #这是加密body
        self.encrypt_title_Label = JLabel(u'\u7f51\u7ad9\u52a0\u5bc6\u6807\u9898\uff1a')
        self.encrypt_title_TextField = JTextField('',20)
        self.constraints.gridx = 2
        self.constraints.gridy = 7
        self.tabs3.add(self.encrypt_title_Label,self.constraints)
        self.constraints.gridx = 3
        self.tabs3.add(self.encrypt_title_TextField,self.constraints)
        #这是加密body的参数
        self.encrypt_title_code_Label = JLabel(u'\u7f51\u7ad9\u52a0\u5bc6\u4ee3\u7801\uff1a')
        self.encrypt_title_code_TextField = JTextField('',20)
        self.constraints.gridx = 2
        self.constraints.gridy = 8
        self.tabs3.add(self.encrypt_title_code_Label,self.constraints)
        self.constraints.gridx = 3
        self.tabs3.add(self.encrypt_title_code_TextField,self.constraints)
        #这是加密body的按钮
        self.encrypt_callFrameId_Body = JLabel(u'\u52a0\u5bc6\u0049\u0064\u503c\uff1a')
        self.Button_encrypt_Body = JButton(u'\u83b7\u53d6\u52a0\u5bc6\u0049\u0064\u503c')
        self.Button_encrypt_Body.addActionListener(self.encrypt_Selected_tmp)
        self.constraints.gridx = 2
        self.constraints.gridy = 9
        self.tabs3.add(self.encrypt_callFrameId_Body,self.constraints)
        self.constraints.gridx = 3
        self.tabs3.add(self.Button_encrypt_Body,self.constraints)
        #这是解密title
        self.decrypt_tmp = JLabel(u'\u7f51\u7ad9\u89e3\u5bc6\u6807\u9898\uff1a')
        self.decrypt_title1 = JTextField('',20)
        self.constraints.gridx = 0
        self.constraints.gridy = 7
        self.tabs3.add(self.decrypt_tmp,self.constraints)
        self.constraints.gridx = 1
        self.tabs3.add(self.decrypt_title1,self.constraints)
        #这是解密代码
        self.decrypt_code_tmp = JLabel(u'\u7f51\u7ad9\u89e3\u5bc6\u4ee3\u7801\uff1a')
        self.decrypt_code = JTextField('',20)
        self.constraints.gridx = 0
        self.constraints.gridy = 8
        self.tabs3.add(self.decrypt_code_tmp,self.constraints)
        self.constraints.gridx = 1
        self.tabs3.add(self.decrypt_code,self.constraints)
        #这是解密按钮1
        self.decrypt_callFrameId__tmp = JLabel(u'\u89e3\u5bc6\u0049\u0064\u503c\uff1a')
        self.Button_decrypt = JButton(u'\u83b7\u53d6\u89e3\u5bc6\u0049\u0064\u503c')
        self.Button_decrypt.addActionListener(self.getbuuton_decrypt)
        self.constraints.gridx = 0
        self.constraints.gridy = 9
        self.tabs3.add(self.decrypt_callFrameId__tmp,self.constraints)
        self.constraints.gridx = 1
        self.tabs3.add(self.Button_decrypt,self.constraints)
        
        self.tabs109 = JPanel()
        #这是要解密的值
        self.tabs55 = JPanel()
        self.tabs55.setLayout(self.layout)
        self.decrypt_tmp_Response_text = JTextArea(2,30)
        #这是解密之后的值
        self.decrypt_title1_Response_text = JTextArea(2,30)
        self.scrollPane_decrypt_tmp_Response_text = JScrollPane(self.decrypt_tmp_Response_text)
        self.scrollPane_decrypt_title1_Response_text = JScrollPane(self.decrypt_title1_Response_text)
        #这是解密按钮
        self.Button_decrypt_Response_text = JButton('decrypt')
        self.Button_decrypt_Response_text.addActionListener(self.decrypt_Request)
        self.constraints.gridx = 1
        self.constraints.gridy = 1
        self.tabs55.add(self.scrollPane_decrypt_tmp_Response_text,self.constraints)
        self.constraints.gridy = 2
        self.tabs55.add(self.scrollPane_decrypt_title1_Response_text,self.constraints)
        self.constraints.gridy = 3
        self.tabs55.add(self.Button_decrypt_Response_text,self.constraints)
        #这是要加密的值
        self.encrypt_tmp_Response_text = JTextArea(2,30)
        self.encrypt_title1_Response_text = JTextArea(2,30)
        self.scrollPane_encrypt_tmp_Response_text = JScrollPane(self.encrypt_tmp_Response_text)
        self.scrollPane_encrypt_title1_Response_text = JScrollPane(self.encrypt_title1_Response_text)
        #这是加密的值
        self.Button_encrypt_Response_text = JButton('encrypt')
        self.Button_encrypt_Response_text.addActionListener(self.getbuuton_encrypt_Body)
        self.constraints.gridx = 3
        self.constraints.gridy = 1
        self.tabs55.add(self.scrollPane_encrypt_tmp_Response_text,self.constraints)
        self.constraints.gridy = 2
        self.tabs55.add(self.scrollPane_encrypt_title1_Response_text,self.constraints)
        self.constraints.gridy = 3
        self.tabs55.add(self.Button_encrypt_Response_text,self.constraints)
        #设置显示
        
        self.tabs109.add(self.tabs55)
        self.abbedPane = JTabbedPane()
        
        self.abbedPane.addTab(u'\u8bbe\u7f6e',self.tabs2)
        self.tabs2.add(self.tabs3)
        self.abbedPane.addTab(u'\u7f51\u7ad9\u52a0\u89e3\u5bc6',self.tabs109)
        #以上组件全部放入上面窗口
        self._splitpane.setLeftComponent(self.abbedPane)
        
        
        
        self.log_ui = JTextArea(10,60)
        #设置为不能编辑
        #以self.log_ui生成滚动框
        self.scrollPane = JScrollPane(self.log_ui)
        self.log_ui.append(u'\u751f\u6210\u7f13\u5b58\u6587\u4ef6\uff1a'+self.file_name+'\n');
        self.tabs10 = JPanel()
        #设置铺满
        self.tabs10.setLayout(BorderLayout())
        #添加滚动窗口
        self.tabs10.add(self.scrollPane)
        self.tabs10.setVisible(True)
        self._splitpane.setRightComponent(self.tabs10)
        callbacks.customizeUiComponent(self._splitpane)
        
        callbacks.addSuiteTab(self)
        self._helpers = callbacks.getHelpers()
        
        # 这是插件加载名称
        callbacks.setExtensionName("Chrome-cdp")
        callbacks.registerIntruderPayloadGeneratorFactory(self)
        callbacks.registerIntruderPayloadProcessor(self)
        callbacks.registerProxyListener(self)
        callbacks.registerContextMenuFactory(self)
        self.PROXYLISTENER_CHARSET = None
        self.MULTIPART_FORM_DATA   = True
    #这里右击之后的数据
    def createMenuItems(self,invocation):
        self.conent = invocation
        print invocation
        MenuItems = [] 
        MenuItem = JMenu("chrome_cdp")
        chrome_cdp_tmp    = JMenuItem(u"\u83b7\u53d6\u89e3\u5bc6\u503c",    actionPerformed = lambda event:self.cgarset_chrome_cdp(event,invocation))
        #解密
        decrypt_Selected_Request_MenuItem    = JMenuItem(u"\u0052\u0065\u0071\u0075\u0065\u0073\u0074\u0020\u89e3\u5bc6",    actionPerformed = lambda event:self.decrypt_Selected_Request_def(event,invocation))
        #加密
        encrypt_Selected_Request_MenuItem    = JMenuItem(u"\u0052\u0065\u0071\u0075\u0065\u0073\u0074\u0020\u52a0\u5bc6",    actionPerformed = lambda event:self.encrypt_Selected_Request_def(event,invocation))
        #解密
        decrypt_Selected_Response_MenuItem    = JMenuItem(u"\u0052\u0065\u0073\u0070\u006f\u006e\u0073\u0065\u0020\u89e3\u5bc6",    actionPerformed = lambda event:self.decrypt_Selected_Response_def(event,invocation))
        #加密
        encrypt_Selected_Response_MenuItem    = JMenuItem(u"\u0052\u0065\u0073\u0070\u006f\u006e\u0073\u0065\u0020\u52a0\u5bc6",    actionPerformed = lambda event:self.encrypt_Selected_Response_def(event,invocation))
        MenuItem.add(chrome_cdp_tmp)
        MenuItem.add(decrypt_Selected_Request_MenuItem)
        MenuItem.add(encrypt_Selected_Request_MenuItem)
        MenuItem.add(decrypt_Selected_Response_MenuItem)
        MenuItem.add(encrypt_Selected_Response_MenuItem)
        MenuItems.append(MenuItem)
        return MenuItems
    #整个body的加密函数
    def getbuuton_encrypt_Body(self,event):
        #请求头加body
        
        tmp_cc = self.encrypt_tmp_Response_text.getText()
        tmp_cc = tmp_cc.replace('"','\\"')
        #tmp_cc = urllib.unquote(tmp_cc)
        self.tmp1_encrypt_Body = self.encrypt_Body_list[0].replace("u'","'")
        self.tmp2_encrypt_Body = self.encrypt_Body_list[1].replace("u'","'")
        #
        encrypt_string_Selected_Request = self.tab_Selected_encrypt.Debugger.evaluateOnCallFrame(callFrameId=self.callFrameId_str_Selected_repeater,expression=self.tmp1_encrypt_Body+str(tmp_cc)+self.tmp2_encrypt_Body)['result']['value']
        #invocation.getSelectedMessages()[0].setRequest(self.replace_zhi(RequestString_encrypt_Body,currentPayload_Selected_Request_tmp,encrypt_string_Selected_Request))
        self.encrypt_title1_Response_text.setText(encrypt_string_Selected_Request)
    #整个body解密函数
    def decrypt_Request(self,event):
        tmp_cc_tmp = self.decrypt_tmp_Response_text.getText()
        self.tmp1_Body = self.dncrypt_list[0].replace("u'","'")
        self.tmp2_Body = self.dncrypt_list[1].replace("u'","'")
        try:
            dncrypt_string_Body_1 = self.tab_body__Response.Debugger.evaluateOnCallFrame(callFrameId=self.callFrameId_str_decrypt,expression=self.tmp1_Body+str(tmp_cc_tmp)+self.tmp2_Body)['result']['value']
            self.decrypt_title1_Response_text.setText(dncrypt_string_Body_1)
        except  Exception as e:
            print 'decrypt_Request'
            print e
    #右击解密
    def decrypt_Selected_Request_def(self,event,invocation):
        #选中的值
        tmp_decrypt = invocation.getSelectedMessages()[0].getRequest()[invocation.getSelectionBounds()[0]:invocation.getSelectionBounds()[1]].tostring()
        #tmp_cc_tmp = tmp_decrypt.replace('"','\"')
        tmp_cc_tmp_1 = urllib.unquote(tmp_decrypt)
        self.tmp1_Body_1 = self.dncrypt_list[0].replace("u'","'")
        self.tmp2_Body_2 = self.dncrypt_list[1].replace("u'","'")
        try:
            dncrypt_string_Body = self.tab_body__Response.Debugger.evaluateOnCallFrame(callFrameId=self.callFrameId_str_decrypt,expression=self.tmp1_Body_1+str(tmp_cc_tmp_1)+self.tmp2_Body_2)['result']['value']
            self.decrypt_title1_Response_text.setText(dncrypt_string_Body)
        except  Exception as e:
            print 'decrypt_Selected_Request_def'
            print e
    #右击加密
    def encrypt_Selected_Request_def(self,event,invocation):
        #选中的值
        tmp_encrypt = invocation.getSelectedMessages()[0].getRequest()[invocation.getSelectionBounds()[0]:invocation.getSelectionBounds()[1]].tostring()
        #tmp_cc_1 = urllib.unquote(tmp_encrypt)
        tmp_cc_1 = tmp_encrypt.replace('"','\\"')
        self.tmp1_Body_1 = self.encrypt_Body_list[0].replace("u'","'")
        self.tmp2_Body_2 = self.encrypt_Body_list[1].replace("u'","'")
        try:
            encrypt_string_Body = self.tab_body__Response.Debugger.evaluateOnCallFrame(callFrameId=self.callFrameId_str_decrypt,expression=self.tmp1_Body_1+str(tmp_cc_1)+self.tmp2_Body_2)['result']['value']
            self.encrypt_title1_Response_text.setText(encrypt_string_Body)
        except  Exception as e:
            print 'encrypt_Selected_Request_def'
            print e
    #右击解密
    def decrypt_Selected_Response_def(self,event,invocation):
        #选中的值
        tmp_decrypt_Response = invocation.getSelectedMessages()[0].getResponse()[invocation.getSelectionBounds()[0]:invocation.getSelectionBounds()[1]].tostring()
        print tmp_decrypt_Response
        #tmp_cc_tmp = tmp_decrypt.replace('"','\"')
        tmp_cc_tmp_1_Response = urllib.unquote(tmp_decrypt_Response)
        self.tmp1_Body_1_Response = self.dncrypt_list[0].replace("u'","'")
        self.tmp2_Body_2_Response = self.dncrypt_list[1].replace("u'","'")
        try:
            dncrypt_string_Body_Response = self.tab_body__Response.Debugger.evaluateOnCallFrame(callFrameId=self.callFrameId_str_decrypt,expression=self.tmp1_Body_1_Response+str(tmp_cc_tmp_1_Response)+self.tmp2_Body_2_Response)['result']['value']
            self.decrypt_title1_Response_text.setText(dncrypt_string_Body_Response)
        except  Exception as e:
            print 'decrypt_Selected_Response_def'
            print e
    #右击加密
    def encrypt_Selected_Response_def(self,event,invocation):
        #选中的值
        tmp_encrypt_Response = invocation.getSelectedMessages()[0].getResponse()[invocation.getSelectionBounds()[0]:invocation.getSelectionBounds()[1]].tostring()
        #tmp_cc_1 = urllib.unquote(tmp_encrypt)
        tmp_cc_1_Response = tmp_encrypt_Response.replace('"','\\"')
        self.tmp1_Body_11_Response = self.encrypt_Body_list[0].replace("u'","'")
        self.tmp2_Body_21_Response = self.encrypt_Body_list[1].replace("u'","'")
        try:
            encrypt_string_Body_Response = self.tab_body__Response.Debugger.evaluateOnCallFrame(callFrameId=self.callFrameId_str_decrypt,expression=self.tmp1_Body_11_Response+str(tmp_cc_1_Response)+self.tmp2_Body_22_Response)['result']['value']
            self.encrypt_title1_Response_text.setText(encrypt_string_Body_Response)
        except  Exception as e:
            print 'encrypt_Selected_Response_def'
            print e
    #gui选中加密之后的值解密
    def cgarset_chrome_cdp(self,event,invocation):
        #这是爆破模块解密
        tmp1 = self.conent.getSelectedMessages()[0].getRequest()[self.conent.getSelectionBounds()[0]:self.conent.getSelectionBounds()[1]].tostring()
        try:
            self.pp = []
            tmp1 = urllib.unquote(tmp1)
            with io.open(self.file_name,'r',encoding="utf-8") as f:
                self.tmp_files = f.readlines()
            for self.i in self.tmp_files:
                #这里写入的数据[u"'11111'", u"'045e6b9c8474ec3e750fe0a91bc36d5793770723bcc579cb5bbde4315c4b9e3fef302fb1f5ca696f399eaeb456058e82956be521e30f98d7567896dc53cf8200976fa6a4cd80555cf83221db74dbf780362a109ae949d90900ac4e564ca857f0137e71f99448'\n"]
                self.i = self.i.replace("u'","'")
                if str(tmp1) in self.i:
                    self.pp = self.i.split(":")
                    #这里是带'未加密数据'，需要用replace将'去掉
                    self.log_ui.append(u"\u89e3\u5bc6\u503c\u4e3a\uff1a"+self.pp[0].replace("'","")+"\n")
                    ta = JTextArea()
                    ta.setText(self.pp[0].replace("'",""));
                    ta.setWrapStyleWord(True);
                    ta.setLineWrap(True);
                    ta.setCaretPosition(0);
                    ta.setEditable(False);
                    cc = JScrollPane(ta)
                    JOptionPane.showMessageDialog(None, cc, "get chrome_cdp Text", JOptionPane.INFORMATION_MESSAGE)
                    break
            if self.pp ==[]:
                #self.tmp_code.setText("Not found !")
                self.log_ui.append(u"\u5728\u7f13\u5b58\u6587\u4ef6\u4e2d\u627e\u4e0d\u5230\u60a8\u9700\u8981\u7684\u660e\u6587\n")
        except  Exception as e:
            print 'unencrypted_def'
            print e
    #这是cdp协议返回数据处理用来获取callFrameId_str
    def request_will_be_sent(self,**kwargs):
        return_kwargs = kwargs.get('callFrames')
        callFrameId_str_list_Id = re.findall("u'callFrameId': u'(.*?)'",str(return_kwargs))
        self.callFrameId_str = callFrameId_str_list_Id[0]
        #设置ui展示
        self.callFrameId__tmp.setText(self.callFrameId_str)
        self.log_ui.append(u"\u7206\u7834\u529f\u80fd\u0049\u0064\u503c\uff1a"+self.callFrameId_str+u"\u002c\u8bf7\u4e0b\u4e00\u6b65\n")
        print self.callFrameId_str
     #这是cdp协议返回数据处理用来获取callFrameId_Selected_str
    def request_will_be_sent_Selected_repeater(self,**kwargs):
        return_kwargs = kwargs.get('callFrames')
        callFrameId_str_list_Selected_repeater = re.findall("u'callFrameId': u'(.*?)'",str(return_kwargs))
        self.callFrameId_str_Selected_repeater = callFrameId_str_list_Selected_repeater[0]
        #设置ui展示
        self.encrypt_callFrameId_Body.setText(self.callFrameId_str_Selected_repeater)
        self.log_ui.append(u"\u7f51\u7ad9\u52a0\u5bc6\u0049\u0064\u503c\uff1a"+self.callFrameId_str_Selected_repeater+u"\u002c\u8bf7\u4e0b\u4e00\u6b65\n")
        print self.callFrameId_str_Selected_repeater
     #这是cdp协议返回数据处理用来获取callFrameId_str
    def request_will_be_sent_decrypt(self,**kwargs):
        return_kwargs = kwargs.get('callFrames')
        callFrameId_str_list_decrypt = re.findall("u'callFrameId': u'(.*?)'",str(return_kwargs))
        self.callFrameId_str_decrypt = callFrameId_str_list_decrypt[0]
        #设置ui展示
        self.decrypt_callFrameId__tmp.setText(self.callFrameId_str_decrypt)
        self.log_ui.append(u"\u7f51\u7ad9\u89e3\u5bc6\u0049\u0064\u503c\uff1a"+self.callFrameId_str_decrypt+u"\u002c\u8bf7\u4e0b\u4e00\u6b65\n")
        print self.callFrameId_str_decrypt
    #清空缓存文件
    def clear_file(self,TextArea1):
        try:
            with io.open(self.file_name,'w',encoding="utf-8") as f:
                self.log_ui.append(u"\u5df2\u6210\u529f\u6e05\u9664\u7f13\u5b58\u6587\u4ef6\n")
        except  Exception as e:
            print 'clear_file'
            print e
    #这是在爆破的同时写入文件，为了不阻塞所以创建新的线程
    def Unencrypted_And_Encrypted_Write_Files_Thread(self,arg1,arg2):
        self.worker_thread = Thread(target=self.Unencrypted_And_Encrypted_Write_Files,kwargs={'arg1':arg1,'arg2':arg2})
        self.worker_thread.start() 
    #Unencrypted_And_Encrypted_Write_Files_Thread的函数
    def Unencrypted_And_Encrypted_Write_Files(self,arg1,arg2):
        try:
            with io.open(self.file_name,'a+',encoding="utf-8") as f:
                #未加密数据和加密数据
                f.write("'"+arg1+"':'"+arg2+"'\n")
        except  Exception as e:
            print 'Unencrypted_And_Encrypted_Write_Files'
            print e
    
    #查找callFrameId_str_intruder,因为使用sleep所以创建一个新的线程，不阻塞主进程
    def getbuuton(self,TextArea1):
        self.worker_thread = Thread(target=self.getbuuton1)
        self.worker_thread.start()
    #这是getbuuton用来获取查找callFrameId_str_intruder的函数
    def getbuuton1(self):
        self.urls ="http://127.0.0.1:9222"
        self.chrome = pychrome.Browser(url=self.urls)
        self.tab_intruder = None
        for self._tab in self.chrome.list_tab():
            try:
                if self.Website_title1.getText() in self._tab._kwargs['title']:
                    self.tab_intruder = self._tab
                    self.url_tmp = self.urls+r'/devtools/inspector.html?ws=127.0.0.1:9222/devtools/page/'+str(self._tab).replace(r"<Tab [","").replace(r"]>","")
                    print '调试地址：'
                    print self.url_tmp
                    print '调试网站：'+self._tab._kwargs['title']
                    self.log_ui.append(u"\u5f53\u524d\u8c03\u8bd5\u6807\u9898\uff1a"+self._tab._kwargs['title']+"\n")
                    self.tab_intruder.start()
                    break
                if not self.tab_intruder:
                    print '未发现可见TAB.'
            except  Exception as e:
                print(e)
        self.tab_intruder.Debugger.enable()
        print '进行第二步,当前延迟时间'+self.Interval_time.getText()
        self.tab_intruder.set_listener("Debugger.paused", self.request_will_be_sent)
        self.encryption_str = self.encryption_code.getText()
        self.encrypt_list = self.encryption_str.split("%%")
        time.sleep(int(self.Interval_time.getText()))
    #查找callFrameId_str_intruder,因为使用sleep所以创建一个新的线程，不阻塞主进程
    def encrypt_Selected_tmp(self,TextArea1):
        self.worker_thread = Thread(target=self.encrypt_Selected_pmt)
        self.worker_thread.start()
    #这是getbuuton用来获取查找callFrameId_str_Selected_repeater的函数
    def encrypt_Selected_pmt(self):
        self.urls ="http://127.0.0.1:9222"
        self.chrome = pychrome.Browser(url=self.urls)
        #self.log_ui.append("Debug title:\n")
        self.tab_Selected_encrypt = None
        for self._tab in self.chrome.list_tab():
            try:
                if self.encrypt_title_TextField.getText() in self._tab._kwargs['title']:
                    self.tab_Selected_encrypt = self._tab
                    self.url_tmp = self.urls+r'/devtools/inspector.html?ws=127.0.0.1:9222/devtools/page/'+str(self._tab).replace(r"<Tab [","").replace(r"]>","")
                    print self.url_tmp
                    print '调试网站：'+self._tab._kwargs['title']
                    self.log_ui.append(u"\u5f53\u524d\u8c03\u8bd5\u6807\u9898\uff1a"+self._tab._kwargs['title']+"\n")
                    self.tab_Selected_encrypt.start()
                    break
                if not self.tab_Selected_encrypt:
                    print '未发现可见TAB.'
            except  Exception as e:
                print(e)
        self.tab_Selected_encrypt.Debugger.enable()
        print '进行第二步,当前延迟时间'+self.Interval_time.getText()
        self.tab_Selected_encrypt.set_listener("Debugger.paused", self.request_will_be_sent_Selected_repeater)
        self.encryption_str_tmp = self.encrypt_title_code_TextField.getText()
        self.encrypt_Body_list = self.encryption_str_tmp.split("%%")
        time.sleep(int(self.Interval_time.getText()))
    def getbuuton_decrypt(self,event):
        self.worker_thread = Thread(target=self.getbuuton2)
        self.worker_thread.start()
    #这是getbuuton_decrypt用来获取解密整个body的函数
    def getbuuton2(self):
        self.urls ="http://127.0.0.1:9222"
        self.chrome = pychrome.Browser(url=self.urls)
        #self.log_ui.append("Debug title:\n")
        self.tab_body__Response = None
        for self._tab in self.chrome.list_tab():
            try:
                if self.decrypt_title1.getText() in self._tab._kwargs['title']:
                    self.tab_body__Response = self._tab
                    self.url_tmp = self.urls+r'/devtools/inspector.html?ws=127.0.0.1:9222/devtools/page/'+str(self._tab).replace(r"<Tab [","").replace(r"]>","")
                    print '调试地址：'
                    print self.url_tmp
                    print '调试网站：'+self._tab._kwargs['title']
                    self.log_ui.append(u"\u5f53\u524d\u8c03\u8bd5\u6807\u9898\uff1a"+self._tab._kwargs['title']+"\n")
                    self.tab_body__Response.start()
                    break
                if not self.tab_body__Response:
                    print '未发现可见TAB.'
            except  Exception as e:
                print(e)
        self.tab_body__Response.Debugger.enable()
        print '进行第二步,当前延迟时间'+self.Interval_time.getText()
        self.tab_body__Response.set_listener("Debugger.paused", self.request_will_be_sent_decrypt)
        
        self.decrypt_code_tmp = self.decrypt_code.getText()
        self.dncrypt_list = self.decrypt_code_tmp.split("%%")
        time.sleep(int(self.Interval_time.getText()))
    
    #这里是ui名称
    def getTabCaption(self):
        return "Chrome-cdp"
    
    def getUiComponent(self):
        return self._splitpane
    #
    # implement IHttpListener
    #
    def getGeneratorName(self):
        return "My custom payloads"

    #这里是爆破加密得名称
    def getProcessorName(self):
        return "Serialized input wrapper"
    #这个函数返回的就是加密后的值
    def processPayload(self, currentPayload, originalPayload, baseValue):
        #在加密数据之前统一使用url编码一次，currentPayload默认是两个数组，但是不知道为什么使用""+就会变为字符串
        #currentPayload = urllib.quote(""+currentPayload)
        encrypt_string_inturder =''
        currentPayload_inturder = ""+currentPayload
        #以%%分割
        self.tmp1_inturder = self.encrypt_list[0].replace("u'","'")
        self.tmp2_inturder = self.encrypt_list[1].replace("u'","'")
        try:
            encrypt_string_inturder = self.tab_intruder.Debugger.evaluateOnCallFrame(callFrameId=self.callFrameId_str,expression=self.tmp1_inturder+str(currentPayload_inturder)+self.tmp2_inturder)['result']['value']
            print encrypt_string_inturder
            self.Unencrypted_And_Encrypted_Write_Files_Thread(currentPayload,encrypt_string_inturder)
        except  Exception as e:
            print 'js加密出错请检测'
            print e
        return encrypt_string_inturder
