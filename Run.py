from spiderLib import Main
#定义爬取的url
url = 'https://www.thepaper.cn/load_index.jsp?nodeids=25434,25436,25433,25438,25435,25437,27234,25485,25432,37978,&topCids=,3420378,3419837,3418451&pageidx='
#定义爬取规则1
rule1 = '<img.*?src="(.*?)".*?>.*?<h2>.*?href="(.*?)".*?>(.*?)</a>.*?</h2>.*?<p>(.*?)</p>.*?<div class="pdtt_trbs">.*?<a.*?>(.*?)</a>.*?<span>(.*?)</span>'
#定义爬取规则2
rule2 = '<div class="news_about">.*?</p>.*?<p>.*?([\d-]+\s+[\d:]+).*?<span>'
#定义pageid
pageid = 1
#调用Main类中的Main方法
obj = Main.Main(url, rule1, rule2, pageid)
obj.main()
