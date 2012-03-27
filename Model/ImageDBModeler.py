#coding: utf-8
import peewee

#データベースの指定
db = peewee.SqliteDatabase("img.db")

#BaseModelの定義
class BaseModel(peewee.Model):
    class Meta:
        database = db

#テーブルの定義
class Image(BaseModel):
    img_id = peewee.PrimaryKeyField()
    file_name = peewee.CharField(unique=True)
    file_title = peewee.CharField(null=True)
    comment = peewee.TextField(null=True)
    tags = peewee.TextField(null=True)
    passwd = peewee.CharField(null=True)
    uptime = peewee.CharField()
    shootday = peewee.CharField(null=True)

#insert等
class ImageLogic(object):
    def __init__(self):
        pass
        ##Image.create_table(True)

    def image_insert(self,fname,uptm,pswd="1234",ftitle=None,cmt=None,tg=None,shtday=None):
        sq = peewee.InsertQuery(Image,file_name=fname,file_title=ftitle,comment=cmt,
                                tags=tg,passwd=pswd,uptime=uptm,shootday=shtday)
        sq.execute()
        return True

    def get_id(self, offset=0, limit=8, order=True):
        sq = Image.Select()
        print sq


sq = Image.select()
res = [u.img_id for u in sq]
print res