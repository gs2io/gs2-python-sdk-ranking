# encoding: utf-8
#
# Copyright 2016 Game Server Services, Inc. or its affiliates. All Rights
# Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

class RankingScore(object):

    def __init__(self, params=None):
        if params is None:
            self.__index = None
            self.__score = None
            self.__meta = None
            self.__update_at = None
            self.__user_id = None
            self.__rank = None
        else:
            self.set_index(params['index'] if 'index' in params.keys() else None)
            self.set_score(params['score'] if 'score' in params.keys() else None)
            self.set_meta(params['meta'] if 'meta' in params.keys() else None)
            self.set_update_at(params['updateAt'] if 'updateAt' in params.keys() else None)
            self.set_user_id(params['userId'] if 'userId' in params.keys() else None)
            self.set_rank(params['rank'] if 'rank' in params.keys() else None)


    def get_index(self):
        """
        先頭からの位置を取得
        :return: 先頭からの位置
        :rtype: long
        """
        return self.__index

    def set_index(self, index):
        """
        先頭からの位置を設定
        :param index: 先頭からの位置
        :type index: long
        """
        self.__index = index

    def get_score(self):
        """
        スコア値を取得
        :return: スコア値
        :rtype: int
        """
        return self.__score

    def set_score(self, score):
        """
        スコア値を設定
        :param score: スコア値
        :type score: int
        """
        self.__score = score

    def get_meta(self):
        """
        メタデータを取得
        :return: メタデータ
        :rtype: unicode
        """
        return self.__meta

    def set_meta(self, meta):
        """
        メタデータを設定
        :param meta: メタデータ
        :type meta: unicode
        """
        self.__meta = meta

    def get_update_at(self):
        """
        登録日時(エポック秒)を取得
        :return: 登録日時(エポック秒)
        :rtype: int
        """
        return self.__update_at

    def set_update_at(self, update_at):
        """
        登録日時(エポック秒)を設定
        :param update_at: 登録日時(エポック秒)
        :type update_at: int
        """
        self.__update_at = update_at

    def get_user_id(self):
        """
        ユーザIDを取得
        :return: ユーザID
        :rtype: unicode
        """
        return self.__user_id

    def set_user_id(self, user_id):
        """
        ユーザIDを設定
        :param user_id: ユーザID
        :type user_id: unicode
        """
        self.__user_id = user_id

    def get_rank(self):
        """
        同点同順位を採用した場合の順位を取得
        :return: 同点同順位を採用した場合の順位
        :rtype: long
        """
        return self.__rank

    def set_rank(self, rank):
        """
        同点同順位を採用した場合の順位を設定
        :param rank: 同点同順位を採用した場合の順位
        :type rank: long
        """
        self.__rank = rank

    def to_dict(self):
        return { 
            "index": self.__index,
            "score": self.__score,
            "meta": self.__meta,
            "updateAt": self.__update_at,
            "userId": self.__user_id,
            "rank": self.__rank,
        }