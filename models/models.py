from sqlalchemy import true
from utils.database import db
from datetime import datetime


class Products(db.Model):
    """
    Product Model
    """
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=true)
    description = db.Column(db.String(120), nullable=True)
    reference_code = db.Column(db.String(120), nullable=False, unique=true)
    product_fk = db.relationship("ProductComponent", back_populates="products")
    
    def __init__(self, name, description, reference_code):
        self.name = name
        self.description = description
        self.reference_code = reference_code
        
    def __repr__(self):
        return '<products %r>' % self.name
   
class Components(db.Model):
    """
    Components Model
    """
    __tablename__ = 'components'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=true)
    description = db.Column(db.String(120))
    irritating = db.Column(db.Boolean, default=False, nullable=False)
    component_fk = db.relationship("ProductComponent", back_populates="components")

    def __repr__(self):
        return '<components %r>' % self.name

    def __init__(self, name, description, irritating):
        self.name = name
        self.description = description
        self.irritating = irritating

class ProductComponent(db.Model):
    """
    Product Component Model
    """
    __tablename__ = 'product_component'
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), primary_key=True)
    component_id = db.Column(db.Integer, db.ForeignKey('components.id'), primary_key=True)
    
    components = db.relationship('Components');
    products = db.relationship('Products');
    # components = db.relationship("Components", backref="component_fk", lazy='dynamic')
    # products = db.relationship("Products", backref="product_fk", lazy='dynamic')
    
    

    def __repr__(self):
        return '<components %r>' % self.product_id

    def __init__(self, product_id, component_id):
        self.product_id = product_id
        self.component_id = component_id