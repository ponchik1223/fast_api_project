import sqlalchemy as _sql

import database as _databsase

    
# модель данных для сохранения audio
class Audio(_databsase.Base):
    __tablename__ = "audio"
    id_audio = _sql.Column(_sql.String, primary_key=True, index=True)
    url_audio = _sql.Column(_sql.String, index=True)
    user_id = _sql.Column(_sql.String, index=True)
    token_access = _sql.Column(_sql.String, index=True)
    path_audio =_sql.Column(_sql.String, index=True)

# модель данных для сохранения contactc
class Contact(_databsase.Base):
    __tablename__ = "contacts"
    id_name = _sql.Column(_sql.String, primary_key=True, index=True)
    name = _sql.Column(_sql.String, index=True)
    token = _sql.Column(_sql.String,index=True, unique=True)
