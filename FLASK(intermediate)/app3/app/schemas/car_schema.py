from marshmallow import Schema, fields


class CarSchema(Schema):
    id = fields.Integer(dump_only=True)
    brand = fields.String(required=True)
    model = fields.String(required=True)
    price = fields.Float(required=True)
    color = fields.String(required=True)


class CarUpdateSchema(Schema):
    id = fields.Integer(required=True)
    brand = fields.String(required=True)
    model = fields.String(required=True)
    price = fields.Float(required=True)
    color = fields.String(required=True)


class ColorUpdateSchema(Schema):
    id = fields.Integer(requied=True)
    color = fields.String(required=True)


class ColorUpdateSchemaWithoutIdInBody(Schema):
    color = fields.String(required=True)


class CarQuerySchema(Schema):
    qry = fields.String(required=True)
    color = fields.String(required=False)
