from sqlalchemy import BigInteger, Column, DECIMAL, DateTime, Float, ForeignKeyConstraint, Index, Integer, Table, text
from sqlalchemy.dialects.mysql import BIT, DATETIME, MEDIUMTEXT, TEXT, TINYINT, VARCHAR
from sqlalchemy.orm import declarative_base, relationship

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


class AdminTargets(Base):
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
    __table_args__ = (
        Index('UK_srawygbb37bm58crwr8ely1ap', 'db_key', unique=True),
    )

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    app_id = Column(VARCHAR(100), server_default=text("''"))
    connection_model = Column(VARCHAR(200), server_default=text("''"))
    connection_model_value = Column(VARCHAR(500), server_default=text("''"))
    customization = Column(VARCHAR(500), server_default=text("''"))
    db_key = Column(VARCHAR(200), server_default=text("''"))
    db_host = Column(VARCHAR(200), server_default=text("''"))
    name = Column(VARCHAR(200), server_default=text("''"))
    db_password = Column(VARCHAR(200), server_default=text("''"))
    db_port = Column(Integer)
    type = Column(VARCHAR(100), server_default=text("''"))
    db_user_name = Column(VARCHAR(100), server_default=text("''"))


class AiSystemConfig(Base):
    __tablename__ = 'ai_system_config'
    __table_args__ = (
        Index('UK_8blktyim4ymnqocs66hi3imo6', 'config_key', unique=True),
    )

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    config_json = Column(VARCHAR(2000), server_default=text("''"))
    config_key = Column(VARCHAR(100), server_default=text("''"))


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
    __table_args__ = (
        Index('UK_3f9g381oysacuxa8wkb3akrym', 'db_key', unique=True),
    )

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    db_key = Column(VARCHAR(100), server_default=text("''"))
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

    id = Column(BigInteger, primary_key=True, comment='主键')
    created_on = Column(DATETIME(fsp=6), nullable=False, comment='创建时间')
    updated_on = Column(DATETIME(fsp=6), nullable=False, comment='更新时间')
    is_satisfied = Column(Integer, comment='是否满意')
    is_success = Column(Integer, comment='是否成功')
    participle = Column(VARCHAR(255), comment='模型处理分词结果')
    text_ = Column('text', VARCHAR(255), comment='对话输入内容')
    is_rebuild = Column(Integer, comment='是否重新生成')
    rebuild_count = Column(Integer, comment='重新生成次数')
    target_json = Column(VARCHAR(1000), comment='指标列表(json)')


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
        Index('idx_report_id', 'report_id'),
        Index('idx_user_id', 'user_id')
    )

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    ower_type = Column(VARCHAR(255), comment='拥有者类型:OWNER,SHARED')
    permission_type = Column(VARCHAR(255), comment='权限类型:READONLY,WRITER')
    report_id = Column(BigInteger)
    report_name = Column(VARCHAR(255), comment='报告名称')
    user_id = Column(BigInteger)


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
    column_id = Column(BigInteger, comment='字段id')
    column_name = Column(VARCHAR(255), comment='字段名称')
    combination_target_logic_id = Column(BigInteger, comment='组合指标逻辑id')
    database_id = Column(BigInteger, comment='数据库连接id')
    refer_target_name = Column(VARCHAR(255), comment='目标指标名称')
    referer_target_logic_id = Column(BigInteger, comment='引用指标逻辑id')
    schema_id = Column(BigInteger, comment='数据库id')
    schema_name = Column(VARCHAR(255), comment='数据库名称')
    table_id = Column(BigInteger, comment='表id')
    table_name = Column(VARCHAR(255), comment='表名')


class CombinationVisualDimensionReferInfo(Base):
    __tablename__ = 'combination_visual_dimension_refer_info'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    column_id = Column(BigInteger, comment='字段id')
    column_name = Column(VARCHAR(255), comment='字段名称')
    combination_target_logic_id = Column(BigInteger, comment='组合指标逻辑id')
    combination_target_name = Column(VARCHAR(255), comment='目标指标名称')
    database_id = Column(BigInteger, comment='数据库连接id')
    schema_id = Column(BigInteger, comment='数据库id')
    schema_name = Column(VARCHAR(255), comment='数据库名称')
    table_id = Column(BigInteger, comment='表id')
    table_name = Column(VARCHAR(255), comment='表名')
    visual_dimension_id = Column(BigInteger, comment='虚拟维度id')
    visual_dimension_name = Column(VARCHAR(255), comment='虚拟维度名称')
    visual_column_id = Column(BigInteger, comment='虚拟字段id')


class CustomerAccount(Base):
    __tablename__ = 'customer_account'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    user_name = Column(VARCHAR(50))
    work_no = Column(VARCHAR(50))


class CustomerDepartment(Base):
    __tablename__ = 'customer_department'
    __table_args__ = (
        Index('UK_iu8dsd1exmgrtny1mc0smt0jj', 'department_code', unique=True),
    )

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    department_code = Column(VARCHAR(50))
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
    database_id = Column(BigInteger, nullable=False)
    qyzt = Column(Integer, nullable=False)
    cron = Column(VARCHAR(255))
    database_name = Column(VARCHAR(255))
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
    department_id = Column(BigInteger, nullable=False)
    data_access_strategy_name = Column(VARCHAR(200), server_default=text("''"))


class DepartmentTargets(Base):
    __tablename__ = 'department_targets'
    __table_args__ = (
        Index('UKpiudioomf2qxgrab5tlx2cwy9', 'department_id', 'target_id', unique=True),
    )

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    department_id = Column(BigInteger, nullable=False)
    target_id = Column(BigInteger, nullable=False)
    department_name = Column(VARCHAR(100), server_default=text("''"))
    table_name = Column(VARCHAR(100), server_default=text("''"))
    target_name = Column(VARCHAR(200), server_default=text("''"))


class DictionaryData(Base):
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
    __table_args__ = {'comment': '部门表'}

    id = Column(BigInteger, primary_key=True, comment='部门表主键')
    created_on = Column(DATETIME(fsp=6), nullable=False, comment='创建时间')
    updated_on = Column(DATETIME(fsp=6), nullable=False, comment='更新时间')
    dept_no = Column(VARCHAR(50), comment='部门编号')
    dept_name = Column(VARCHAR(255), comment='部门名称')
    parent_no = Column(VARCHAR(50), comment='上级编号')


t_draw_prize = Table(
    'draw_prize', metadata,
    Column('id', BigInteger, comment='奖品表主键'),
    Column('prize_name', VARCHAR(255), comment='奖品名'),
    Column('prize_price', DECIMAL(10, 2), comment='奖品价值'),
    Column('prize_lv', VARCHAR(50), comment='奖品等级'),
    Column('prize_count', Integer, comment='奖品数量'),
    Column('created_on', DATETIME(fsp=6), nullable=False, comment='创建时间'),
    Column('updated_on', DATETIME(fsp=6), nullable=False, comment='更新时间'),
    comment='奖品表'
)


class DrawRecord(Base):
    __tablename__ = 'draw_record'

    id = Column(BigInteger, primary_key=True, comment='抽奖记录id')
    created_on = Column(DATETIME(fsp=6), nullable=False, comment='创建时间')
    updated_on = Column(DATETIME(fsp=6), nullable=False, comment='更新时间')
    user_no = Column(VARCHAR(50), comment='用户编号')
    user_name = Column(VARCHAR(255), comment='用户姓名')
    dept_no = Column(VARCHAR(50), comment='部门编号')
    dept_name = Column(VARCHAR(255), comment='部门名称')
    prize_name = Column(VARCHAR(255), comment='奖品名称')
    prize_price = Column(DECIMAL(10, 2), comment='奖品价值')
    prize_count = Column(Integer, comment='中奖数量')
    prize_lv = Column(VARCHAR(255), comment='奖品等级')


class DrawUser(Base):
    __tablename__ = 'draw_user'
    __table_args__ = {'comment': '用户表'}

    id = Column(BigInteger, primary_key=True, comment='用户表主键')
    created_on = Column(DATETIME(fsp=6), nullable=False, comment='创建时间')
    updated_on = Column(DATETIME(fsp=6), nullable=False, comment='更新时间')
    user_no = Column(VARCHAR(50), comment='用户工号')
    user_name = Column(VARCHAR(255), comment='用户姓名')
    gend = Column(VARCHAR(2), comment='性别')
    dept_no = Column(VARCHAR(50), comment='部门编号')


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
    access_type = Column(VARCHAR(20), comment='访问类型')
    strategy_define = Column(TEXT, comment='策略内容')
    strategy_desc = Column(VARCHAR(255), comment='策略描述')
    strategy_name = Column(VARCHAR(120), comment='策略名称')
    strategy_script = Column(TEXT, comment='策略执行脚本')
    strategy_type = Column(VARCHAR(20), comment='策略类型')
    strategy_version = Column(VARCHAR(120), comment='策略版本')


class IndexDataAccessStrategyDetail(Base):
    __tablename__ = 'index_data_access_strategy_detail'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    column_id = Column(BigInteger)
    database_id = Column(BigInteger)
    limited_values = Column(TEXT, comment='限制值')
    schema_id = Column(BigInteger)
    strategy_id = Column(BigInteger, comment='策略ID')
    table_id = Column(BigInteger)
    value_source = Column(VARCHAR(255))


class IndexDataDictionary(Base):
    __tablename__ = 'index_data_dictionary'
    __table_args__ = (
        Index('IDX_COLUMN', 'column_id'),
    )

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    column_id = Column(BigInteger)
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
    condition_group_code = Column(VARCHAR(100), server_default=text("'分组编码'"))
    condition_name = Column(VARCHAR(100), server_default=text("'条件名'"))
    logic_name = Column(VARCHAR(100), server_default=text("'逻辑名称'"))
    parent_condition_group_code = Column(VARCHAR(100), server_default=text("'父级分组编码'"))
    refer_column_id = Column(BigInteger)
    refer_column_name = Column(VARCHAR(100), server_default=text("'关联的字段名称'"))
    relation = Column(VARCHAR(500), server_default=text("'关系'"))
    sql_expressions = Column(TEXT)
    value = Column(VARCHAR(500), server_default=text("'条件值'"))


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
    __table_args__ = (
        Index('IDX_TARGETID', 'target_id'),
    )

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    column_id = Column(BigInteger)
    column_name = Column(VARCHAR(255))
    condition_group_code = Column(VARCHAR(100), server_default=text("'分组编码'"))
    condition_name = Column(VARCHAR(255))
    logic_name = Column(VARCHAR(100), server_default=text("'逻辑名称'"))
    parent_condition_group_code = Column(VARCHAR(100), server_default=text("'父级分组编码'"))
    relation = Column(VARCHAR(255))
    sql_expressions = Column(TEXT)
    target_id = Column(BigInteger)
    value = Column(VARCHAR(255))


class IndexRobotDatabase(Base):
    __tablename__ = 'index_robot_database'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    name = Column(VARCHAR(200), comment='数据库连接名')
    password = Column(VARCHAR(100), comment='数据库连接密码')
    port = Column(VARCHAR(50), comment='数据库端口')
    space = Column(VARCHAR(100), comment='空间地址')
    status = Column(Integer, comment='状态')
    type = Column(VARCHAR(50), comment='数据库类型')
    url = Column(VARCHAR(100), comment='数据库ip地址')
    username = Column(VARCHAR(100), comment='数据库连接用户名')


class IndexRobotDimension(Base):
    __tablename__ = 'index_robot_dimension'
    __table_args__ = (
        Index('IDX_TARGETID', 'target_id'),
    )

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    data_type = Column(Integer, nullable=False)
    dimension_type = Column(Integer, nullable=False)
    status = Column(Integer, nullable=False)
    column_id = Column(BigInteger)
    column_name = Column(VARCHAR(255))
    default_date_dimension = Column(VARCHAR(10), server_default=text("'N'"), comment='默认日期维度')
    dimension_name = Column(VARCHAR(255))
    table_id = Column(BigInteger)
    table_name = Column(VARCHAR(255))
    target_id = Column(BigInteger)
    zh_target_id = Column(BigInteger)


class IndexRobotLabel(Base):
    __tablename__ = 'index_robot_label'
    __table_args__ = (
        Index('IDX_RELATION', 'logic_id'),
    )

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    label_describe = Column(VARCHAR(255))
    label_name = Column(VARCHAR(255))
    logic_id = Column(BigInteger)
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
    join_type = Column(VARCHAR(100), server_default=text("''"), comment='连接类型')
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
    db_type = Column(VARCHAR(255), comment='数据库类型')
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
    need_distinct = Column(VARCHAR(10), comment='N不需要去重，Y需要去重')
    qyzt = Column(Integer)
    schema_id = Column(BigInteger)
    schema_name = Column(VARCHAR(255))
    stop_remark = Column(Integer)
    table_name = Column(VARCHAR(255))
    yuliu2 = Column(VARCHAR(255))


class IndexRobotTargetDetail(Base):
    __tablename__ = 'index_robot_target_detail'
    __table_args__ = (
        Index('UK_b88fa9muwj60q9ufvq3a29jbo', 'target_logic_id', unique=True),
    )

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    target_define = Column(TEXT)
    target_logic_id = Column(BigInteger)


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
    __table_args__ = (
        ForeignKeyConstraint(['parent_id'], ['index_target_category.id'], name='FK6mftxee0it5t8xni013hj010g'),
        Index('FK6mftxee0it5t8xni013hj010g', 'parent_id')
    )

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    category_comment = Column(VARCHAR(255), server_default=text("''"), comment='指标分类备注')
    category_name = Column(VARCHAR(255), server_default=text("''"), comment='指标分类名称')
    parent_id = Column(BigInteger)

    parent = relationship('IndexTargetCategory', remote_side=[id], back_populates='parent_reverse')
    parent_reverse = relationship('IndexTargetCategory', remote_side=[parent_id], back_populates='parent')
    index_robot_target = relationship('IndexRobotTarget', back_populates='category')


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
    status = Column(Integer, nullable=False)
    batch_date = Column(DATETIME(fsp=6))
    database_id = Column(BigInteger)
    doing_now = Column(VARCHAR(255))
    event = Column(Integer)
    log_date = Column(DATETIME(fsp=6))


class NorthStartTargetRelation(Base):
    __tablename__ = 'north_start_target_relation'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    column_id = Column(BigInteger, nullable=False)
    business_domain_id = Column(BigInteger)
    dimension_id = Column(BigInteger, comment='默认时间维度ID')
    period_type_name = Column(VARCHAR(255), comment='指标展示时候默认时间周期')
    target_id = Column(BigInteger)


class PermissionStrategy(Base):
    __tablename__ = 'permission_strategy'
    __table_args__ = (
        Index('UK_4hfxbcheu150k96h7h9vh4sc0', 'strategy_code', unique=True),
    )

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    strategy_code = Column(VARCHAR(50), server_default=text("''"))
    strategy_name = Column(VARCHAR(100), server_default=text("''"))


class RecommendQuestion(Base):
    __tablename__ = 'recommend_question'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    question = Column(VARCHAR(255), comment='问题')
    question_type = Column(VARCHAR(50), comment='问题类型')


class SqlResultDto(Base):
    __tablename__ = 'sql_result_dto'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    group_field = Column(VARCHAR(255))
    sum = Column(VARCHAR(255))


class SysCaliber(Base):
    __tablename__ = 'sys_caliber'
    __table_args__ = (
        Index('IDX_caliber', 'caliber'),
        Index('IDX_effective_date', 'effective_date')
    )

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    caliber = Column(VARCHAR(20), server_default=text("''"))
    effective_date = Column(VARCHAR(20), server_default=text("''"))
    value = Column(VARCHAR(200), server_default=text("''"))


class SysConfigCommonParameterType(Base):
    __tablename__ = 'sys_config_common_parameter_type'
    __table_args__ = {'comment': '参数类型表'}

    id = Column(VARCHAR(36), primary_key=True, server_default=text("''"), comment='主键')
    code = Column(VARCHAR(255), server_default=text("''"), comment='code')
    match_rule = Column(VARCHAR(255), server_default=text("''"), comment='匹配规则')
    name = Column(VARCHAR(255), server_default=text("''"), comment='名称')
    type = Column(VARCHAR(255), server_default=text("''"), comment='类型')


class SysConfigParameterType(Base):
    __tablename__ = 'sys_config_parameter_type'
    __table_args__ = {'comment': '参数类型表'}

    id = Column(VARCHAR(36), primary_key=True, server_default=text("''"), comment='主键')
    application_id = Column(VARCHAR(255), server_default=text("''"), comment='应用id')
    code = Column(VARCHAR(255), server_default=text("''"), comment='code')
    match_rule = Column(VARCHAR(255), server_default=text("''"), comment='匹配规则')
    name = Column(VARCHAR(255), server_default=text("''"), comment='名称')
    type = Column(VARCHAR(255), server_default=text("''"), comment='类型')


class SysDisease(Base):
    __tablename__ = 'sys_disease'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    code = Column(VARCHAR(255), server_default=text("''"), comment='疾病编码')
    name = Column(VARCHAR(255), server_default=text("''"), comment='名称')
    parent_code = Column(VARCHAR(255), server_default=text("''"), comment='上级编码')


class SysJixiao(Base):
    __tablename__ = 'sys_jixiao'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    compute_method = Column(VARCHAR(255), server_default=text("''"), comment='计算方式')
    index_definition = Column(VARCHAR(255), server_default=text("''"), comment='指标定义')
    index_desc = Column(VARCHAR(255), server_default=text("''"), comment='指标说明')
    index_name = Column(VARCHAR(255), server_default=text("''"), comment='指标名称')
    index_orientation = Column(VARCHAR(255), server_default=text("''"), comment='指标导向')
    index_property = Column(VARCHAR(255), server_default=text("''"), comment='指标属性')
    one = Column(VARCHAR(255), server_default=text("''"), comment='一级')
    two = Column(VARCHAR(255), server_default=text("''"), comment='二级')
    unit = Column(VARCHAR(255), server_default=text("''"), comment='计量单位')


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
    function_category = Column(VARCHAR(255), comment='函数类别')
    function_desc = Column(VARCHAR(255), comment='函数描述')
    function_expression = Column(VARCHAR(255), comment='函数表达式')
    function_name = Column(VARCHAR(255), comment='函数名称')


class UfhAdmin(Base):
    __tablename__ = 'ufh_admin'
    __table_args__ = (
        Index('UK_rwj621eacignp2n7pvcylskcv', 'login_name', unique=True),
    )

    id = Column(BigInteger, primary_key=True, comment='主键')
    login_name = Column(VARCHAR(50), nullable=False, comment='登录id')
    password = Column(VARCHAR(255), nullable=False, comment='登录密码')
    is_auto_authorization = Column(Integer, nullable=False)
    created_on = Column(DATETIME(fsp=6), comment='创建时间')
    updated_on = Column(DATETIME(fsp=6), comment='更新时间')
    bu_code = Column(TEXT, comment='部门编码')
    facility = Column(VARCHAR(500), server_default=text("''"), comment='facility编码')
    market = Column(VARCHAR(500), server_default=text("''"), comment='市场编码')
    status = Column(Integer, comment='账户状态')
    comment = Column(VARCHAR(255), server_default=text("''"), comment='备注')
    format_bu_code = Column(TEXT, comment='bucode格式化，用于交互')
    hq = Column(VARCHAR(255), server_default=text("''"), comment='hq')
    real_name = Column(VARCHAR(50), server_default=text("''"))
    channel = Column(VARCHAR(50), server_default=text("''"))
    auth_user_id = Column(VARCHAR(50), server_default=text("''"))
    email = Column(VARCHAR(100), server_default=text("''"))


class UfhAdminApplicationResourceDataPermissions(Base):
    __tablename__ = 'ufh_admin_application_resource_data_permissions'
    __table_args__ = {'comment': '用户特殊的数据权限'}

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    admin_id = Column(BigInteger, nullable=False, comment='管理员id')
    bu_code = Column(VARCHAR(255), nullable=False, comment='所属bu')
    facility = Column(VARCHAR(255), nullable=False, comment='所属facility')
    market = Column(VARCHAR(255), nullable=False, comment='所属market')
    resource_id = Column(BigInteger, nullable=False, comment='关联的应用id')


class UfhAdminMetadata(Base):
    __tablename__ = 'ufh_admin_metadata'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    admin_id = Column(BigInteger, nullable=False)
    metadata_id = Column(BigInteger, nullable=False)
    metadata_type = Column(Integer, nullable=False)


class UfhAdminResourcePermissions(Base):
    __tablename__ = 'ufh_admin_resource_permissions'
    __table_args__ = {'comment': '管理员用户和资源关系、权限'}

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    admin_id = Column(BigInteger, nullable=False, comment='管理员账户id')
    permissions = Column(VARCHAR(400), nullable=False, comment='资源的操作权限：create\\update等')
    resource_id = Column(BigInteger, nullable=False, comment='资源id')
    status = Column(Integer, nullable=False)


class UfhAdminRole(Base):
    __tablename__ = 'ufh_admin_role'
    __table_args__ = {'comment': '管理员角色关系'}

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    admin_id = Column(BigInteger, nullable=False, comment='管理员id')
    role_id = Column(BigInteger, nullable=False, comment='角色id')


class UfhAdminTimeDictionaryCondition(Base):
    __tablename__ = 'ufh_admin_time_dictionary_condition'
    __table_args__ = (
        Index('IDX_DICCON_ADMIN_ID', 'admin_id'),
        Index('IDX_DICCON_COLUMN_ID', 'column_id')
    )

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    admin_id = Column(BigInteger, nullable=False, comment='用户id')
    column_id = Column(BigInteger, nullable=False, comment='字段id')
    logical_operator = Column(VARCHAR(255), nullable=False, comment='存储的值')
    operator = Column(VARCHAR(255), nullable=False, comment='条件')
    value = Column(VARCHAR(255), nullable=False, comment='存储的值')
    condition_order = Column(Integer, server_default=text("'0'"), comment='条件顺序')


class UfhApplicationResourceDataPermissions(Base):
    __tablename__ = 'ufh_application_resource_data_permissions'
    __table_args__ = (
        Index('UK1dlt52rm3sf510v9f02lm4qlp', 'resource_id', unique=True),
        Index('UK3rsb16g9876jikbti1rer8hre', 'application_id', 'resource_id', unique=True),
        Index('UKahatpk9vfr6cdwcahngsc4nao', 'resource_id', unique=True),
        {'comment': '资源的数据权限配置'}
    )

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    bu_field = Column(VARCHAR(255), nullable=False, comment='允许的BU')
    facility_field = Column(VARCHAR(255), nullable=False, comment='允许的facility')
    market_field = Column(VARCHAR(255), nullable=False, comment='允许的market')
    resource_id = Column(BigInteger, nullable=False, comment='资源id')
    use_bucode = Column(BIT(1), nullable=False, comment='是否使用bu过滤')
    use_facility = Column(BIT(1), nullable=False, comment='是否使用facility过滤')
    use_market = Column(BIT(1), nullable=False, comment='是否使用market过滤')
    application_id = Column(BigInteger, nullable=False, comment='资源所属应用id')


class UfhCustomer(Base):
    __tablename__ = 'ufh_customer'
    __table_args__ = (
        Index('IDX_CUSTOMER_MRN', 'mrn'),
        {'comment': '废弃的表，可忽略'}
    )

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
    mrn = Column(VARCHAR(50), nullable=False, server_default=text("''"))
    nationality = Column(VARCHAR(50), nullable=False, server_default=text("''"))
    nationality_id = Column(VARCHAR(10), nullable=False, server_default=text("''"))
    preferable_language = Column(VARCHAR(50), nullable=False, server_default=text("''"))


class UfhDepartment(Base):
    __tablename__ = 'ufh_department'
    __table_args__ = (
        Index('UK_b2lpudrgowqo8gy9xdaa0y447', 'department_code', unique=True),
        Index('UK_ha6n36tusrwjwgyxhdfxgl8ne', 'department_name', unique=True)
    )

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    department_name = Column(VARCHAR(50), nullable=False)
    parent_id = Column(BigInteger, nullable=False)
    department_code = Column(VARCHAR(50))


class UfhResourceNoSequence(Base):
    __tablename__ = 'ufh_resource_no_sequence'
    __table_args__ = (
        Index('IDX_TEMPLATE_SEQUENCE', 'sequence_day'),
        Index('UK_o7q7umvjxa5oqko1urdowrc3v', 'sequence_format_value', unique=True),
        {'comment': '资源编号生成sequence'}
    )

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    has_used = Column(BIT(1), nullable=False, comment='是否使用')
    sequence_value = Column(Integer, nullable=False, comment='format前的值')
    code_type = Column(VARCHAR(20), server_default=text("''"), comment=' 编号类型')
    sequence_day = Column(VARCHAR(20), server_default=text("''"), comment='编号所属日期')
    sequence_format_value = Column(VARCHAR(30), server_default=text("''"), comment='format后的编号值')


class UfhRoleMetadata(Base):
    __tablename__ = 'ufh_role_metadata'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    metadata_id = Column(BigInteger, nullable=False)
    metadata_type = Column(Integer, nullable=False)
    role_id = Column(BigInteger, nullable=False)


class UfhRoleTimeDictionaryCondition(Base):
    __tablename__ = 'ufh_role_time_dictionary_condition'
    __table_args__ = {'comment': '角色和时间字段条件的关系表'}

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    role_id = Column(BigInteger, nullable=False, comment='角色id')
    column_id = Column(BigInteger, nullable=False, comment='字段id')
    operator = Column(VARCHAR(255), nullable=False, comment='条件')
    value = Column(VARCHAR(255), nullable=False, comment='存储的值')
    logical_operator = Column(VARCHAR(3), nullable=False, comment='逻辑运算符')
    condition_order = Column(Integer, server_default=text("'0'"), comment='条件顺序')


class UfhSystemDataHierarchy(Base):
    __tablename__ = 'ufh_system_data_hierarchy'
    __table_args__ = {'comment': 'Ufh的组织结构关系'}

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    bu_code = Column(VARCHAR(100), nullable=False, comment='bu编码')
    hq = Column(VARCHAR(100), nullable=False, comment='hq')
    market_or_facility = Column(VARCHAR(100), nullable=False)
    market_or_facility_type = Column(VARCHAR(255), nullable=False)


class UfhSystemFormFilter(Base):
    __tablename__ = 'ufh_system_form_filter'
    __table_args__ = (
        Index('UK9pwuf8fjqw0q5mmi6pplwqb39', 'reference_table', 'filter_key', unique=True),
        Index('UKmo7yq81wuj7hdgbd59wx38flb', 'reference_table', 'filter_key', unique=True),
        {'comment': '平台的过滤组件定义表'}
    )

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    filter_execution_type = Column(VARCHAR(50), nullable=False, server_default=text("''"), comment='组件的执行类型')
    filter_hint = Column(VARCHAR(50), nullable=False, server_default=text("''"), comment='组件的提示')
    filter_input_type = Column(VARCHAR(50), nullable=False, server_default=text("''"), comment='组件的输入类型')
    filter_key = Column(VARCHAR(50), nullable=False, server_default=text("''"), comment='组件关联的字段key')
    filter_label = Column(VARCHAR(50), nullable=False, server_default=text("''"), comment='组件的显示label')
    reference_table = Column(VARCHAR(50), nullable=False, server_default=text("''"), comment='关联的表')
    select_filter_values = Column(VARCHAR(200), nullable=False, server_default=text("''"), comment='是否筛选类型的组件')


class UfhSystemFunctionalResources(Base):
    __tablename__ = 'ufh_system_functional_resources'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    display_name = Column(VARCHAR(255), nullable=False, comment='显示名称')
    name = Column(VARCHAR(255), nullable=False, comment='资源功能名字')
    notes = Column(VARCHAR(255), nullable=False, comment='备注')
    path = Column(VARCHAR(255), nullable=False, server_default=text("''"), comment='资源功能路径')


class UfhSystemLog(Base):
    __tablename__ = 'ufh_system_log'
    __table_args__ = (
        Index('IDX_DATALOG_OPERATOR', 'oeprator'),
    )

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    action = Column(VARCHAR(50), server_default=text("''"))
    app_name = Column(VARCHAR(50), server_default=text("''"))
    content = Column(VARCHAR(500), server_default=text("''"))
    data_file_url = Column(VARCHAR(500), server_default=text("''"))
    has_file_url = Column(TINYINT(1), server_default=text("'0'"))
    ip = Column(VARCHAR(50), server_default=text("''"))
    oeprator = Column(VARCHAR(100), server_default=text("''"))
    oeprator_time = Column(VARCHAR(50), server_default=text("''"))
    path = Column(VARCHAR(200), server_default=text("''"))


class UfhSystemLogs(Base):
    __tablename__ = 'ufh_system_logs'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    ind_trace_id = Column(VARCHAR(100), nullable=False, server_default=text("''"), comment='唯一标识')
    log_type = Column(VARCHAR(100), nullable=False, server_default=text("''"), comment='类型')
    operator = Column(VARCHAR(100), nullable=False, server_default=text("''"), comment='操作人')
    request_method = Column(VARCHAR(200), nullable=False, server_default=text("''"), comment='请求方法')
    request_parameters = Column(VARCHAR(800), nullable=False, server_default=text("''"), comment='请求参数')
    request_url = Column(VARCHAR(300), nullable=False, server_default=text("''"), comment='请求地址')
    response_value = Column(MEDIUMTEXT, comment='响应结果')


class UfhSystemPermissions(Base):
    __tablename__ = 'ufh_system_permissions'
    __table_args__ = {'comment': '定义资源拥有的权限功能列表'}

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    concrete_resource_id = Column(BigInteger, nullable=False, comment='资源id')
    display_name = Column(VARCHAR(50), nullable=False, comment='显示名称')
    name = Column(VARCHAR(50), nullable=False, comment='功能')
    notes = Column(VARCHAR(100), nullable=False, comment='备注')


class UfhSystemResourceMeta(Base):
    __tablename__ = 'ufh_system_resource_meta'
    __table_args__ = {'comment': '资源关联的元数据'}

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    extension = Column(VARCHAR(255), nullable=False, comment='扩展内容')
    meta_type = Column(VARCHAR(50), nullable=False, comment='元数据类型')
    resource_id = Column(BigInteger, nullable=False, comment='关联资源id')
    value = Column(VARCHAR(100), nullable=False, comment='元数据值')


class UfhSystemResources(Base):
    __tablename__ = 'ufh_system_resources'

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    depth = Column(Integer, nullable=False, comment='系统资源深度')
    functional_resource_id = Column(BigInteger, nullable=False, server_default=text("'0'"), comment='关联的功能id')
    group_id = Column(Integer, nullable=False, server_default=text("'1'"), comment='所属组')
    icon = Column(VARCHAR(255), nullable=False, comment='资源的icon')
    internal_full_path = Column(VARCHAR(200), nullable=False, server_default=text("''"), comment='完整的路径用于逻辑处理')
    internal_uuid = Column(VARCHAR(32), nullable=False, server_default=text("''"), comment='资源的uuid')
    locked = Column(BIT(1), nullable=False, comment='是否被锁住')
    name = Column(VARCHAR(255), nullable=False, comment='资源名称')
    parent_id = Column(BigInteger, nullable=False, comment='资源的上一级id')
    path = Column(VARCHAR(500), nullable=False, comment='所属路径')
    resource_number = Column(VARCHAR(255), nullable=False, comment='资源编码')
    resource_type = Column(VARCHAR(255), nullable=False, comment='资源类型')
    settings = Column(VARCHAR(500), nullable=False, server_default=text("''"), comment='配置信息')
    sort_order = Column(Integer, nullable=False, comment='排序')
    status = Column(Integer, nullable=False, comment='状态')
    comment = Column(VARCHAR(200), server_default=text("''"), comment='备注')
    bu_column = Column(VARCHAR(30), server_default=text("''"), comment='关联的BU')
    facility_column = Column(VARCHAR(30), server_default=text("''"), comment='关联的facility')
    hq_column = Column(VARCHAR(30), server_default=text("''"), comment='hq')
    market_column = Column(VARCHAR(30), server_default=text("''"), comment='关联的market')
    title = Column(VARCHAR(50), server_default=text("''"), comment='资源标题')
    group_name = Column(VARCHAR(30), server_default=text("''"))


class UfhSystemRoleResource(Base):
    __tablename__ = 'ufh_system_role_resource'
    __table_args__ = {'comment': '资源和角色的关系'}

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    permissions = Column(VARCHAR(400), nullable=False, comment='权限信息')
    resource_id = Column(BigInteger, nullable=False, comment='资源的ID')
    role_id = Column(BigInteger, nullable=False, comment='角色ID')
    status = Column(Integer, nullable=False)


class UfhSystemRoles(Base):
    __tablename__ = 'ufh_system_roles'
    __table_args__ = {'comment': '系统角色表'}

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    display_name = Column(VARCHAR(50), nullable=False, comment='角色展示名称')
    name = Column(VARCHAR(50), nullable=False, comment='角色')
    notes = Column(VARCHAR(50), nullable=False, comment='备注')
    status = Column(Integer, nullable=False, comment='0:启动，1:禁用')
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
    __table_args__ = {'comment': '系统基础配置'}

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    login_page_background_image_url = Column(VARCHAR(500), nullable=False, server_default=text("''"), comment='背景图片地址')
    side_bar_color = Column(VARCHAR(50), nullable=False, server_default=text("''"), comment='边栏目背景色')
    welcome_words = Column(VARCHAR(200), nullable=False, server_default=text("''"), comment='欢迎词')
    background_of_dark_style = Column(VARCHAR(50), nullable=False, server_default=text("''"), comment='黑色主题的背景色')
    background_of_light_style = Column(VARCHAR(50), nullable=False, server_default=text("''"), comment='默认主题背景色')


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
    __table_args__ = (
        Index('IDX_DATA_EXTRACT_DATAKEY', 'extract_data_key'),
    )

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    extract_data_key = Column(VARCHAR(20), server_default=text("''"))
    extract_day = Column(VARCHAR(20), server_default=text("''"))
    extract_end_time = Column(VARCHAR(30), server_default=text("''"))
    increment_hours = Column(Integer)


class YibaoDataExtractLog(Base):
    __tablename__ = 'yibao_data_extract_log'
    __table_args__ = (
        Index('IDX_DATA_EXTRACT_LOG', 'extract_data_key'),
    )

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    data_size = Column(BigInteger)
    extract_data_key = Column(VARCHAR(100), server_default=text("''"))
    extract_data_time = Column(VARCHAR(30), server_default=text("''"))
    extract_end_time = Column(VARCHAR(30), server_default=text("''"))
    extract_start_time = Column(VARCHAR(30), server_default=text("''"))
    extract_scripts = Column(TEXT)


class YibaoDbDefinition(Base):
    __tablename__ = 'yibao_db_definition'
    __table_args__ = (
        Index('UK_87fwehhpjopap4kvy14kgy5g3', 'db_name', unique=True),
    )

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    db_name = Column(VARCHAR(50), server_default=text("''"))
    description = Column(VARCHAR(200), server_default=text("''"))


class YibaoJobConfiguration(Base):
    __tablename__ = 'yibao_job_configuration'
    __table_args__ = (
        Index('UK_py0r91a37vaejc8fs1ixa1exb', 'rule_key', unique=True),
    )

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    cron_expressions = Column(VARCHAR(200), server_default=text("''"))
    job_name = Column(VARCHAR(100), server_default=text("''"))
    rule_key = Column(VARCHAR(100), server_default=text("''"))
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
        ForeignKeyConstraint(['category_id'], ['index_target_category.id'], name='FK1x9phufc8eb3c75mmlrgvt41n'),
        Index('FK1x9phufc8eb3c75mmlrgvt41n', 'category_id'),
        Index('IDX_LOGIC_ID', 'logic_id'),
        Index('IDX_PARENTID', 'parent_id'),
        Index('IDX_YZ', 'table_id', 'target_type', 'column_id')
    )

    id = Column(BigInteger, primary_key=True)
    created_on = Column(DATETIME(fsp=6), nullable=False)
    updated_on = Column(DATETIME(fsp=6), nullable=False)
    data_cache_time = Column(VARCHAR(10), comment='数据缓存时间，或者是0则查实时数据')
    column_id = Column(BigInteger)
    column_name = Column(VARCHAR(255))
    compare_logic_id = Column(BigInteger)
    compare_type = Column(Integer)
    database_id = Column(BigInteger)
    date_group_type = Column(VARCHAR(20), comment='时间维度分组类型')
    default_date_column = Column(VARCHAR(50), comment='默认时间字段')
    default_time_period = Column(VARCHAR(20), comment='默认时间周期')
    target_frequency = Column(VARCHAR(20))
    logic_id = Column(BigInteger)
    need_distinct = Column(VARCHAR(10), comment='N不需要去重，Y需要去重')
    parent_id = Column(BigInteger)
    table_id = Column(BigInteger)
    table_name = Column(VARCHAR(255))
    target_define = Column(VARCHAR(255))
    target_formula = Column(VARCHAR(255))
    target_name = Column(VARCHAR(255))
    target_number = Column(VARCHAR(255))
    target_type = Column(Integer)
    unit_of_target = Column(VARCHAR(10), server_default=text("''"))
    category_id = Column(BigInteger)

    category = relationship('IndexTargetCategory', back_populates='index_robot_target')
