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


class DeleteGameModeRequest(Gs2BasicRequest):

    class Constant(Gs2Ranking):
        FUNCTION = "DeleteGameMode"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(DeleteGameModeRequest, self).__init__(params)
        if params is None:
            self.__ranking_table_name = None
        else:
            self.set_ranking_table_name(params['rankingTableName'] if 'rankingTableName' in params.keys() else None)
        if params is None:
            self.__game_mode = None
        else:
            self.set_game_mode(params['gameMode'] if 'gameMode' in params.keys() else None)

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
        if not isinstance(ranking_table_name, unicode):
            raise TypeError(type(ranking_table_name))
        self.__ranking_table_name = ranking_table_name

    def with_ranking_table_name(self, ranking_table_name):
        """
        ランキングテーブルの名前を指定します。を設定
        :param ranking_table_name: ランキングテーブルの名前を指定します。
        :type ranking_table_name: unicode
        :return: this
        :rtype: DeleteGameModeRequest
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
        if not isinstance(game_mode, unicode):
            raise TypeError(type(game_mode))
        self.__game_mode = game_mode

    def with_game_mode(self, game_mode):
        """
        ゲームモードの名前を指定します。を設定
        :param game_mode: ゲームモードの名前を指定します。
        :type game_mode: unicode
        :return: this
        :rtype: DeleteGameModeRequest
        """
        self.set_game_mode(game_mode)
        return self
