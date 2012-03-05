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
    file_name = peewee.TextField(unique=True)
    file_title = peewee.TextField(null=True)
    comment = peewee.TextField(null=True)
    tags = peewee.TextField(null=True)
    passwd = peewee.TextField(null=True)
    uptime = peewee.TextField()
    shootday = peewee.TextField(null=True)

#insert等
class ImageLogic(object):
    def __init__(self):
        Image.create_table(True)

    def image_insert(self,fname,uptm,pswd=1234,ftitle=None,cmt=None,tg=None,shtday=None):
        sq = peewee.InsertQuery(Image,file_name=fname,file_title=ftitle,comment=cmt,
                                tags=tg,passwd=pswd,uptime=uptm,shootday=shtday)
        sq.execute()
        return True
