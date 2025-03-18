import sys
from sqlalchemy import Column, String, Float, Integer, Date, text
from flask import Flask, jsonify,json
from flask_sqlalchemy import SQLAlchemy
from db_config import mysql_config

user_name = mysql_config['user']
password = mysql_config['password']
host = mysql_config['host']
port = mysql_config['port']
database = mysql_config['database']

app = Flask(__name__)

# 配置SQLAlchemy连接MySQL数据库，根据实际情况修改
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user_name}:{password}@{host}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# 病案首页基本信息表
class Tmrdde(db.Model):
    __tablename__ = 'hospital_cmis_tmrdde'  # 表名

    sysid = Column(Integer, primary_key=True, autoincrement=True, comment="自增索引")
    fmrdid = Column(String(50), comment="病案号")
    # 住院
    fbihid = Column(String(50), comment="住院号")
    fbihda = Column(Integer, comment="住院天数")
    fbfop = Column(Integer, comment="术前住院天数")
    # 医生
    fzzys = Column(String(50), comment="主治医师")
    fzyys = Column(String(50), comment="住院医师")
    fzrys = Column(String(50), comment="主任医师")
    fzkys = Column(String(50), comment="质控医生")
    fzkhs = Column(String(50), comment="质控护士")
    # 科室 病房
    fioffi = Column(String(50), comment="入院科室编码")
    filoca = Column(String(50), comment="入院病房编码")
    ftoffi = Column(String(50), comment="转入科室编码")
    ftloca = Column(String(50), comment="转入病房编码")
    froffi = Column(String(50), comment="再转科室编码")
    frloca = Column(String(50), comment="再转病房编码")
    fooffi = Column(String(50), comment="出院科室编码")
    foloca = Column(String(50), comment="出院病房编码")
    # 时间
    fihdat = Column(Date, comment="入院时间")
    fodate = Column(Date, comment="出院时间")
    ftdate = Column(Date, comment="转入日期")
    fswdat = Column(Date, comment="死亡日期")
    # 患者
    fname = Column(String(50), comment="患者姓名")
    fsex = Column(String(50), comment="患者性别")
    fage = Column(Integer, comment="患者年龄")
    # 诊断
    fryzd = Column(String(50), comment="入院诊断")
    fmzzd = Column(String(50), comment="门（急）诊诊断")
    fsalcu = Column(Integer, comment="抢救次数")
    fscucu = Column(Integer, comment="抢救成功次数")
    # 其他
    fmzycy = Column(String(50), comment="门诊与出院符合")
    fryycy = Column(String(50), comment="入院与出院符合")
    fsqysh = Column(String(50), comment="术前与术后符合")

@app.route('/api/data', methods=['GET'])
def get_data():
    data = Tmrdde.query.limit(1).all() 
    result = [{"出院科室": item.fooffi} for item in data]  # 根据实际字段调整返回内容
    print(result)
    # 使用 json.dumps 并设置 ensure_ascii=False
    json_str = json.dumps(result, ensure_ascii=False)
    response = app.response_class(json_str, content_type='application/json; charset=utf-8')
    return response

if __name__ == '__main__':
    app.run(debug=True)