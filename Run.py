from spiderLib import Main
from multiprocessing import Process
from multiprocessing import Pool
import os, time, random

#澎湃新闻
def pengpai():
    # #定义爬取的url
    url_pengpai = 'https://www.thepaper.cn/load_index.jsp?nodeids=25434,25436,25433,25438,25435,25437,27234,25485,25432,37978,&topCids=,3420378,3419837,3418451&pageidx='
    #定义爬取规则1
    rule1_pengpai = '<img.*?src="(.*?)".*?>.*?<h2>.*?href="(.*?)".*?>(.*?)</a>.*?</h2>.*?<p>(.*?)</p>.*?<div class="pdtt_trbs">.*?<a.*?>(.*?)</a>.*?<span>(.*?)</span>'
    #定义爬取规则2
    rule2_pengpai = '<div class="news_about">.*?</p>.*?<p>.*?([\d-]+\s+[\d:]+).*?<span>'
    #定义pageid
    pageid_pengpai = 1
    #调用Main类中的Main方法
    obj = Main.Main(url_pengpai, rule1_pengpai, rule2_pengpai, pageid_pengpai)
    obj.main_pengpai()

# 中国经济网
def zgjj():
    # #定义爬取的url
    print('Run task %s...' % (os.getpid(),))
    url = 'http://finance.ce.cn/rolling/index.shtml'
    # 定义爬取规则1
    rule1 = '<td height="28".*?href="(.*?)".*?\[(.*?)\].*?</td>'
    #定义爬取规则2
    rule2 = '<h1 id="articleTitle">(.*?)</h1>.*?<span id="articleSource">来源：(.*?)</span>.*?<div class="content" id="articleText">.*?><p.*?>(.*?)</p>'
    #定义pageid
    pageid = 2
    #调用Main类中的Main方法
    obj = Main.Main(url, rule1, rule2, pageid)
    obj.main_zgjj()

#中国科技网
def zgkj():
    #定义爬取的url
    print('Run task %s...' % (os.getpid(),))
    url = 'http://www.stdaily.com/cxzg80/kejizixun/kejizixun'
    # 定义爬取规则1
    rule1 = '<dl>.*?<h3>.*?>(.*?)</a>.*?<dd>.*?<p>(.*?)</p>.*?"sp_1">(.*?)</span>'
    #定义爬取规则2
    rule2 = ''
    #定义pageid
    pageid = 3
    #调用Main类中的Main方法
    obj = Main.Main(url, rule1, rule2, pageid)
    obj.main_zgkj()

#人民网
def rmw():
    #定义爬取的url
    url = 'http://finance.people.com.cn/GB/70846/index.html'
    # 定义爬取规则1
    rule1 = "<li>.*?<a href='(.*?)'.*?>.*?</li>"
    #定义爬取规则2
    rule2 = 'text_title">.*?<h1>(.*?)</h1>.*?"fl">.*?([\d]+).*?([\d]+).*?([\d]+).*?([\d]+).*?([\d]+).*?"_blank">(.*?)</a>.*?<div class="box_pic"></div>(.*?)<div class="box_pic"></div>'
    #定义pageid
    pageid = 4
    #调用Main类中的Main方法
    obj = Main.Main(url, rule1, rule2, pageid)
    obj.main_rmw()

#新浪财经7*24小时
def xlcj():
    # 定义爬取的url
    # print('Run task %s...' % (os.getpid(),))
    url = 'http://zhibo.sina.com.cn/api/zhibo/feed?callback=jQuery111208852375871132476_1557710175201&page_size=20&zhibo_id=152&page='
    # 定义爬取规则1
    rule1 = '.*?"rich_text":"(.*?)".*?"create_time":"(.*?)".*?'
    # 定义爬取规则2
    rule2 = ''
    # 定义pageid
    pageid = 5
    # 调用Main类中的Main方法
    obj = Main.Main(url, rule1, rule2, pageid)
    obj.main_xlcj()

#36氪
def ke():
    # 定义爬取的url
    url = 'https://36kr.com/newsflashes'
    # 定义爬取规则1
    rule1 = '"\/newsflashes\/([\d]{6})"'
    # 定义爬取规则2
    rule2 = '{"id":([\d]{6}),.*?"title":"(.*?)".*?"description":"(.*?)".*?"published_at":"(.*?)"'
    # 定义pageid
    pageid = 6
    # 调用Main类中的Main方法
    obj = Main.Main(url, rule1, rule2, pageid)
    obj.main_ke()


def test(name):
    print('Run task %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    rmw()
    xlcj()
    pengpai()
    ke()
    zgjj()
    # # q启动一个进程，执行澎湃网页面爬取程序
    # p_pengpai = Process(target=pengpai, args=('pengpai',))
    # p_pengpai.start()
    # p_pengpai.join()
    # print('Child pengpai process end.')
    #
    # # q启动一个进程，执行中国经济网页面爬取程序
    # p_zgjj = Process(target=zgjj, args=('zgjj',))
    # p_zgjj.start()
    # p_zgjj.join()
    # print('Child zgjj process end.')
    #
    # # q启动一个进程，执行中国科技网页面爬取程序
    # p_zgkj = Process(target=zgkj, args=('zgkj',))
    # p_zgkj.start()
    # p_zgkj.join()
    # print('Child zgkj process end.')
    #
    # #q启动一个进程，执行人名网页面爬取程序
    # p_rmw = Process(target=rmw, args=('rmw',))
    # p_rmw.start()
    # p_rmw.join()
    # print('Child rmw process end.')
    # p = Pool(4)
    # process_list = ['pengpai', 'zgjj', 'zgkj ', 'rmw']
    #
    # for i in range(4):
    #     #print(process_list[i])
    #     p.apply_async(rmw, args=(i,))
    # print('Waiting for all subprocesses done...')
    # p.close()
    # p.join()
    # print('All subprocesses done.')


