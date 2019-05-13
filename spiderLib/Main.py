from spiderLib import ParseOnePage
import datetime
import logging

class Main(ParseOnePage.ParseOnePage):
    #定义main_pengpai()函数，这是爬取澎湃新闻的方法
    def main_pengpai(self):
        try:
            conn = self.db_conn()
            cursor = conn.cursor()
            #爬取前五页的数据
            for i in [1, 2, 3, 4, 5]:
                url = self.url+str(i)
                html = self.get_one_page(url)
                #匹配页面数据并循环插入数据库
                for item in self.parse_one_page(html, self.rule1):
                    category_info = self.do_category(item, 2, 3)
                    url_son = "https://www.thepaper.cn/"+item[1]
                    #获取准确时间，这里是由于爬取页面的特殊性造成的，不然不会有爬取主页以获取时间的
                    html_son = self.get_one_page(url_son)
                    public_time = self.parse_one_page(html_son,self.rule2)
                    cursor.execute('select * from tblGrabNews where title=%s', (item[2].strip().replace("&nbsp;", ""),))
                    values = cursor.fetchall()
                    #格式化爬取下来的时间，爬取的数据是字符串格式，我们需要将其转化为datetime格式
                    public_time_d = datetime.datetime.strptime(public_time[0]+":00",'%Y-%m-%d %H:%M:%S')  
                    if len(values) == 0:
                        if len(item[3].strip()) > 30:
                            #将数据存入数据库
                            cursor.execute("INSERT INTO tblGrabNews VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                           (item[2].strip().replace("&nbsp;", ""), item[3].strip(), item[0].strip(), public_time[0], '0', '0', item[4].strip(), 0, 0, public_time_d, self.pageid, category_info[0], category_info[1]))
                            conn.commit()
            conn.close()
            print("done!!!")
        except Exception as e:
            logging.exception(e)

    #定义main_zgjj（）函数,这是爬取中国经济网页面的方法
    def main_zgjj(self):
        try:
            conn = self.db_conn()
            cursor = conn.cursor()
            html = self.get_one_page(self.url)
            for item in self.parse_one_page(html, self.rule1):
                if item[0][0:2] == "./":
                    url_son = item[0].replace("./", "http://finance.ce.cn/rolling/")
                    html_son = self.get_one_page(url_son)
                    for article_info in self.parse_one_page(html_son, self.rule2):
                        category_info = self.do_category(article_info, 0, 2)
                        cursor.execute('select * from tblGrabNews where title=%s',
                                       (article_info[0].strip().replace("&nbsp;", ""),))
                        values = cursor.fetchall()
                        # 格式化爬取下来的时间，爬取的数据是字符串格式，我们需要将其转化为datetime格式
                        public_time_d = datetime.datetime.strptime(item[1].strip().replace("/", "-")+":00", '%Y-%m-%d %H:%M:%S')
                        if len(values) == 0:
                            if len(article_info[2].strip()) > 50:
                                # 将数据存入数据库
                                cursor.execute("INSERT INTO tblGrabNews VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                                   (article_info[0].strip().replace("&nbsp;", ""), article_info[2].strip(), '0', item[1].strip(), article_info[1].strip(), '0', '0', 0, 0, public_time_d, self.pageid, category_info[0], category_info[1]))
                                conn.commit()
                                # print('111111')

                elif item[0][0:2] == "..":
                    url_son = item[0].replace("../", "http://finance.ce.cn/")
                    html_son = self.get_one_page(url_son)
                    for article_info in self.parse_one_page(html_son, self.rule2):
                        category_info = self.do_category(article_info, 0, 2)
                        cursor.execute('select * from tblGrabNews where title=%s',
                                       (article_info[0].strip().replace("&nbsp;", ""),))
                        values = cursor.fetchall()
                        # 格式化爬取下来的时间，爬取的数据是字符串格式，我们需要将其转化为datetime格式
                        public_time_d = datetime.datetime.strptime(item[1].strip().replace("/", "-")+":00", '%Y-%m-%d %H:%M:%S')
                        if len(values) == 0:
                            if len(article_info[2].strip()) > 50:
                                # 将数据存入数据库
                                cursor.execute("INSERT INTO tblGrabNews VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                                   (article_info[0].strip().replace("&nbsp;", ""), article_info[2].strip(), '0', item[1].strip(), article_info[1].strip(), '0', '0', 0, 0, public_time_d, self.pageid, category_info[0], category_info[1]))
                                conn.commit()
                                # print('111111')
            conn.close()
            print("done!!!")
        except Exception as e:
            logging.exception(e)
    #中国科技网
    def main_zgkj(self):
        try:
            conn = self.db_conn()
            cursor = conn.cursor()
            for i in ["", "_2", "_3", "_4", "_5"]:
                html = self.get_one_page(self.url+i+".shtml")
                for item in self.parse_one_page(html, self.rule1):
                    # print(item[0].strip())
                    category_info = self.do_category(item, 0, 1)
                    cursor.execute('select * from tblGrabNews where title=%s', (item[0].strip().replace("&nbsp;", ""),))
                    values = cursor.fetchall()
                    # 格式化爬取下来的时间，爬取的数据是字符串格式，我们需要将其转化为datetime格式
                    public_time_d = datetime.datetime.strptime(item[2].strip() + ":00", '%Y-%m-%d %H:%M:%S')
                    if len(values) == 0:
                        if len(item[1].strip()) > 30:
                            # 将数据存入数据库
                            cursor.execute("INSERT INTO tblGrabNews VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                           (item[0].strip().replace("&nbsp;", ""), item[1].strip(), '0',
                                            item[2].strip(), '0', '0', '0', 0, 0, public_time_d, self.pageid,
                                            category_info[0], category_info[1]))
                            conn.commit()
            conn.close()
            print("done!!!")
        except Exception as e:
            logging.exception(e)
    #人名网
    def main_rmw(self):
        try:
            conn = self.db_conn()
            cursor = conn.cursor()
            html = self.get_one_page(self.url)
            ts_rule = '<div class="ej_left">(.*?)<div class="p1_right ej_right">'
            html_real_list = self.parse_one_page(html, ts_rule)
            html_real = html_real_list[0]
            for item in self.parse_one_page(html_real, self.rule1):
                html_son = self.get_one_page("http://finance.people.com.cn"+item)
                for item_son in self.parse_one_page(html_son, self.rule2):
                    category_info = self.do_category(item_son, 0, 7)
                    cursor.execute('select * from tblGrabNews where title=%s', (item_son[0].strip().replace("&nbsp;", ""),))
                    values = cursor.fetchall()
                    # 格式化爬取下来的时间，爬取的数据是字符串格式，我们需要将其转化为datetime格式
                    time_str = item_son[1]+"-"+item_son[2]+"-"+item_son[3]+" "+item_son[4]+":"+item_son[5]+":00"
                    public_time_d = datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
                    if len(values) == 0:
                        if len(item_son[7].strip()) > 30:
                            # 将数据存入数据库
                            cursor.execute("INSERT INTO tblGrabNews VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                           (item_son[0].strip().replace("&nbsp;", ""), item_son[7].strip(), '0',
                                            time_str, '0', '0', '0', 0, 0, public_time_d, self.pageid,
                                            category_info[0], category_info[1]))
                            conn.commit()
            conn.close()
            print("done!!!")
        except Exception as e:
            logging.exception(e)


    #新浪财经
    def main_xlcj(self):
        try:
            conn = self.db_conn()
            cursor = conn.cursor()
            #获取本页面数据在数据库中的最新一条数据的时间，用于判断爬取下来的数据有没有存入数据库，做增量插入
            newest_time = self.get_newest_time_by_pageid()
            for i in ["1", "2", "3", "4", "5"]:
                url_real = self.url+i
                html = self.get_one_page(url_real)
                for item in self.parse_one_page(html, self.rule1):
                    item = list(item)
                    item[0] = item[0].encode('utf-8').decode("unicode_escape")
                    category_info = self.do_category(item, 0, 0)
                    cursor.execute('select * from tblGrabNews where title=%s',
                                   (item[0].strip().replace("&nbsp;", ""),))
                    values = cursor.fetchall()
                    public_time_d = datetime.datetime.strptime(item[1].strip(), '%Y-%m-%d %H:%M:%S')
                    if public_time_d <= newest_time:
                        return
                    if len(values) == 0:
                        if len(item[0].strip()) > 20:
                            # 将数据存入数据库
                            cursor.execute("INSERT INTO tblGrabNews VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                                   ("0", item[0].strip(), '0',
                                                    item[1], '0', '0', '0', 0, 0, public_time_d, self.pageid,
                                                    category_info[0], category_info[1]))
                            conn.commit()
                conn.close()
        except Exception as e:
            logging.exception(e)
    #获取上市公司名称
    def main_get_company_name(self):
        html = self.get_one_page(self.url)
        name_list = self.parse_one_page(html, self.rule1)
        str_name_list = ",".join(name_list)
        print(str_name_list)
        f = open('./companyName/companyName.txt', 'w')
        f.write(str_name_list)
        f.close()
