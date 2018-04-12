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

from gs2_core_client.Gs2UserRequest import Gs2UserRequest
from gs2_ranking_client.Gs2Ranking import Gs2Ranking


class PutScoreRequest(Gs2UserRequest):

    class Constant(Gs2Ranking):
        FUNCTION = "PutScore"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(PutScoreRequest, self).__init__(params)
        if params is None:
            self.__ranking_table_name = None
            self.__game_mode = None
            self.__score = None
            self.__meta = None
        else:
            self.set_ranking_table_name(params['rankingTableName'] if 'rankingTableName' in params.keys() else None)
            self.set_game_mode(params['gameMode'] if 'gameMode' in params.keys() else None)
            self.set_score(params['score'] if 'score' in params.keys() else None)
            self.set_meta(params['meta'] if 'meta' in params.keys() else None)

    def get_ranking_table_name(self):
        """
        ランキングテーブルの名前を指定します。を取得
        :return: ランキングテーブルの名前を指定します。
        :rtype: unicode
        """
        return self.__ranking_table_name

    def set_ranking_table_name(self, ranking_table_name):
        """
        ランキングテーブルの名前を指定します。を設定
        :param ranking_table_name: ランキングテーブルの名前を指定します。
        :type ranking_table_name: unicode
        """
        if ranking_table_name and not isinstance(ranking_table_name, unicode):
            raise TypeError(type(ranking_table_name))
        self.__ranking_table_name = ranking_table_name

    def with_ranking_table_name(self, ranking_table_name):
        """
        ランキングテーブルの名前を指定します。を設定
        :param ranking_table_name: ランキングテーブルの名前を指定します。
        :type ranking_table_name: unicode
        :return: this
        :rtype: PutScoreRequest
        """
        self.set_ranking_table_name(ranking_table_name)
        return self

    def get_game_mode(self):
        """
        ゲームモードの名前を指定します。を取得
        :return: ゲームモードの名前を指定します。
        :rtype: unicode
        """
        return self.__game_mode

    def set_game_mode(self, game_mode):
        """
        ゲームモードの名前を指定します。を設定
        :param game_mode: ゲームモードの名前を指定します。
        :type game_mode: unicode
        """
        if game_mode and not isinstance(game_mode, unicode):
            raise TypeError(type(game_mode))
        self.__game_mode = game_mode

    def with_game_mode(self, game_mode):
        """
        ゲームモードの名前を指定します。を設定
        :param game_mode: ゲームモードの名前を指定します。
        :type game_mode: unicode
        :return: this
        :rtype: PutScoreRequest
        """
        self.set_game_mode(game_mode)
        return self

    def get_score(self):
        """
        スコア値を取得
        :return: スコア値
        :rtype: long
        """
        return self.__score

    def set_score(self, score):
        """
        スコア値を設定
        :param score: スコア値
        :type score: long
        """
        if score and not isinstance(score, long):
            raise TypeError(type(score))
        self.__score = score

    def with_score(self, score):
        """
        スコア値を設定
        :param score: スコア値
        :type score: long
        :return: this
        :rtype: PutScoreRequest
        """
        self.set_score(score)
        return self

    def get_meta(self):
        """
        スコアに付随するメタ情報を取得
        :return: スコアに付随するメタ情報
        :rtype: unicode
        """
        return self.__meta

    def set_meta(self, meta):
        """
        スコアに付随するメタ情報を設定
        :param meta: スコアに付随するメタ情報
        :type meta: unicode
        """
        if meta and not isinstance(meta, unicode):
            raise TypeError(type(meta))
        self.__meta = meta

    def with_meta(self, meta):
        """
        スコアに付随するメタ情報を設定
        :param meta: スコアに付随するメタ情報
        :type meta: unicode
        :return: this
        :rtype: PutScoreRequest
        """
        self.set_meta(meta)
        return self
