from .. import ma
from ..models.users import User


class UserSerializer(ma.ModelSchema):
    class Meta:
        model = User
        load_only = ('password',)
