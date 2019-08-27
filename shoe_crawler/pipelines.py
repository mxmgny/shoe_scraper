import psycopg2


class ShoeCrawlerPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = psycopg2.connect(
            user='postgres',
            password='MaximiliaN98ujlf',
            host='127.0.0.1',
            port='5432',
            database='shoes_db'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS shoes""")

        self.curr.execute("""create table shoes(
                            Id serial PRIMARY KEY,
                            Manufacturer VARCHAR(50),
                            Title VARCHAR(50), 
                            Subtitle VARCHAR(50),
                            Current_price INT,
                            Full_price INT
                            )""")

    def process_item(self, item, spider):
        item['manufacturer'] = spider.name.title()
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into shoes 
                            (Manufacturer, Title, Subtitle, Current_price, Full_price) 
                            values (%s, %s, %s, %s, %s)""", (
                            item['manufacturer'],
                            item['title'][0],
                            item['subtitle'][0],
                            item['current_price'][0],
                            item['full_price'][0],
        )
                          )
        self.conn.commit()
