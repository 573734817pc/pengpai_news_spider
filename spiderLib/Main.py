from spiderLib import ParseOnePage
import datetime
import logging

class Main(ParseOnePage.ParseOnePage):
    #定义main()
    def main(self):
        try:
            conn = self.db_conn()
            #爬取前五页的数据
            for i in [1, 2, 3, 4, 5]:
                url = self.url+str(i)
                html = self.get_one_page(url)
                cursor = conn.cursor()
                r = 0
                #匹配页面数据并循环插入数据库
                for item in self.parse_one_page(html,self.rule1):
                    category_info = self.do_category(item)
                    url_son = "https://www.thepaper.cn/"+item[1]
                    #获取准确时间，这里是由于爬取页面的特殊性造成的，不然不会有爬取主页以获取时间的
                    html_son = self.get_one_page(url_son)
                    public_time = self.parse_one_page(html_son,self.rule2)
                    cursor.execute('select * from tblGrabNews where title=%s', (item[2].strip().replace("&nbsp;", ""),))
                    values = cursor.fetchall()
                    #格式化爬取下来的时间，爬取的数据是字符串格式，我们需要将其转化为datetime格式
                    public_time_d = datetime.datetime.strptime(public_time[0]+":00",'%Y-%m-%d %H:%M:%S')  
                    if len(values) == 0:
                        #将数据存入数据库
                        cursor.execute("INSERT INTO tblGrabNews VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                       (item[2].strip().replace("&nbsp;", ""), item[3].strip(), item[0].strip(), public_time[0], '0', '0', item[4].strip(), 0, 0, public_time_d, self.pageid, category_info[0], category_info[1]))
                        conn.commit()
                        r = r + 1
                    print(r)
            conn.close()
            print("done!!!")
        except Exception as e:
            logging.exception(e)
    
