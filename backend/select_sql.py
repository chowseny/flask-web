import datetime
import pandas as pd
from sqlalchemy import column, create_engine, Column, Integer, String, func,or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import BigInteger, Column, DECIMAL, DateTime, Float, ForeignKey, Index, Integer, Table, text
from sqlalchemy.dialects.mysql import BIT, DATETIME, MEDIUMTEXT, TEXT, TINYINT, VARCHAR
from topo_models import *
from db_config import mysql_config

user_name = mysql_config['user']
password = mysql_config['password']
host = mysql_config['host']
port = mysql_config['port']
database = mysql_config['database']

# 创建数据库引擎
engine = create_engine(f'mysql+pymysql://{user_name}:{password}@{host}:{port}/{database}')

# 创建会话
Session = sessionmaker(bind=engine)
session = Session()

def query_data(model, filters=None, aggregates=None, columns=None):
    """
    查询数据库中的数据。

    :param model: SQLAlchemy 模型类
    :param filters: 过滤条件列表，例如 [Model.column == value]
    :param aggregates: 聚合函数列表，例如 [func.count(Model.column)]
    :param columns: 要查询的列列表，默认为所有列
    :return: 包含查询结果的 DataFrame
    """
    if columns is None:
        columns = model.__table__.columns.keys()
    
    query = session.query(*[getattr(model, col) for col in columns])
    
    if filters:
        for filter_condition in filters:
            query = query.filter(filter_condition)
    
    if aggregates:
        query = query.add_columns(*aggregates)
    
    result = query.all()
    
    if aggregates:
        column_names = columns + [str(agg).split(' ')[0] for agg in aggregates]
    else:
        column_names = columns
    
    data = [
        {
            column_name: getattr(row, column_name) if hasattr(row, column_name) else row[i]
            for i, column_name in enumerate(column_names)
        }
        for row in result
    ]
    
    return pd.DataFrame(data)

def update_data(model, filters, update_values):
    """
    根据条件更新数据库中的数据。

    :param model: SQLAlchemy 模型类
    :param filters: 过滤条件列表，例如 [Model.column == value]
    :param update_values: 要更新的值，字典形式，例如 {'column_name': 'new_value'}
    :return: 更新的记录数
    """
    try:
        query = session.query(model)
        for filter_condition in filters:
            query = query.filter(filter_condition)
        updated_count = query.update(update_values)
        session.commit()
        return updated_count
    except Exception as e:
        session.rollback()
        print(f"更新出错: {e}")
        return 0

if __name__ == "__main__":
    # 元数据类型修改，更新指标类型【时间、字符串、数值、类型、主键】
    df_all_columns = query_data(IndexRobotColumn,filters=[IndexRobotColumn.data_type == '4'])
    print("所有列查询结果:",df_all_columns)
    # 获取指标相关信息,IndexRobotTarget,传入指标名，查询相关信息
    # df_target = query_data(IndexRobotTarget,filters=[IndexRobotTarget.target_name == '-'])
    
    # 获取指标信息，IndexRobotColumn,传入指标名，查询相关信息
    df_column = query_data(IndexRobotColumn,filters=[IndexRobotColumn.column_remark == '开放床数'])
    print("所有列查询结果:",df_column.columns)
    print("所有列查询结果:",df_column)

    # 获取database_id、schema_id、table_id、
    database_id = df_column['database_id'].values[0]
    schema_id = df_column['schema_id'].values[0]
    table_id = df_column['table_id'].values[0]
    print(f'database_id : {database_id}',f'schema_id : {schema_id}',f'table_id : {table_id}')

    # remark_name teble_name data ,需要换成id
    filters = [IndexRobotColumn.column_remark == '开放床数',IndexRobotColumn.table_name == 'hospital_cmis_tipsi']
    update_values = {'data_type': 2}
    updated_count = update_data(IndexRobotColumn, filters, update_values)
    print(f"更新的记录数: {updated_count}")

    # 新增数据类型原子指标
    # 1.获取维度
    # 1.1获取血缘
    filters = [IndexRobotModel.table_init_id == table_id]
    df_model = query_data(IndexRobotModel, filters=filters)
    print("所有列查询结果:",df_model)
    # 1.2没有血缘，找自身
    filter = [IndexRobotTable.id == table_id]
    df_table = query_data(IndexRobotTable, filters=filter)
    print("所有列查询结果:",df_table)
    filters = [IndexRobotColumn.table_id == table_id,or_(IndexRobotColumn.data_type == 3,IndexRobotColumn.data_type == 5)]
    df_column = query_data(IndexRobotColumn, filters=filters)
    print("所有列查询结果:",df_column.columns)
    created_on = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    updated_on = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    column_id = df_column['id'].values[0]
    column_name = df_column['column_name'].values[0]
    database_id = df_column['database_id'].values[0]
    
    table_id = df_column['table_id'].values[0]
    table_name = df_column['table_name'].values[0]
    
    # 2.新增指标

# try:
#     # 示例：查询所有列
#     df_all_columns = query_data(IndexRobotColumn)
#     print("所有列查询结果:")
#     print(df_all_columns)

#     # 示例：查询指定列并添加过滤条件
#     filters = [IndexRobotColumn.column_type == '4']
#     columns = ['id', 'column_name']
#     df_filtered = query_data(IndexRobotColumn, filters=filters, columns=columns)
#     print("\n指定列和过滤条件查询结果:")
#     print(df_filtered)

#     # 示例：查询并使用聚合函数，添加 GROUP BY
#     aggregates = [func.count(IndexRobotColumn.id)]
#     columns = ['column_type']  # 选择一个非聚合列进行分组
#     filters = []
#     query = session.query(*[getattr(IndexRobotColumn, col) for col in columns]).add_columns(*aggregates).group_by(*columns)
#     if filters:
#         for filter_condition in filters:
#             query = query.filter(filter_condition)
#     result = query.all()
#     column_names = columns + [str(agg).split(' ')[0] for agg in aggregates]
#     data = [
#         {
#             column_name: getattr(row, column_name) if hasattr(row, column_name) else row[i]
#             for i, column_name in enumerate(column_names)
#         }
#         for row in result
#     ]
#     df_aggregated = pd.DataFrame(data)
#     print("\n聚合查询结果:")
#     print(df_aggregated)

# except Exception as e:
#     print(f"查询出错: {e}")
# finally:
#     # 关闭会话
#     session.close()