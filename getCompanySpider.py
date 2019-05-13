from spiderLib import Main

#获取上市公司名称
def getCompanyName():
    # #定义爬取的url
    url= 'https://www.banban.cn/gupiao/list_sh.html'
    #定义爬取规则1
    get_rule = '<li>.*?<a href="/gupiao/\d.*?">([\u4e00-\u9fa5]+).*?</a>'
    #定义爬取规则2
    get_rule2= ''
    #定义pageid
    pageid= 0
    #调用Main类中的Main方法
    obj = Main.Main(url, get_rule, get_rule2, pageid)
    obj.main_get_company_name()

if __name__=='__main__':
    getCompanyName()