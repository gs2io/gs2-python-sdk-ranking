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


class UpdateGameModeRequest(Gs2BasicRequest):

    class Constant(Gs2Ranking):
        FUNCTION = "UpdateGameMode"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(UpdateGameModeRequest, self).__init__(params)
        if params is None:
            self.__ranking_table_name = None
            self.__game_mode = None
            self.__calc_interval = None
        else:
            self.set_ranking_table_name(params['rankingTableName'] if 'rankingTableName' in params.keys() else None)
            self.set_game_mode(params['gameMode'] if 'gameMode' in params.keys() else None)
            self.set_calc_interval(params['calcInterval'] if 'calcInterval' in params.keys() else None)

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
        self.__ranking_table_name = ranking_table_name

    def with_ranking_table_name(self, ranking_table_name):
        """
        ランキングテーブルの名前を指定します。を設定
        :param ranking_table_name: ランキングテーブルの名前を指定します。
        :type ranking_table_name: unicode
        :return: this
        :rtype: UpdateGameModeRequest
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
        self.__game_mode = game_mode

    def with_game_mode(self, game_mode):
        """
        ゲームモードの名前を指定します。を設定
        :param game_mode: ゲームモードの名前を指定します。
        :type game_mode: unicode
        :return: this
        :rtype: UpdateGameModeRequest
        """
        self.set_game_mode(game_mode)
        return self

    def get_calc_interval(self):
        """
        このゲームモードのランキング集計間隔を分単位で指定しますを取得
        :return: このゲームモードのランキング集計間隔を分単位で指定します
        :rtype: int
        """
        return self.__calc_interval

    def set_calc_interval(self, calc_interval):
        """
        このゲームモードのランキング集計間隔を分単位で指定しますを設定
        :param calc_interval: このゲームモードのランキング集計間隔を分単位で指定します
        :type calc_interval: int
        """
        self.__calc_interval = calc_interval

    def with_calc_interval(self, calc_interval):
        """
        このゲームモードのランキング集計間隔を分単位で指定しますを設定
        :param calc_interval: このゲームモードのランキング集計間隔を分単位で指定します
        :type calc_interval: int
        :return: this
        :rtype: UpdateGameModeRequest
        """
        self.set_calc_interval(calc_interval)
        return self
