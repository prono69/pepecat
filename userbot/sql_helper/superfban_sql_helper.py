from sqlalchemy import Column, String

from . import BASE, SESSION


class Superfban(BASE):
    __tablename__ = "superfban"
    chat_id = Column(String(14), primary_key=True)
    reason = Column(String(127))

    def __init__(self, chat_id, reason=""):
        self.chat_id = chat_id
        self.reason = reason


GBan.__table__.create(checkfirst=True)


def is_gbanned(chat_id):
    try:
        return SESSION.query(Superfban).filter(Superfban.chat_id == str(chat_id)).one()
    except BaseException:
        return None
    finally:
        SESSION.close()


def get_superfbanuser(chat_id):
    try:
        return SESSION.query(Superfban).get(str(chat_id))
    finally:
        SESSION.close()


def catsuperfban(chat_id, reason):
    adder = Superfban(str(chat_id), str(reason))
    SESSION.add(adder)
    SESSION.commit()


def catunsuperfban(chat_id):
    if rem := SESSION.query(Superfban).get(str(chat_id)):
        SESSION.delete(rem)
        SESSION.commit()


def get_all_superfbanned():
    rem = SESSION.query(Superfban).all()
    SESSION.close()
    return rem
