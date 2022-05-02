from app import app
from utils.database import db

# from models.models import Products
from flask_marshmallow import Marshmallow

# Initialize Marshmallow
ma = Marshmallow(app)


def _fk_pragma_on_connect(dbapi_con, con_record):  # noqa
    dbapi_con.execute('pragma foreign_keys=ON')


with app.app_context():
    # Enforce FK constraint for SQLite with when using flask-sqlalchemy
    from sqlalchemy import event
    event.listen(db.engine, 'connect', _fk_pragma_on_connect)
    db.session.execute('pragma foreign_keys=on')

    # clean database
    # db.drop_all()
    # create database
    db.create_all()

    # db.session.execute('insert into product_component(product_id, component_id) values(15, 20)')
    # products = Products.query.filter().all()


if __name__ == "__main__":
    # debug=True permite no tener que reiniciar el servidor
    app.run(debug=True)
