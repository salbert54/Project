from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields
from models.models import ProductComponent
ma = Marshmallow()

class ProductsSchema(ma.Schema):
    """
    Product
    """
    id = fields.Int(dump_only=True)
    name = fields.Str()
    description = fields.Str()
    reference_code = fields.Str()
        
class ComponentsSchema(ma.Schema):
    """
    Component
    """
    id = fields.Int(dump_only=True)
    name = fields.Str()
    description = fields.Str()
    irritating = fields.Bool()
        
class ProductComponentSchema(ma.Schema):
    """
    ProductComponent
    """
    class Meta:
        fields = (
        'product_id', 
        'component_id'
        )
        
class ProductComponentFullListSchema(ma.Schema):
    """
    ProductComponent
    """
    products = fields.Nested(ProductsSchema)
    components = fields.Nested(ComponentsSchema)
    
    # product_id = fields.Int(dump_only=True)
    # product_name = fields.Str()
    # product_description = fields.Str()
    # product_reference_code = fields.Str()
    # component_id = fields.Int(dump_only=True)
    # component_name = fields.Str()
    # component_description = fields.Str()
    # component_irritating = fields.Bool()
    