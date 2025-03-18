# coding: utf-8
from sqlalchemy import BigInteger, Column, DECIMAL, DateTime, Float, ForeignKey, Index, Integer, Table, text
from sqlalchemy.dialects.mysql import BIT, DATETIME, MEDIUMTEXT, TEXT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class AdminDataAccessStrategy(Base):
    __tablename__ = 'admin_data_access_strategy'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    access_type = Column(VARCHAR(20), server_default=text("'READ'"))
    admin_id = Column(BigInteger)
    department_id = Column(BigInteger)
    department_name = Column(VARCHAR(255))
    permission_type = Column(VARCHAR(20), server_default=text("'PERSONAL'"))
    strategy_id = Column(BigInteger)


class AdminDepartment(Base):
    __tablename__ = 'admin_department'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    admin_id = Column(BigInteger)
    department_id = Column(BigInteger)


class AdminNorthStarPermission(Base):
    __tablename__ = 'admin_north_star_permission'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    admin_id = Column(BigInteger)
    business_domain_id = Column(BigInteger)
    target_logic_id = Column(BigInteger)


class AdminTarget(Base):
    __tablename__ = 'admin_targets'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    admin_id = Column(BigInteger)
    department_id = Column(BigInteger)
    department_name = Column(VARCHAR(255))
    permission_type = Column(VARCHAR(20), server_default=text("'PERSONAL'"))
    table_name = Column(VARCHAR(200))
    target_id = Column(BigInteger)
    target_name = Column(VARCHAR(200), server_default=text("''"))


class AiDbConnection(Base):
    __tablename__ = 'ai_db_connection'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    app_id = Column(VARCHAR(100), server_default=text("''"))
    connection_model = Column(VARCHAR(200), server_default=text("''"))
    connection_model_value = Column(VARCHAR(500), server_default=text("''"))
    customization = Column(VARCHAR(500), server_default=text("''"))
    db_key = Column(VARCHAR(200), unique=True, server_default=text("''"))
    db_host = Column(VARCHAR(200), server_default=text("''"))
    name = Column(VARCHAR(200), server_default=text("''"))
    db_password = Column(VARCHAR(200), server_default=text("''"))
    db_port = Column(Integer)
    type = Column(VARCHAR(100), server_default=text("''"))
    db_user_name = Column(VARCHAR(100), server_default=text("''"))


class AiSystemConfig(Base):
    __tablename__ = 'ai_system_config'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    config_json = Column(VARCHAR(2000), server_default=text("''"))
    config_key = Column(VARCHAR(100), unique=True, server_default=text("''"))


class AiSystemDataSource(Base):
    __tablename__ = 'ai_system_data_source'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    app_id = Column(VARCHAR(50), server_default=text("''"))
    code = Column(VARCHAR(100), server_default=text("''"))
    connection_id = Column(BigInteger)
    db_key = Column(VARCHAR(100), server_default=text("''"))
    db_name = Column(VARCHAR(100), server_default=text("''"))
    db_source_type = Column(VARCHAR(50), server_default=text("''"))
    db_type = Column(VARCHAR(30), server_default=text("''"))
    name = Column(VARCHAR(50), server_default=text("''"))
    table_comment = Column(VARCHAR(200), server_default=text("''"))
    table_name = Column(VARCHAR(100), server_default=text("''"))
    type = Column(VARCHAR(50), server_default=text("''"))


class AiSystemDataSourceDetail(Base):
    __tablename__ = 'ai_system_data_source_detail'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    column_as_name = Column(VARCHAR(100), server_default=text("''"))
    column_comment = Column(VARCHAR(200), server_default=text("''"))
    column_length = Column(Integer)
    column_name = Column(VARCHAR(100), server_default=text("''"))
    column_type = Column(VARCHAR(50), server_default=text("''"))
    code = Column(VARCHAR(100), server_default=text("''"))
    data_source_id = Column(BigInteger)


class AiSystemDb(Base):
    __tablename__ = 'ai_system_db'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    db_key = Column(VARCHAR(100), unique=True, server_default=text("''"))
    db_password = Column(VARCHAR(100), server_default=text("''"))
    db_type = Column(VARCHAR(100), server_default=text("''"))
    db_url = Column(VARCHAR(300), server_default=text("''"))
    db_user = Column(VARCHAR(100), server_default=text("''"))


class Algorithm(Base):
    __tablename__ = 'algorithm'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    algorithm_code = Column(VARCHAR(50), nullable=False, server_default=text("''"))
    algorithm_name = Column(VARCHAR(50), nullable=False, server_default=text("''"))
    dictionary_data_id = Column(BigInteger, nullable=False)
    description = Column(VARCHAR(200), nullable=False, server_default=text("''"))
    enable = Column(VARCHAR(10), nullable=False, server_default=text("''"))
    remark = Column(VARCHAR(200), server_default=text("''"))


class AlgorithmCode(Base):
    __tablename__ = 'algorithm_code'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    code = Column(VARCHAR(50), server_default=text("''"))
    status = Column(VARCHAR(50), server_default=text("''"))


class BusinessDomain(Base):
    __tablename__ = 'business_domain'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    name = Column(VARCHAR(255))


class ChatCommonQuestion(Base):
    __tablename__ = 'chat_common_question'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    question = Column(VARCHAR(255))


class ChatCommonQuestionBack(Base):
    __tablename__ = 'chat_common_question_back'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    question = Column(VARCHAR(255))


class ChatLog(Base):
    __tablename__ = 'chat_log'

    id = Column(BigInteger, primary_key=True, comment='����')
    created_on = Column(DATETIME(fsp=6), nullable=False, comment='����ʱ��')
    updated_on = Column(DATETIME(fsp=6), nullable=False, comment='����ʱ��')
    is_satisfied = Column(Integer, comment='�Ƿ�����')
    is_success = Column(Integer, comment='�Ƿ�ɹ�')
    participle = Column(VARCHAR(255), comment='ģ�ʹ����ִʽ��')
    text = Column(VARCHAR(255), comment='�Ի���������')
    is_rebuild = Column(Integer, comment='�Ƿ���������')
    rebuild_count = Column(Integer, comment='�������ɴ���')
    target_json = Column(VARCHAR(1000), comment='ָ���б�(json)')


class ChatReport(Base):
    __tablename__ = 'chat_report'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    canvas_value = Column(VARCHAR(255))
    qyzt = Column(Integer)
    report_describe = Column(VARCHAR(255))
    report_name = Column(VARCHAR(255))
    user_id = Column(BigInteger)


class ChatReportDetail(Base):
    __tablename__ = 'chat_report_detail'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    chart_name = Column(VARCHAR(255))
    param = Column(VARCHAR(255))
    report_id = Column(BigInteger)
    return_value = Column(VARCHAR(255))
    sorted = Column(Integer)
    url = Column(VARCHAR(255))


class ChatReportPermission(Base):
    __tablename__ = 'chat_report_permission'
    __table_args__ = (
        Index('UKhok14d5vt0xmqhu1bmdnjaqhp', 'report_id', 'user_id', unique=True),
    )

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    ower_type = Column(VARCHAR(255), comment='ӵ��������:OWNER,SHARED')
    permission_type = Column(VARCHAR(255), comment='Ȩ������:READONLY,WRITER')
    report_id = Column(BigInteger, index=True)
    report_name = Column(VARCHAR(255), comment='��������')
    user_id = Column(BigInteger, index=True)


class ColumnRecord(Base):
    __tablename__ = 'column_record'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    column_name = Column(VARCHAR(255))
    is_change = Column(Integer)
    record = Column(BigInteger)


class CombinationTargetRefererTarget(Base):
    __tablename__ = 'combination_target_referer_target'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    column_id = Column(BigInteger, comment='�ֶ�id')
    column_name = Column(VARCHAR(255), comment='�ֶ�����')
    combination_target_logic_id = Column(BigInteger, comment='���ָ���߼�id')
    database_id = Column(BigInteger, comment='���ݿ�����id')
    refer_target_name = Column(VARCHAR(255), comment='Ŀ��ָ������')
    referer_target_logic_id = Column(BigInteger, comment='����ָ���߼�id')
    schema_id = Column(BigInteger, comment='���ݿ�id')
    schema_name = Column(VARCHAR(255), comment='���ݿ�����')
    table_id = Column(BigInteger, comment='��id')
    table_name = Column(VARCHAR(255), comment='����')


class CombinationVisualDimensionReferInfo(Base):
    __tablename__ = 'combination_visual_dimension_refer_info'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    column_id = Column(BigInteger, comment='�ֶ�id')
    column_name = Column(VARCHAR(255), comment='�ֶ�����')
    combination_target_logic_id = Column(BigInteger, comment='���ָ���߼�id')
    combination_target_name = Column(VARCHAR(255), comment='Ŀ��ָ������')
    database_id = Column(BigInteger, comment='���ݿ�����id')
    schema_id = Column(BigInteger, comment='���ݿ�id')
    schema_name = Column(VARCHAR(255), comment='���ݿ�����')
    table_id = Column(BigInteger, comment='��id')
    table_name = Column(VARCHAR(255), comment='����')
    visual_dimension_id = Column(BigInteger, comment='����ά��id')
    visual_dimension_name = Column(VARCHAR(255), comment='����ά������')
    visual_column_id = Column(BigInteger, comment='�����ֶ�id')


class CustomerAccount(Base):
    __tablename__ = 'customer_account'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    user_name = Column(VARCHAR(50))
    work_no = Column(VARCHAR(50))


class CustomerDepartment(Base):
    __tablename__ = 'customer_department'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    department_code = Column(VARCHAR(50), unique=True)
    department_name = Column(VARCHAR(50))


class DataModelRelationShip(Base):
    __tablename__ = 'data_model_relation_ship'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)


class DataTask(Base):
    __tablename__ = 'data_task'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    cron = Column(VARCHAR(255))
    database_id = Column(BigInteger, nullable=False)
    database_name = Column(VARCHAR(255))
    qyzt = Column(Integer, nullable=False)
    rate = Column(DECIMAL(19, 2))
    task_desc = Column(VARCHAR(255))
    task_name = Column(VARCHAR(255))
    task_type = Column(Integer)
    ext = Column(DECIMAL(19, 2))


class DatabaseLexiconRelation(Base):
    __tablename__ = 'database_lexicon_relation'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    database_id = Column(BigInteger)
    lexicon_id = Column(BigInteger)


class Dataset(Base):
    __tablename__ = 'dataset'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    dictionary_data_id = Column(BigInteger)
    dataset_code = Column(VARCHAR(50), server_default=text("''"))
    dataset_name = Column(VARCHAR(50), server_default=text("''"))
    description = Column(VARCHAR(200), server_default=text("''"))
    enable = Column(VARCHAR(10), server_default=text("''"))
    remark = Column(VARCHAR(200), server_default=text("''"))
    type_id = Column(BigInteger)


class DatasetCode(Base):
    __tablename__ = 'dataset_code'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    code = Column(VARCHAR(50), server_default=text("''"))
    status = Column(VARCHAR(50), server_default=text("''"))


class DepartmentDataAccessStrategy(Base):
    __tablename__ = 'department_data_access_strategy'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    data_access_strategy_id = Column(BigInteger, nullable=False)
    data_access_strategy_name = Column(VARCHAR(200), server_default=text("''"))
    department_id = Column(BigInteger, nullable=False)


class DepartmentTarget(Base):
    __tablename__ = 'department_targets'
    __table_args__ = (
        Index('UKpiudioomf2qxgrab5tlx2cwy9', 'department_id', 'target_id', unique=True),
    )

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    department_id = Column(BigInteger, nullable=False)
    department_name = Column(VARCHAR(100), server_default=text("''"))
    table_name = Column(VARCHAR(100), server_default=text("''"))
    target_id = Column(BigInteger, nullable=False)
    target_name = Column(VARCHAR(200), server_default=text("''"))


class DictionaryDatum(Base):
    __tablename__ = 'dictionary_data'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    dictionary_data_code = Column(VARCHAR(50), server_default=text("''"))
    dictionary_data_name = Column(VARCHAR(50), server_default=text("''"))
    dictionary_type_id = Column(BigInteger)
    enable = Column(VARCHAR(50), server_default=text("''"))
    remark = Column(VARCHAR(200), server_default=text("''"))


class DictionaryDataCode(Base):
    __tablename__ = 'dictionary_data_code'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    code = Column(VARCHAR(50), server_default=text("''"))
    status = Column(VARCHAR(50), server_default=text("''"))


class DictionaryType(Base):
    __tablename__ = 'dictionary_type'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    dictionary_type_code = Column(VARCHAR(50), server_default=text("''"))
    dictionary_type_name = Column(VARCHAR(50), server_default=text("''"))
    remark = Column(VARCHAR(200), server_default=text("''"))


class DictionaryTypeCode(Base):
    __tablename__ = 'dictionary_type_code'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    code = Column(VARCHAR(50), server_default=text("''"))
    status = Column(VARCHAR(50), server_default=text("''"))


class DrawDept(Base):
    __tablename__ = 'draw_dept'
    __table_args__ = {'comment': '���ű�'}

    id = Column(BigInteger, primary_key=True, comment='���ű�����')
    dept_no = Column(VARCHAR(50), comment='���ű��')
    dept_name = Column(VARCHAR(255), comment='��������')
    parent_no = Column(VARCHAR(50), comment='�ϼ����')
    created_on = Column(DATETIME(fsp=6), nullable=False, comment='����ʱ��')
    updated_on = Column(DATETIME(fsp=6), nullable=False, comment='����ʱ��')


t_draw_prize = Table(
    'draw_prize', metadata,
    Column('id', BigInteger, comment='��Ʒ������'),
    Column('prize_name', VARCHAR(255), comment='��Ʒ��'),
    Column('prize_price', DECIMAL(10, 2), comment='��Ʒ��ֵ'),
    Column('prize_lv', VARCHAR(50), comment='��Ʒ�ȼ�'),
    Column('prize_count', Integer, comment='��Ʒ����'),
    Column('created_on', DATETIME(fsp=6), nullable=False, comment='����ʱ��'),
    Column('updated_on', DATETIME(fsp=6), nullable=False, comment='����ʱ��'),
    comment='��Ʒ��'
)


class DrawRecord(Base):
    __tablename__ = 'draw_record'

    id = Column(BigInteger, primary_key=True, comment='�齱��¼id')
    user_no = Column(VARCHAR(50), comment='�û����')
    user_name = Column(VARCHAR(255), comment='�û�����')
    dept_no = Column(VARCHAR(50), comment='���ű��')
    dept_name = Column(VARCHAR(255), comment='��������')
    prize_name = Column(VARCHAR(255), comment='��Ʒ����')
    prize_price = Column(DECIMAL(10, 2), comment='��Ʒ��ֵ')
    prize_count = Column(Integer, comment='�н�����')
    created_on = Column(DATETIME(fsp=6), nullable=False, comment='����ʱ��')
    updated_on = Column(DATETIME(fsp=6), nullable=False, comment='����ʱ��')
    prize_lv = Column(VARCHAR(255), comment='��Ʒ�ȼ�')


class DrawUser(Base):
    __tablename__ = 'draw_user'
    __table_args__ = {'comment': '�û���'}

    id = Column(BigInteger, primary_key=True, comment='�û�������')
    user_no = Column(VARCHAR(50), comment='�û�����')
    user_name = Column(VARCHAR(255), comment='�û�����')
    gend = Column(VARCHAR(2), comment='�Ա�')
    dept_no = Column(VARCHAR(50), comment='���ű��')
    created_on = Column(DATETIME(fsp=6), nullable=False, comment='����ʱ��')
    updated_on = Column(DATETIME(fsp=6), nullable=False, comment='����ʱ��')


class EsInitLog(Base):
    __tablename__ = 'es_init_log'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    column_id = Column(BigInteger)
    database_id = Column(BigInteger)
    init_date = Column(DATETIME(fsp=6))
    table_id = Column(BigInteger)


class IndexDataAccessStrategy(Base):
    __tablename__ = 'index_data_access_strategy'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    access_type = Column(VARCHAR(20), comment='��������')
    strategy_define = Column(TEXT, comment='��������')
    strategy_desc = Column(VARCHAR(255), comment='��������')
    strategy_name = Column(VARCHAR(120), comment='��������')
    strategy_script = Column(TEXT, comment='����ִ�нű�')
    strategy_type = Column(VARCHAR(20), comment='��������')
    strategy_version = Column(VARCHAR(120), comment='���԰汾')


class IndexDataAccessStrategyDetail(Base):
    __tablename__ = 'index_data_access_strategy_detail'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    column_id = Column(BigInteger)
    database_id = Column(BigInteger)
    limited_values = Column(TEXT, comment='����ֵ')
    schema_id = Column(BigInteger)
    strategy_id = Column(BigInteger, comment='����ID')
    table_id = Column(BigInteger)
    value_source = Column(VARCHAR(255))


class IndexDataDictionary(Base):
    __tablename__ = 'index_data_dictionary'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    column_id = Column(BigInteger, index=True)
    source_value = Column(VARCHAR(255))
    table_id = Column(BigInteger)
    target_value = Column(VARCHAR(255))


class IndexNameMappingEn(Base):
    __tablename__ = 'index_name_mapping_en'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    english_name = Column(VARCHAR(50))
    chinese_name = Column(VARCHAR(50))
    database_id = Column(BigInteger)
    schema_id = Column(BigInteger)
    table_id = Column(BigInteger)


class IndexRobotColumCondition(Base):
    __tablename__ = 'index_robot_colum_condition'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    column_id = Column(BigInteger)
    condition_group_code = Column(VARCHAR(100), server_default=text("'�������'"))
    condition_name = Column(VARCHAR(100), server_default=text("'������'"))
    logic_name = Column(VARCHAR(100), server_default=text("'�߼�����'"))
    parent_condition_group_code = Column(VARCHAR(100), server_default=text("'�����������'"))
    refer_column_id = Column(BigInteger)
    refer_column_name = Column(VARCHAR(100), server_default=text("'�������ֶ�����'"))
    relation = Column(VARCHAR(500), server_default=text("'��ϵ'"))
    sql_expressions = Column(TEXT)
    value = Column(VARCHAR(500), server_default=text("'����ֵ'"))


class IndexRobotColumn(Base):
    __tablename__ = 'index_robot_column'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    column_name = Column(VARCHAR(255))
    column_remark = Column(VARCHAR(255))
    column_type = Column(VARCHAR(255))
    data_type = Column(Integer)
    database_id = Column(BigInteger)
    date_convert_format = Column(VARCHAR(50), server_default=text("''"))
    qyzt = Column(Integer)
    schema_id = Column(BigInteger)
    schema_name = Column(VARCHAR(255))
    table_id = Column(BigInteger)
    table_name = Column(VARCHAR(255))
    yuliu2 = Column(VARCHAR(255))
    created_visual_flag = Column(VARCHAR(10), server_default=text("'N'"))
    target_id = Column(BigInteger)


class IndexRobotCondition(Base):
    __tablename__ = 'index_robot_condition'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    column_id = Column(BigInteger)
    column_name = Column(VARCHAR(255))
    condition_group_code = Column(VARCHAR(100), server_default=text("'�������'"))
    condition_name = Column(VARCHAR(255))
    logic_name = Column(VARCHAR(100), server_default=text("'�߼�����'"))
    parent_condition_group_code = Column(VARCHAR(100), server_default=text("'�����������'"))
    relation = Column(VARCHAR(255))
    sql_expressions = Column(TEXT)
    target_id = Column(BigInteger, index=True)
    value = Column(VARCHAR(255))


class IndexRobotDatabase(Base):
    __tablename__ = 'index_robot_database'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    name = Column(VARCHAR(200), comment='���ݿ�������')
    password = Column(VARCHAR(100), comment='���ݿ���������')
    port = Column(VARCHAR(50), comment='���ݿ�˿�')
    space = Column(VARCHAR(100), comment='�ռ��ַ')
    status = Column(Integer, comment='״̬')
    type = Column(VARCHAR(50), comment='���ݿ�����')
    url = Column(VARCHAR(100), comment='���ݿ�ip��ַ')
    username = Column(VARCHAR(100), comment='���ݿ������û���')


class IndexRobotDimension(Base):
    __tablename__ = 'index_robot_dimension'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    column_id = Column(BigInteger)
    column_name = Column(VARCHAR(255))
    data_type = Column(Integer, nullable=False)
    default_date_dimension = Column(VARCHAR(10), server_default=text("'N'"), comment='Ĭ������ά��')
    dimension_name = Column(VARCHAR(255))
    dimension_type = Column(Integer, nullable=False)
    status = Column(Integer, nullable=False)
    table_id = Column(BigInteger)
    table_name = Column(VARCHAR(255))
    target_id = Column(BigInteger, index=True)
    zh_target_id = Column(BigInteger)


class IndexRobotLabel(Base):
    __tablename__ = 'index_robot_label'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    label_describe = Column(VARCHAR(255))
    label_name = Column(VARCHAR(255))
    logic_id = Column(BigInteger, index=True)
    schema_match = Column(VARCHAR(255))
    table_match = Column(VARCHAR(255))
    type = Column(Integer)


class IndexRobotLabelRelation(Base):
    __tablename__ = 'index_robot_label_relation'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    label_id = Column(BigInteger)
    target_id = Column(BigInteger)
    target_type = Column(Integer)


class IndexRobotLabelRelationV2(Base):
    __tablename__ = 'index_robot_label_relation_v2'
    __table_args__ = (
        Index('IDX_RELATION', 'type', 'data_id'),
    )

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    create_type = Column(Integer)
    data_id = Column(BigInteger)
    label_id = Column(BigInteger)
    type = Column(Integer)


class IndexRobotModel(Base):
    __tablename__ = 'index_robot_model'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    database_id = Column(BigInteger)
    is_auto = Column(Integer)
    join_type = Column(VARCHAR(100), server_default=text("''"), comment='��������')
    sentence = Column(VARCHAR(255))
    table_end_control = Column(VARCHAR(255))
    table_end_id = Column(BigInteger)
    table_end_name = Column(VARCHAR(255))
    table_end_schema = Column(VARCHAR(255))
    table_init_control = Column(VARCHAR(255))
    table_init_id = Column(BigInteger)
    table_init_name = Column(VARCHAR(255))
    table_init_schema = Column(VARCHAR(255))


class IndexRobotModelRelation(Base):
    __tablename__ = 'index_robot_model_relation'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    column_end_control = Column(VARCHAR(255))
    column_end_id = Column(BigInteger)
    column_end_name = Column(VARCHAR(255))
    column_init_control = Column(VARCHAR(255))
    column_init_id = Column(BigInteger)
    column_init_name = Column(VARCHAR(255))
    database_id = Column(BigInteger)
    is_auto = Column(Integer)
    model_id = Column(BigInteger)
    relation = Column(VARCHAR(255))


class IndexRobotNumber(Base):
    __tablename__ = 'index_robot_number'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    number_length = Column(Integer)
    number_prefix = Column(VARCHAR(255))
    number_type = Column(Integer)
    number_value = Column(Integer)


class IndexRobotSchema(Base):
    __tablename__ = 'index_robot_schema'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    control_name = Column(VARCHAR(255))
    database_id = Column(BigInteger)
    db_type = Column(VARCHAR(255), comment='���ݿ�����')
    schema_name = Column(VARCHAR(255))
    yuliu1 = Column(VARCHAR(255))
    yuliu2 = Column(VARCHAR(255))


class IndexRobotTable(Base):
    __tablename__ = 'index_robot_table'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    control_name = Column(VARCHAR(255))
    database_id = Column(BigInteger)
    is_main_data = Column(Integer)
    is_real_table = Column(Integer)
    need_distinct = Column(VARCHAR(10), comment='N����Ҫȥ�أ�Y��Ҫȥ��')
    qyzt = Column(Integer)
    schema_id = Column(BigInteger)
    schema_name = Column(VARCHAR(255))
    stop_remark = Column(Integer)
    table_name = Column(VARCHAR(255))
    yuliu2 = Column(VARCHAR(255))


class IndexRobotTargetDetail(Base):
    __tablename__ = 'index_robot_target_detail'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    target_define = Column(TEXT)
    target_logic_id = Column(BigInteger, unique=True)


class IndexRobotTargetZh(Base):
    __tablename__ = 'index_robot_target_zh'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    target_define = Column(VARCHAR(255))
    target_formula = Column(VARCHAR(255))
    target_name = Column(VARCHAR(255))
    target_number = Column(VARCHAR(255))


class IndexTargetCategory(Base):
    __tablename__ = 'index_target_category'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    category_comment = Column(VARCHAR(255), server_default=text("''"), comment='ָ����౸ע')
    category_name = Column(VARCHAR(255), server_default=text("''"), comment='ָ���������')
    parent_id = Column(ForeignKey('index_target_category.id'), index=True)

    parent = relationship('IndexTargetCategory', remote_side=[id])


class Indicator(Base):
    __tablename__ = 'indicator'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    dictionary_data_id = Column(BigInteger, nullable=False)
    data_type = Column(BigInteger, nullable=False)
    enable = Column(VARCHAR(10), nullable=False, server_default=text("''"))
    indicator_code = Column(VARCHAR(50), nullable=False, server_default=text("''"))
    indicator_formula = Column(VARCHAR(200), nullable=False, server_default=text("''"))
    indicator_name = Column(VARCHAR(50), nullable=False, server_default=text("''"))
    remark = Column(VARCHAR(200), server_default=text("''"))


class IndicatorCode(Base):
    __tablename__ = 'indicator_code'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    code = Column(VARCHAR(50), server_default=text("''"))
    status = Column(VARCHAR(50), server_default=text("''"))


class InitPsTargetResult(Base):
    __tablename__ = 'init_ps_target_result'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    batch_no = Column(VARCHAR(255))
    create_file_date = Column(DATETIME(fsp=6))
    database_id = Column(BigInteger)
    exec_sql_begin_date = Column(DATETIME(fsp=6))
    exec_sql_end_date = Column(DATETIME(fsp=6))
    file_path = Column(VARCHAR(255))
    table_id = Column(BigInteger)
    io_close_date = Column(DATETIME(fsp=6))


class Itestd(Base):
    __tablename__ = 'itestd'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    source_value = Column(VARCHAR(255))


class Lexicon(Base):
    __tablename__ = 'lexicon'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    name = Column(VARCHAR(255))
    path = Column(VARCHAR(255))


class MetadataTargerLog(Base):
    __tablename__ = 'metadata_targer_log'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    batch_date = Column(DATETIME(fsp=6))
    database_id = Column(BigInteger)
    doing_now = Column(VARCHAR(255))
    event = Column(Integer)
    log_date = Column(DATETIME(fsp=6))
    status = Column(Integer, nullable=False)


class NorthStartTargetRelation(Base):
    __tablename__ = 'north_start_target_relation'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    business_domain_id = Column(BigInteger)
    column_id = Column(BigInteger, nullable=False)
    dimension_id = Column(BigInteger, comment='Ĭ��ʱ��ά��ID')
    period_type_name = Column(VARCHAR(255), comment='ָ��չʾʱ��Ĭ��ʱ������')
    target_id = Column(BigInteger)


class PermissionStrategy(Base):
    __tablename__ = 'permission_strategy'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    strategy_code = Column(VARCHAR(50), unique=True, server_default=text("''"))
    strategy_name = Column(VARCHAR(100), server_default=text("''"))


class RecommendQuestion(Base):
    __tablename__ = 'recommend_question'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    question = Column(VARCHAR(255), comment='����')
    question_type = Column(VARCHAR(50), comment='��������')


class SqlResultDto(Base):
    __tablename__ = 'sql_result_dto'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    group_field = Column(VARCHAR(255))
    sum = Column(VARCHAR(255))


class SysCaliber(Base):
    __tablename__ = 'sys_caliber'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    caliber = Column(VARCHAR(20), index=True, server_default=text("''"))
    effective_date = Column(VARCHAR(20), index=True, server_default=text("''"))
    value = Column(VARCHAR(200), server_default=text("''"))


class SysConfigCommonParameterType(Base):
    __tablename__ = 'sys_config_common_parameter_type'
    __table_args__ = {'comment': '�������ͱ�'}

    id = Column(VARCHAR(36), primary_key=True, server_default=text("''"), comment='����')
    code = Column(VARCHAR(255), server_default=text("''"), comment='code')
    match_rule = Column(VARCHAR(255), server_default=text("''"), comment='ƥ�����')
    name = Column(VARCHAR(255), server_default=text("''"), comment='����')
    type = Column(VARCHAR(255), server_default=text("''"), comment='����')


class SysConfigParameterType(Base):
    __tablename__ = 'sys_config_parameter_type'
    __table_args__ = {'comment': '�������ͱ�'}

    id = Column(VARCHAR(36), primary_key=True, server_default=text("''"), comment='����')
    application_id = Column(VARCHAR(255), server_default=text("''"), comment='Ӧ��id')
    code = Column(VARCHAR(255), server_default=text("''"), comment='code')
    match_rule = Column(VARCHAR(255), server_default=text("''"), comment='ƥ�����')
    name = Column(VARCHAR(255), server_default=text("''"), comment='����')
    type = Column(VARCHAR(255), server_default=text("''"), comment='����')


class SysDisease(Base):
    __tablename__ = 'sys_disease'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    code = Column(VARCHAR(255), server_default=text("''"), comment='��������')
    name = Column(VARCHAR(255), server_default=text("''"), comment='����')
    parent_code = Column(VARCHAR(255), server_default=text("''"), comment='�ϼ�����')


class SysJixiao(Base):
    __tablename__ = 'sys_jixiao'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    compute_method = Column(VARCHAR(255), server_default=text("''"), comment='���㷽ʽ')
    index_definition = Column(VARCHAR(255), server_default=text("''"), comment='ָ�궨��')
    index_desc = Column(VARCHAR(255), server_default=text("''"), comment='ָ��˵��')
    index_name = Column(VARCHAR(255), server_default=text("''"), comment='ָ������')
    index_orientation = Column(VARCHAR(255), server_default=text("''"), comment='ָ�굼��')
    index_property = Column(VARCHAR(255), server_default=text("''"), comment='ָ������')
    one = Column(VARCHAR(255), server_default=text("''"), comment='һ��')
    two = Column(VARCHAR(255), server_default=text("''"), comment='����')
    unit = Column(VARCHAR(255), server_default=text("''"), comment='������λ')


class SystemLog(Base):
    __tablename__ = 'system_log'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    app_name = Column(VARCHAR(100), server_default=text("''"))
    execute_detail = Column(VARCHAR(1000), server_default=text("''"))
    request_method = Column(VARCHAR(100), server_default=text("''"))
    execute_result = Column(Integer)
    execute_runtime = Column(Float(asdecimal=True))
    execute_sql = Column(VARCHAR(1000), server_default=text("''"))
    sub_system_name = Column(VARCHAR(100), server_default=text("''"))


class TargetStaticRecord(Base):
    __tablename__ = 'target_static_record'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    access_type = Column(VARCHAR(100), server_default=text("''"))
    category_id = Column(BigInteger)
    target_id = Column(BigInteger, server_default=text("'0'"))
    target_type = Column(Integer)
    user_id = Column(BigInteger)
    user_name = Column(VARCHAR(100), server_default=text("''"))


class TempSource(Base):
    __tablename__ = 'temp_source'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    allow_null_value = Column(VARCHAR(255))
    column_name = Column(VARCHAR(255))
    column_default_value = Column(VARCHAR(255))
    column_type = Column(VARCHAR(255))
    comment = Column(VARCHAR(255))
    source_table_name = Column(VARCHAR(255))
    temp_table_name = Column(VARCHAR(255))


class TopoFunction(Base):
    __tablename__ = 'topo_function'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    function_category = Column(VARCHAR(255), comment='�������')
    function_desc = Column(VARCHAR(255), comment='��������')
    function_expression = Column(VARCHAR(255), comment='��������ʽ')
    function_name = Column(VARCHAR(255), comment='��������')


class UfhAdmin(Base):
    __tablename__ = 'ufh_admin'

    id = Column(BigInteger, primary_key=True, comment='����')
    created_on = Column(DATETIME(fsp=6), comment='����ʱ��')
    updated_on = Column(DATETIME(fsp=6), comment='����ʱ��')
    bu_code = Column(TEXT, comment='���ű���')
    facility = Column(VARCHAR(500), server_default=text("''"), comment='facility����')
    login_name = Column(VARCHAR(50), nullable=False, unique=True, comment='��¼id')
    market = Column(VARCHAR(500), server_default=text("''"), comment='�г�����')
    password = Column(VARCHAR(255), nullable=False, comment='��¼����')
    status = Column(Integer, comment='�˻�״̬')
    comment = Column(VARCHAR(255), server_default=text("''"), comment='��ע')
    format_bu_code = Column(TEXT, comment='bucode��ʽ�������ڽ���')
    hq = Column(VARCHAR(255), server_default=text("''"), comment='hq')
    real_name = Column(VARCHAR(50), server_default=text("''"))
    channel = Column(VARCHAR(50), server_default=text("''"))
    auth_user_id = Column(VARCHAR(50), server_default=text("''"))
    email = Column(VARCHAR(100), server_default=text("''"))
    is_auto_authorization = Column(Integer, nullable=False)


class UfhAdminApplicationResourceDataPermission(Base):
    __tablename__ = 'ufh_admin_application_resource_data_permissions'
    __table_args__ = {'comment': '�û����������Ȩ��'}

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    admin_id = Column(BigInteger, nullable=False, comment='����Աid')
    bu_code = Column(VARCHAR(255), nullable=False, comment='����bu')
    facility = Column(VARCHAR(255), nullable=False, comment='����facility')
    market = Column(VARCHAR(255), nullable=False, comment='����market')
    resource_id = Column(BigInteger, nullable=False, comment='������Ӧ��id')


class UfhAdminMetadatum(Base):
    __tablename__ = 'ufh_admin_metadata'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    admin_id = Column(BigInteger, nullable=False)
    metadata_id = Column(BigInteger, nullable=False)
    metadata_type = Column(Integer, nullable=False)


class UfhAdminResourcePermission(Base):
    __tablename__ = 'ufh_admin_resource_permissions'
    __table_args__ = {'comment': '����Ա�û�����Դ��ϵ��Ȩ��'}

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    admin_id = Column(BigInteger, nullable=False, comment='����Ա�˻�id')
    permissions = Column(VARCHAR(400), nullable=False, comment='��Դ�Ĳ���Ȩ�ޣ�create\\update��')
    resource_id = Column(BigInteger, nullable=False, comment='��Դid')
    status = Column(Integer, nullable=False)


class UfhAdminRole(Base):
    __tablename__ = 'ufh_admin_role'
    __table_args__ = {'comment': '����Ա��ɫ��ϵ'}

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    admin_id = Column(BigInteger, nullable=False, comment='����Աid')
    role_id = Column(BigInteger, nullable=False, comment='��ɫid')


class UfhAdminTimeDictionaryCondition(Base):
    __tablename__ = 'ufh_admin_time_dictionary_condition'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    admin_id = Column(BigInteger, nullable=False, index=True, comment='�û�id')
    column_id = Column(BigInteger, nullable=False, index=True, comment='�ֶ�id')
    condition_order = Column(Integer, server_default=text("'0'"), comment='����˳��')
    logical_operator = Column(VARCHAR(255), nullable=False, comment='�洢��ֵ')
    operator = Column(VARCHAR(255), nullable=False, comment='����')
    value = Column(VARCHAR(255), nullable=False, comment='�洢��ֵ')


class UfhApplicationResourceDataPermission(Base):
    __tablename__ = 'ufh_application_resource_data_permissions'
    __table_args__ = (
        Index('UK3rsb16g9876jikbti1rer8hre', 'application_id', 'resource_id', unique=True),
        {'comment': '��Դ������Ȩ������'}
    )

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    bu_field = Column(VARCHAR(255), nullable=False, comment='������BU')
    facility_field = Column(VARCHAR(255), nullable=False, comment='������facility')
    market_field = Column(VARCHAR(255), nullable=False, comment='������market')
    resource_id = Column(BigInteger, nullable=False, unique=True, comment='��Դid')
    use_bucode = Column(BIT(1), nullable=False, comment='�Ƿ�ʹ��bu����')
    use_facility = Column(BIT(1), nullable=False, comment='�Ƿ�ʹ��facility����')
    use_market = Column(BIT(1), nullable=False, comment='�Ƿ�ʹ��market����')
    application_id = Column(BigInteger, nullable=False, comment='��Դ����Ӧ��id')


class UfhCustomer(Base):
    __tablename__ = 'ufh_customer'
    __table_args__ = {'comment': '�����ı����ɺ���'}

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    address = Column(VARCHAR(200), nullable=False, server_default=text("''"))
    date_of_birth = Column(VARCHAR(30), nullable=False, server_default=text("''"))
    email = Column(VARCHAR(100), nullable=False, server_default=text("''"))
    facility = Column(VARCHAR(50), nullable=False, server_default=text("''"))
    family_name = Column(VARCHAR(30), nullable=False, server_default=text("''"))
    first_name = Column(VARCHAR(30), nullable=False, server_default=text("''"))
    language_flag = Column(VARCHAR(20), nullable=False, server_default=text("''"))
    mobile = Column(VARCHAR(20), nullable=False, server_default=text("''"))
    mrn = Column(VARCHAR(50), nullable=False, index=True, server_default=text("''"))
    nationality = Column(VARCHAR(50), nullable=False, server_default=text("''"))
    nationality_id = Column(VARCHAR(10), nullable=False, server_default=text("''"))
    preferable_language = Column(VARCHAR(50), nullable=False, server_default=text("''"))


class UfhDepartment(Base):
    __tablename__ = 'ufh_department'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    department_code = Column(VARCHAR(50), unique=True)
    department_name = Column(VARCHAR(50), nullable=False, unique=True)
    parent_id = Column(BigInteger, nullable=False)


class UfhResourceNoSequence(Base):
    __tablename__ = 'ufh_resource_no_sequence'
    __table_args__ = {'comment': '��Դ�������sequence'}

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    code_type = Column(VARCHAR(20), server_default=text("''"), comment=' �������')
    has_used = Column(BIT(1), nullable=False, comment='�Ƿ�ʹ��')
    sequence_day = Column(VARCHAR(20), index=True, server_default=text("''"), comment='�����������')
    sequence_format_value = Column(VARCHAR(30), unique=True, server_default=text("''"), comment='format��ı��ֵ')
    sequence_value = Column(Integer, nullable=False, comment='formatǰ��ֵ')


class UfhRoleMetadatum(Base):
    __tablename__ = 'ufh_role_metadata'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    metadata_id = Column(BigInteger, nullable=False)
    metadata_type = Column(Integer, nullable=False)
    role_id = Column(BigInteger, nullable=False)


class UfhRoleTimeDictionaryCondition(Base):
    __tablename__ = 'ufh_role_time_dictionary_condition'
    __table_args__ = {'comment': '��ɫ��ʱ���ֶ������Ĺ�ϵ��'}

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    role_id = Column(BigInteger, nullable=False, comment='��ɫid')
    column_id = Column(BigInteger, nullable=False, comment='�ֶ�id')
    operator = Column(VARCHAR(255), nullable=False, comment='����')
    value = Column(VARCHAR(255), nullable=False, comment='�洢��ֵ')
    logical_operator = Column(VARCHAR(3), nullable=False, comment='�߼������')
    condition_order = Column(Integer, server_default=text("'0'"), comment='����˳��')


class UfhSystemDataHierarchy(Base):
    __tablename__ = 'ufh_system_data_hierarchy'
    __table_args__ = {'comment': 'Ufh����֯�ṹ��ϵ'}

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    bu_code = Column(VARCHAR(100), nullable=False, comment='bu����')
    hq = Column(VARCHAR(100), nullable=False, comment='hq')
    market_or_facility = Column(VARCHAR(100), nullable=False)
    market_or_facility_type = Column(VARCHAR(255), nullable=False)


class UfhSystemFormFilter(Base):
    __tablename__ = 'ufh_system_form_filter'
    __table_args__ = (
        Index('UKmo7yq81wuj7hdgbd59wx38flb', 'reference_table', 'filter_key', unique=True),
        Index('UK9pwuf8fjqw0q5mmi6pplwqb39', 'reference_table', 'filter_key', unique=True),
        {'comment': 'ƽ̨�Ĺ�����������'}
    )

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    filter_execution_type = Column(VARCHAR(50), nullable=False, server_default=text("''"), comment='�����ִ������')
    filter_hint = Column(VARCHAR(50), nullable=False, server_default=text("''"), comment='�������ʾ')
    filter_input_type = Column(VARCHAR(50), nullable=False, server_default=text("''"), comment='�������������')
    filter_key = Column(VARCHAR(50), nullable=False, server_default=text("''"), comment='����������ֶ�key')
    filter_label = Column(VARCHAR(50), nullable=False, server_default=text("''"), comment='�������ʾlabel')
    reference_table = Column(VARCHAR(50), nullable=False, server_default=text("''"), comment='�����ı�')
    select_filter_values = Column(VARCHAR(200), nullable=False, server_default=text("''"), comment='�Ƿ�ɸѡ���͵����')


class UfhSystemFunctionalResource(Base):
    __tablename__ = 'ufh_system_functional_resources'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    display_name = Column(VARCHAR(255), nullable=False, comment='��ʾ����')
    name = Column(VARCHAR(255), nullable=False, comment='��Դ��������')
    notes = Column(VARCHAR(255), nullable=False, comment='��ע')
    path = Column(VARCHAR(255), nullable=False, server_default=text("''"), comment='��Դ����·��')


class UfhSystemLog(Base):
    __tablename__ = 'ufh_system_log'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    action = Column(VARCHAR(50), server_default=text("''"))
    app_name = Column(VARCHAR(50), server_default=text("''"))
    content = Column(VARCHAR(500), server_default=text("''"))
    data_file_url = Column(VARCHAR(500), server_default=text("''"))
    has_file_url = Column(TINYINT(1), server_default=text("'0'"))
    ip = Column(VARCHAR(50), server_default=text("''"))
    oeprator = Column(VARCHAR(100), index=True, server_default=text("''"))
    oeprator_time = Column(VARCHAR(50), server_default=text("''"))
    path = Column(VARCHAR(200), server_default=text("''"))


class UfhSystemLog(Base):
    __tablename__ = 'ufh_system_logs'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    ind_trace_id = Column(VARCHAR(100), nullable=False, server_default=text("''"), comment='Ψһ��ʶ')
    log_type = Column(VARCHAR(100), nullable=False, server_default=text("''"), comment='����')
    operator = Column(VARCHAR(100), nullable=False, server_default=text("''"), comment='������')
    request_method = Column(VARCHAR(200), nullable=False, server_default=text("''"), comment='���󷽷�')
    request_parameters = Column(VARCHAR(800), nullable=False, server_default=text("''"), comment='�������')
    request_url = Column(VARCHAR(300), nullable=False, server_default=text("''"), comment='�����ַ')
    response_value = Column(MEDIUMTEXT, comment='��Ӧ���')


class UfhSystemPermission(Base):
    __tablename__ = 'ufh_system_permissions'
    __table_args__ = {'comment': '������Դӵ�е�Ȩ�޹����б�'}

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    concrete_resource_id = Column(BigInteger, nullable=False, comment='��Դid')
    display_name = Column(VARCHAR(50), nullable=False, comment='��ʾ����')
    name = Column(VARCHAR(50), nullable=False, comment='����')
    notes = Column(VARCHAR(100), nullable=False, comment='��ע')


class UfhSystemResourceMeta(Base):
    __tablename__ = 'ufh_system_resource_meta'
    __table_args__ = {'comment': '��Դ������Ԫ����'}

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    extension = Column(VARCHAR(255), nullable=False, comment='��չ����')
    meta_type = Column(VARCHAR(50), nullable=False, comment='Ԫ��������')
    resource_id = Column(BigInteger, nullable=False, comment='������Դid')
    value = Column(VARCHAR(100), nullable=False, comment='Ԫ����ֵ')


class UfhSystemResource(Base):
    __tablename__ = 'ufh_system_resources'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    comment = Column(VARCHAR(200), server_default=text("''"), comment='��ע')
    depth = Column(Integer, nullable=False, comment='ϵͳ��Դ���')
    functional_resource_id = Column(BigInteger, nullable=False, server_default=text("'0'"), comment='�����Ĺ���id')
    group_id = Column(Integer, nullable=False, server_default=text("'1'"), comment='������')
    icon = Column(VARCHAR(255), nullable=False, comment='��Դ��icon')
    internal_full_path = Column(VARCHAR(200), nullable=False, server_default=text("''"), comment='������·�������߼�����')
    internal_uuid = Column(VARCHAR(32), nullable=False, server_default=text("''"), comment='��Դ��uuid')
    locked = Column(BIT(1), nullable=False, comment='�Ƿ���ס')
    name = Column(VARCHAR(255), nullable=False, comment='��Դ����')
    parent_id = Column(BigInteger, nullable=False, comment='��Դ����һ��id')
    path = Column(VARCHAR(500), nullable=False, comment='����·��')
    resource_number = Column(VARCHAR(255), nullable=False, comment='��Դ����')
    resource_type = Column(VARCHAR(255), nullable=False, comment='��Դ����')
    settings = Column(VARCHAR(500), nullable=False, server_default=text("''"), comment='������Ϣ')
    sort_order = Column(Integer, nullable=False, comment='����')
    status = Column(Integer, nullable=False, comment='״̬')
    bu_column = Column(VARCHAR(30), server_default=text("''"), comment='������BU')
    facility_column = Column(VARCHAR(30), server_default=text("''"), comment='������facility')
    hq_column = Column(VARCHAR(30), server_default=text("''"), comment='hq')
    market_column = Column(VARCHAR(30), server_default=text("''"), comment='������market')
    title = Column(VARCHAR(50), server_default=text("''"), comment='��Դ����')
    group_name = Column(VARCHAR(30), server_default=text("''"))


class UfhSystemRoleResource(Base):
    __tablename__ = 'ufh_system_role_resource'
    __table_args__ = {'comment': '��Դ�ͽ�ɫ�Ĺ�ϵ'}

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    permissions = Column(VARCHAR(400), nullable=False, comment='Ȩ����Ϣ')
    resource_id = Column(BigInteger, nullable=False, comment='��Դ��ID')
    role_id = Column(BigInteger, nullable=False, comment='��ɫID')
    status = Column(Integer, nullable=False)


class UfhSystemRole(Base):
    __tablename__ = 'ufh_system_roles'
    __table_args__ = {'comment': 'ϵͳ��ɫ��'}

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    display_name = Column(VARCHAR(50), nullable=False, comment='��ɫչʾ����')
    name = Column(VARCHAR(50), nullable=False, comment='��ɫ')
    notes = Column(VARCHAR(50), nullable=False, comment='��ע')
    status = Column(Integer, nullable=False, comment='0:������1:����')
    is_auto_authorization = Column(Integer, nullable=False)


class UfhSystemRolesInterface(Base):
    __tablename__ = 'ufh_system_roles_interface'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    interface_name = Column(VARCHAR(255), nullable=False)
    role_id = Column(BigInteger, nullable=False)


class UfhSystemSetting(Base):
    __tablename__ = 'ufh_system_setting'
    __table_args__ = {'comment': 'ϵͳ��������'}

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    login_page_background_image_url = Column(VARCHAR(500), nullable=False, server_default=text("''"), comment='����ͼƬ��ַ')
    side_bar_color = Column(VARCHAR(50), nullable=False, server_default=text("''"), comment='����Ŀ����ɫ')
    welcome_words = Column(VARCHAR(200), nullable=False, server_default=text("''"), comment='��ӭ��')
    background_of_dark_style = Column(VARCHAR(50), nullable=False, server_default=text("''"), comment='��ɫ����ı���ɫ')
    background_of_light_style = Column(VARCHAR(50), nullable=False, server_default=text("''"), comment='Ĭ�����ⱳ��ɫ')


class UserReport(Base):
    __tablename__ = 'user_report'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DateTime, nullable=False)
    updated_on = Column(DateTime, nullable=False)
    admin_id = Column(BigInteger)
    description = Column(VARCHAR(200), server_default=text("''"))
    report_content = Column(TEXT)
    report_name = Column(VARCHAR(100), server_default=text("''"))
    report_type = Column(VARCHAR(50), server_default=text("''"))
    table_report_config = Column(TEXT)


class YibaoColumnDefinition(Base):
    __tablename__ = 'yibao_column_definition'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    column_name = Column(VARCHAR(50), server_default=text("''"))
    column_type = Column(VARCHAR(50), server_default=text("''"))
    db_definition_id = Column(BigInteger)
    description = Column(VARCHAR(200), server_default=text("''"))
    table_definition_id = Column(BigInteger)


class YibaoColumnRelationShip(Base):
    __tablename__ = 'yibao_column_relation_ship'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    db_definition_id = Column(BigInteger)
    description = Column(VARCHAR(200), server_default=text("''"))
    from_column_id = Column(BigInteger)
    relation_type = Column(VARCHAR(20), server_default=text("''"))
    table_definition_id = Column(BigInteger)
    target_column_id = Column(BigInteger)


class YibaoDataExtractConfig(Base):
    __tablename__ = 'yibao_data_extract_config'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    extract_data_key = Column(VARCHAR(20), index=True, server_default=text("''"))
    extract_day = Column(VARCHAR(20), server_default=text("''"))
    extract_end_time = Column(VARCHAR(30), server_default=text("''"))
    increment_hours = Column(Integer)


class YibaoDataExtractLog(Base):
    __tablename__ = 'yibao_data_extract_log'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    data_size = Column(BigInteger)
    extract_data_key = Column(VARCHAR(100), index=True, server_default=text("''"))
    extract_data_time = Column(VARCHAR(30), server_default=text("''"))
    extract_end_time = Column(VARCHAR(30), server_default=text("''"))
    extract_start_time = Column(VARCHAR(30), server_default=text("''"))
    extract_scripts = Column(TEXT)


class YibaoDbDefinition(Base):
    __tablename__ = 'yibao_db_definition'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    db_name = Column(VARCHAR(50), unique=True, server_default=text("''"))
    description = Column(VARCHAR(200), server_default=text("''"))


class YibaoJobConfiguration(Base):
    __tablename__ = 'yibao_job_configuration'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    cron_expressions = Column(VARCHAR(200), server_default=text("''"))
    job_name = Column(VARCHAR(100), server_default=text("''"))
    rule_key = Column(VARCHAR(100), unique=True, server_default=text("''"))
    scripts = Column(TEXT)
    status = Column(Integer, server_default=text("'0'"))
    type = Column(VARCHAR(100), server_default=text("''"))


class YibaoModelRelationShip(Base):
    __tablename__ = 'yibao_model_relation_ship'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    algorithm_id = Column(BigInteger)
    column_id = Column(BigInteger)
    data_set_id = Column(BigInteger)
    from_id = Column(BigInteger)
    from_type = Column(VARCHAR(50), server_default=text("''"))
    indicator_id = Column(BigInteger)


class YibaoTableDefinition(Base):
    __tablename__ = 'yibao_table_definition'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    db_definition_id = Column(BigInteger)
    description = Column(VARCHAR(200), server_default=text("''"))
    table_name = Column(VARCHAR(50), server_default=text("''"))


class IndexRobotTarget(Base):
    __tablename__ = 'index_robot_target'
    __table_args__ = (
        Index('IDX_YZ', 'table_id', 'target_type', 'column_id'),
    )

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    data_cache_time = Column(VARCHAR(10), comment='���ݻ���ʱ�䣬������0���ʵʱ����')
    column_id = Column(BigInteger)
    column_name = Column(VARCHAR(255))
    compare_logic_id = Column(BigInteger)
    compare_type = Column(Integer)
    database_id = Column(BigInteger)
    date_group_type = Column(VARCHAR(20), comment='ʱ��ά�ȷ�������')
    default_date_column = Column(VARCHAR(50), comment='Ĭ��ʱ���ֶ�')
    default_time_period = Column(VARCHAR(20), comment='Ĭ��ʱ������')
    target_frequency = Column(VARCHAR(20))
    logic_id = Column(BigInteger, index=True)
    need_distinct = Column(VARCHAR(10), comment='N����Ҫȥ�أ�Y��Ҫȥ��')
    parent_id = Column(BigInteger, index=True)
    table_id = Column(BigInteger)
    table_name = Column(VARCHAR(255))
    target_define = Column(VARCHAR(255))
    target_formula = Column(VARCHAR(255))
    target_name = Column(VARCHAR(255))
    target_number = Column(VARCHAR(255))
    target_type = Column(Integer)
    unit_of_target = Column(VARCHAR(10), server_default=text("''"))
    category_id = Column(ForeignKey('index_target_category.id'), index=True)

    category = relationship('IndexTargetCategory')
