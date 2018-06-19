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


class GetEstimateRankResult(object):

    def __init__(self, response):
        """
        コンストラクタ
        :type response: レスポンスボディ
        :type response: dict
        """
        self.__min = long(response['min']) if 'min' in response.keys() and response['min'] is not None else None
        self.__max = long(response['max']) if 'max' in response.keys() and response['max'] is not None else None
    def get_min(self):
        """
        推定最小順位を取得
        :return: 推定最小順位
        :rtype: long
        """
        return self.__min
    def get_max(self):
        """
        推定最大順位を取得
        :return: 推定最大順位
        :rtype: long
        """
        return self.__max

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return super(GetEstimateRankResult, self).__getitem__(key)

    def to_dict(self):
        """
        辞書配列に変換
        :return: 辞書配列
        :rtype: dict
        """
        return {
            'min': self.__min,
            'max': self.__max,
        }
