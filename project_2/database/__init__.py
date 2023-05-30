
import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

# Подключение к базе данных
try:

    engine = _sql.create_engine("postgresql://admin2:root2@localhost:5433/postgres")
    SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = _declarative.declarative_base()
    Base.metadata.create_all(bind=engine)

except _sql.exc.OperationalError as e:
    print(str(e), "ОШИБКА ПОДКЛЮЧЕНИЯ К БАЗЕ ДАННЫХ")