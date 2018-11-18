#!/usr/bin/python3
# -*- coding: utf-8 -*-

class user_object(object):

    def __init__(self , connection , dbuser):
        pass


    def add_friend(self, user):

        pass

    def delete_friend(self, user):

        pass


    def get_all_friends(self):

        pass


    def get_friend_with_username(self , username):

        pass


    def get_friend_with_Id(self, friendId):

        pass



class user_model(object):

    def __init__(self):

        pass


    def add_new_online_user(self, user):
        """
        新增用户
        """
        pass

    def delete_user_because_offline(self, user):
        """用户下线以后，从在线中删除"""
        pass

    def get_user_by_connection(self, connection):
        """根据连接获取用户信息"""
        pass


    def get_user_exist_by_userId(self, userid):
        """根据用户id判断用户是否在线,并返回"""
        pass


    def get_user_exist_by_username(self, username):
        """根据用户名称判断用户是否在线,并返回，确保用户登录的唯一"""
        pass


    def delete_user_by_username(self, user):
        """根据好友，从用户列表中删除"""
        pass

    def reset(self):
        """刷新用户信息"""
        pass