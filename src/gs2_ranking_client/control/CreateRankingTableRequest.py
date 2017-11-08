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

from gs2_core_client.Gs2BasicRequest import Gs2BasicRequest
from gs2_ranking_client.Gs2Ranking import Gs2Ranking


class CreateRankingTableRequest(Gs2BasicRequest):

    class Constant(Gs2Ranking):
        FUNCTION = "CreateRankingTable"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(CreateRankingTableRequest, self).__init__(params)
        if params is None:
            self.__name = None
            self.__description = None
        else:
            self.set_name(params['name'] if 'name' in params.keys() else None)
            self.set_description(params['description'] if 'description' in params.keys() else None)

    def get_name(self):
        """
        ランキングテーブルの名前を取得
        :return: ランキングテーブルの名前
        :rtype: unicode
        """
        return self.__name

    def set_name(self, name):
        """
        ランキングテーブルの名前を設定
        :param name: ランキングテーブルの名前
        :type name: unicode
        """
        self.__name = name

    def with_name(self, name):
        """
        ランキングテーブルの名前を設定
        :param name: ランキングテーブルの名前
        :type name: unicode
        :return: this
        :rtype: CreateRankingTableRequest
        """
        self.set_name(name)
        return self

    def get_description(self):
        """
        説明文を取得
        :return: 説明文
        :rtype: unicode
        """
        return self.__description

    def set_description(self, description):
        """
        説明文を設定
        :param description: 説明文
        :type description: unicode
        """
        self.__description = description

    def with_description(self, description):
        """
        説明文を設定
        :param description: 説明文
        :type description: unicode
        :return: this
        :rtype: CreateRankingTableRequest
        """
        self.set_description(description)
        return self