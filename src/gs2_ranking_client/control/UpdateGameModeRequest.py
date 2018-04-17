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
        else:
            self.set_ranking_table_name(params['rankingTableName'] if 'rankingTableName' in params.keys() else None)
        if params is None:
            self.__game_mode = None
        else:
            self.set_game_mode(params['gameMode'] if 'gameMode' in params.keys() else None)
        if params is None:
            self.__calc_interval = None
        else:
            self.set_calc_interval(params['calcInterval'] if 'calcInterval' in params.keys() else None)
        if params is None:
            self.__put_score_trigger_script = None
        else:
            self.set_put_score_trigger_script(params['putScoreTriggerScript'] if 'putScoreTriggerScript' in params.keys() else None)
        if params is None:
            self.__put_score_done_trigger_script = None
        else:
            self.set_put_score_done_trigger_script(params['putScoreDoneTriggerScript'] if 'putScoreDoneTriggerScript' in params.keys() else None)
        if params is None:
            self.__calculate_ranking_done_trigger_script = None
        else:
            self.set_calculate_ranking_done_trigger_script(params['calculateRankingDoneTriggerScript'] if 'calculateRankingDoneTriggerScript' in params.keys() else None)

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
        if ranking_table_name and not (isinstance(ranking_table_name, str) or isinstance(ranking_table_name, unicode)):
            raise TypeError(type(ranking_table_name))
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
        if game_mode and not (isinstance(game_mode, str) or isinstance(game_mode, unicode)):
            raise TypeError(type(game_mode))
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
        if calc_interval and not isinstance(calc_interval, int):
            raise TypeError(type(calc_interval))
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

    def get_put_score_trigger_script(self):
        """
        スコア登録時 に実行されるGS2-Scriptを取得
        :return: スコア登録時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__put_score_trigger_script

    def set_put_score_trigger_script(self, put_score_trigger_script):
        """
        スコア登録時 に実行されるGS2-Scriptを設定
        :param put_score_trigger_script: スコア登録時 に実行されるGS2-Script
        :type put_score_trigger_script: unicode
        """
        if put_score_trigger_script and not (isinstance(put_score_trigger_script, str) or isinstance(put_score_trigger_script, unicode)):
            raise TypeError(type(put_score_trigger_script))
        self.__put_score_trigger_script = put_score_trigger_script

    def with_put_score_trigger_script(self, put_score_trigger_script):
        """
        スコア登録時 に実行されるGS2-Scriptを設定
        :param put_score_trigger_script: スコア登録時 に実行されるGS2-Script
        :type put_score_trigger_script: unicode
        :return: this
        :rtype: UpdateGameModeRequest
        """
        self.set_put_score_trigger_script(put_score_trigger_script)
        return self

    def get_put_score_done_trigger_script(self):
        """
        スコア登録完了時 に実行されるGS2-Scriptを取得
        :return: スコア登録完了時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__put_score_done_trigger_script

    def set_put_score_done_trigger_script(self, put_score_done_trigger_script):
        """
        スコア登録完了時 に実行されるGS2-Scriptを設定
        :param put_score_done_trigger_script: スコア登録完了時 に実行されるGS2-Script
        :type put_score_done_trigger_script: unicode
        """
        if put_score_done_trigger_script and not (isinstance(put_score_done_trigger_script, str) or isinstance(put_score_done_trigger_script, unicode)):
            raise TypeError(type(put_score_done_trigger_script))
        self.__put_score_done_trigger_script = put_score_done_trigger_script

    def with_put_score_done_trigger_script(self, put_score_done_trigger_script):
        """
        スコア登録完了時 に実行されるGS2-Scriptを設定
        :param put_score_done_trigger_script: スコア登録完了時 に実行されるGS2-Script
        :type put_score_done_trigger_script: unicode
        :return: this
        :rtype: UpdateGameModeRequest
        """
        self.set_put_score_done_trigger_script(put_score_done_trigger_script)
        return self

    def get_calculate_ranking_done_trigger_script(self):
        """
        集計処理完了時 に実行されるGS2-Scriptを取得
        :return: 集計処理完了時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__calculate_ranking_done_trigger_script

    def set_calculate_ranking_done_trigger_script(self, calculate_ranking_done_trigger_script):
        """
        集計処理完了時 に実行されるGS2-Scriptを設定
        :param calculate_ranking_done_trigger_script: 集計処理完了時 に実行されるGS2-Script
        :type calculate_ranking_done_trigger_script: unicode
        """
        if calculate_ranking_done_trigger_script and not (isinstance(calculate_ranking_done_trigger_script, str) or isinstance(calculate_ranking_done_trigger_script, unicode)):
            raise TypeError(type(calculate_ranking_done_trigger_script))
        self.__calculate_ranking_done_trigger_script = calculate_ranking_done_trigger_script

    def with_calculate_ranking_done_trigger_script(self, calculate_ranking_done_trigger_script):
        """
        集計処理完了時 に実行されるGS2-Scriptを設定
        :param calculate_ranking_done_trigger_script: 集計処理完了時 に実行されるGS2-Script
        :type calculate_ranking_done_trigger_script: unicode
        :return: this
        :rtype: UpdateGameModeRequest
        """
        self.set_calculate_ranking_done_trigger_script(calculate_ranking_done_trigger_script)
        return self
