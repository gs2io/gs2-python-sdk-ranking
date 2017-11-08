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

from gs2_ranking_client.model import *


class GetMyRankResult(object):

    def __init__(self, response):
        """
        コンストラクタ
        :type response: レスポンスボディ
        :type response: dict
        """
        
        self.__index = long(response['index']) if 'index' in response.keys() and response['index'] is not None else None
        
        self.__rank = long(response['rank']) if 'rank' in response.keys() and response['rank'] is not None else None

    def get_index(self):
        """
        先頭からの位置を取得
        :return: 先頭からの位置
        :rtype: long
        """
        return self.__index

    def get_rank(self):
        """
        同点同順位を採用した場合の順位を取得
        :return: 同点同順位を採用した場合の順位
        :rtype: long
        """
        return self.__rank

    def to_dict(self):
        """
        辞書配列に変換
        :return: 辞書配列
        :rtype: dict
        """
        return { 
            'index': self.__index,
        
            'rank': self.__rank,
        
        }