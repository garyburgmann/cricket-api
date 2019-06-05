from marshmallow import Schema, fields, EXCLUDE


class UserSchema(Schema):
    uuid = fields.UUID(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    class Meta:
        unknown = EXCLUDE
