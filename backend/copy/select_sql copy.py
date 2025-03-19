import uuid
import datetime
import faker
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

def insert_into(model, insert_values):
    """
    向数据库中插入数据。

    :param model: SQLAlchemy 模型类
    :param insert_values: 要插入的值，字典形式，例如 {'column_name': 'new_value'}
    :return: 插入成功返回 True，失败返回 False
    """
    try:
        new_record = model(**insert_values)
        session.add(new_record)
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        print(f"插入出错: {e}")
        return False

if __name__ == "__main__":
    aim_target = '抢救次数'
    # 元数据类型修改，更新指标类型【时间、字符串、数值、类型、主键】
    df_all_columns = query_data(IndexRobotColumn, filters=[IndexRobotColumn.data_type == '4'])
    print("所有列查询结果:", df_all_columns.T, sep='\n')

    # 获取字段信息，IndexRobotColumn,传入字段/中文名，查询相关信息
    df_column = query_data(IndexRobotColumn, filters=[IndexRobotColumn.column_remark == aim_target])
    print("所有列名:", df_column.columns, sep='\n')
    print("所有列查询结果:", df_column.T, sep='\n')

    # 获取database_id、schema_id、table_id、
    database_id = df_column['database_id'].values[0]
    schema_id = df_column['schema_id'].values[0]
    table_id = df_column['table_id'].values[0]
    table_name = df_column['table_name'].values[0]
    print(f'database_id : {database_id}', f'schema_id : {schema_id}', 
          f'table_id : {table_id}', f'table_name : {table_name}',sep='\n')

    # remark_name teble_name data ,需要换成id
    filters = [IndexRobotColumn.column_remark == aim_target, IndexRobotColumn.table_name == table_name]
    new_data_type = 2
    update_values = {'data_type': new_data_type}
    updated_count = update_data(IndexRobotColumn, filters, update_values)
    print(f"更新的记录数: {updated_count}",f'更新后的data_type: {new_data_type}', sep='\n')

    # 新增数据类型原子指标
    # 1.获取维度
    # 1.1获取血缘
    filters = [IndexRobotModel.table_init_id == table_id]
    df_model = query_data(IndexRobotModel, filters=filters)
    print("所有列查询结果:", df_model.T, sep='\n')
    # 1.2没有血缘，找自身
    filter = [IndexRobotTable.id == table_id]
    df_table = query_data(IndexRobotTable, filters=filter)
    print("所有列查询结果:", df_table.T, sep='\n')
    # TODO 添加类型的集合，简化表达
    filters = [IndexRobotColumn.table_id == table_id, or_(IndexRobotColumn.data_type == 3, IndexRobotColumn.data_type == 5)]
    df_column = query_data(IndexRobotColumn, filters=filters)
    
    # 使用 faker 生成一个 16 位以 9 开头的数值型 logic_id
    fake = faker.Faker()
    same_logic_id = int('9' + fake.numerify(text='#' * 15))

    # 在index_robot_table中通过database_id、schema_id、table_id、获取control_name
    filters = [IndexRobotTable.database_id == database_id, IndexRobotTable.schema_id == schema_id, IndexRobotTable.id == table_id]
    df_control_name = query_data(IndexRobotTable, filters=filters, columns=['control_name'])
    print("所有列查询结果:", df_control_name.T, sep='\n')
    control_name = df_control_name['control_name'].values[0] if not df_control_name.empty else None
    print(f'control_name: {control_name}')
    # 没有血缘，写入指标
    for index, row in df_column.head(1).iterrows():
        insert_values = {
            'created_on': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'updated_on': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'column_id': row['id'],
            'column_name': row['column_name'],
            'database_id': row['database_id'],
            'logic_id': same_logic_id,  # 使用同一个 logic_id
            'table_id': row['table_id'],
            'table_name': row['table_name'],
            'target_formula': '合计',
            'target_name': f'{control_name}-抢救次数',
            'target_number': 'l00009',
            'target_type': '1',
        }
        if insert_into(IndexRobotTarget, insert_values):
            print("指标插入成功")
        else:
            print("指标插入失败")
    # 1.3没有血缘，写入自身维度
    # 遍历df_column，插入IndexRobotDimension
    # 遍历 df_column 并插入数据到 IndexRobotDimension
    for index, row in df_column.iterrows():
        create_on = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        updated_on = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        column_id = row['id']
        column_name = row['column_name']
        data_type = row['data_type']
        dimension_name = row['column_remark']
        dimension_type = '1'
        status = '0'
        table_id = row['table_id']
        table_name = row['table_name']
        target_id = same_logic_id  # 使用同一个 logic_id

        # 准备插入的数据
        insert_values = {
            'created_on': create_on,
            'updated_on': updated_on,
            'column_id': column_id,
            'column_name': column_name,
            'data_type': data_type,
            'dimension_name': dimension_name,
            'dimension_type': dimension_type,
            'status': status,
            'table_id': table_id,
            'table_name': table_name,
            'target_id': target_id
        }

        # 插入数据到 IndexRobotDimension 表
        if insert_into(IndexRobotDimension, insert_values):
            print(f"维度数据插入成功，行索引: {index}")
        else:
            print(f"维度数据插入失败，行索引: {index}")

    
    # 1.2有血缘，找血缘
    # table_id = 105
    filters = [IndexRobotModel.table_init_id == table_id]
    df_model = query_data(IndexRobotModel, filters=filters)
    print("所有列查询结果:", df_model.T, sep='\n')
    print(df_model.shape)
    if df_model.shape[0] != 0:
        pass
    # 用于存储所有的 table_end_id
    all_table_end_ids = set()
    df_all_models = query_data(IndexRobotModel)
    print("所有列查询结果:", df_all_models.T.shape)
    # 在df_all_models查找table_init_id等于table_id的数据，将table_end_id赋值给all__tables,再递归查找，直到all__tables为空为止
    all__tables = [table_id]  # 初始化 all__tables 列表，从当前 table_id 开始
    result_table_end_ids = set()  # 用于存储所有找到的 table_end_id

    while all__tables:
        current_table_id = all__tables.pop(0)  # 取出一个 table_id
        matching_rows = df_all_models[df_all_models['table_init_id'] == current_table_id]
        new_table_end_ids = matching_rows['table_end_id'].tolist()
        result_table_end_ids.update(new_table_end_ids)  # 将新找到的 table_end_id 添加到结果集合中
        all__tables.extend(new_table_end_ids)  # 将新找到的 table_end_id 添加到 all__tables 列表中，继续递归查找

    all_table_end_ids.update(result_table_end_ids)  # 将所有找到的 table_end_id 添加到最终集合中

    print("所有的 table_end_id 集合:", all_table_end_ids)

    # 按照没有血缘的逻辑，将 all_table_end_ids 中的 table_id 作为 table_id，获取 df_column，并打印所有 insert_values
    # 将数据写入 IndexRobotDimension 表，去掉第一张表
    for table_id in all_table_end_ids:
        filters = [IndexRobotColumn.table_id == table_id, or_(IndexRobotColumn.data_type == 3, IndexRobotColumn.data_type == 5)]
        df_column = query_data(IndexRobotColumn, filters=filters)

        for index, row in df_column.iterrows():
            create_on = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            updated_on = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            column_id = row['id']
            column_name = row['column_name']
            data_type = row['data_type']
            dimension_name = row['column_remark']
            # TODO 自身维度，关联维度
            dimension_type = '2'
            status = '0'
            table_id = row['table_id']
            table_name = row['table_name']
            target_id = same_logic_id  # 使用同一个 logic_id

            # 准备插入的数据
            insert_values = {
                'created_on': create_on,
                'updated_on': updated_on,
                'column_id': column_id,
                'column_name': column_name,
                'data_type': data_type,
                'dimension_name': dimension_name,
                'dimension_type': dimension_type,
                'status': status,
                'table_id': table_id,
                'table_name': table_name,
                'target_id': target_id
            }

            # print(f"插入值 for row {index} in table {table_id}: {insert_values}")

            # 插入数据到 IndexRobotDimension 表
            if insert_into(IndexRobotDimension, insert_values):
                print(f"维度数据插入成功，行索引: {index}，表 ID: {table_id}")
            else:
                print(f"维度数据插入失败，行索引: {index}，表 ID: {table_id}")