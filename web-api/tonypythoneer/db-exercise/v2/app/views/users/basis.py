#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160202
#  @date          20160202
#  @version       0.0
"""basis for Users API
"""
from flask.views import MethodView

from flask.ext.login import current_user, login_required

from webargs.flaskparser import use_args

from . import users_bp
from ..mixins import RestfulViewMixin
from ...models.users import User
from ...schemas.users import ProfileUpdateSchema
from ...serializers.users import UserSerializer


class UserDetailView(RestfulViewMixin, MethodView):
    model = User
    serializer_class = UserSerializer

    def get(self, id):
        user = self.get_object(id)
        serializer = self.get_serializer()
        data = serializer.dump(user).data
        return self.get_response(data={"data": data}, status=200)

    '''
    @use_args(UserDetailUpdateSchema, locations=('json',))
    def put(self, args, id):
        user = self.get_object(id)
        user.nickname = args.get('nickname', user.nickname)
        user.update()
        return self.get_response(status=200)

    def delete(self, id):
        user = self.get_object(id)
        user.delete()
        return self.get_response(status=204)
    '''


class AboutMeView(RestfulViewMixin, MethodView):
    serializer_class = UserSerializer
    decorators = (login_required,)

    def get(self):
        user = current_user
        serializer = self.get_serializer()
        data = serializer.dump(user).data
        return self.get_response(data={"data": data}, status=200)

    @use_args(ProfileUpdateSchema, locations=('json',))
    def put(self, args):
        user = current_user
        user.nickname = args.get('nickname', user.nickname)
        user.update()
        return self.get_response(status=200)

    def delete(self):
        user = current_user
        user.delete()
        return self.get_response(status=204)


# Url patterns: To register views in blueprint
users_bp.add_url_rule('/<int:id>', view_func=UserDetailView.as_view('user-detail'))
users_bp.add_url_rule('/me', view_func=AboutMeView.as_view('about-me'))