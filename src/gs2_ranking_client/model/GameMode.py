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


class GameMode(object):

    def __init__(self, params=None):
        if params is None:
            self.__game_mode_id = None
            self.__ranking_table_id = None
            self.__owner_id = None
            self.__game_mode = None
            self.__asc = None
            self.__calc_interval = None
            self.__calculating = None
            self.__put_score_trigger_script = None
            self.__put_score_done_trigger_script = None
            self.__calculate_ranking_done_trigger_script = None
            self.__create_at = None
            self.__update_at = None
            self.__last_calc_at = None
        else:
            self.set_game_mode_id(params['gameModeId'] if 'gameModeId' in params.keys() else None)
            self.set_ranking_table_id(params['rankingTableId'] if 'rankingTableId' in params.keys() else None)
            self.set_owner_id(params['ownerId'] if 'ownerId' in params.keys() else None)
            self.set_game_mode(params['gameMode'] if 'gameMode' in params.keys() else None)
            self.set_asc(params['asc'] if 'asc' in params.keys() else None)
            self.set_calc_interval(params['calcInterval'] if 'calcInterval' in params.keys() else None)
            self.set_calculating(params['calculating'] if 'calculating' in params.keys() else None)
            self.set_put_score_trigger_script(params['putScoreTriggerScript'] if 'putScoreTriggerScript' in params.keys() else None)
            self.set_put_score_done_trigger_script(params['putScoreDoneTriggerScript'] if 'putScoreDoneTriggerScript' in params.keys() else None)
            self.set_calculate_ranking_done_trigger_script(params['calculateRankingDoneTriggerScript'] if 'calculateRankingDoneTriggerScript' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)
            self.set_update_at(params['updateAt'] if 'updateAt' in params.keys() else None)
            self.set_last_calc_at(params['lastCalcAt'] if 'lastCalcAt' in params.keys() else None)

    def get_game_mode_id(self):
        """
        ゲームモードGRNを取得
        :return: ゲームモードGRN
        :rtype: unicode
        """
        return self.__game_mode_id

    def set_game_mode_id(self, game_mode_id):
        """
        ゲームモードGRNを設定
        :param game_mode_id: ゲームモードGRN
        :type game_mode_id: unicode
        """
        self.__game_mode_id = game_mode_id

    def get_ranking_table_id(self):
        """
        ランキングテーブルを取得
        :return: ランキングテーブル
        :rtype: unicode
        """
        return self.__ranking_table_id

    def set_ranking_table_id(self, ranking_table_id):
        """
        ランキングテーブルを設定
        :param ranking_table_id: ランキングテーブル
        :type ranking_table_id: unicode
        """
        self.__ranking_table_id = ranking_table_id

    def get_owner_id(self):
        """
        オーナーIDを取得
        :return: オーナーID
        :rtype: unicode
        """
        return self.__owner_id

    def set_owner_id(self, owner_id):
        """
        オーナーIDを設定
        :param owner_id: オーナーID
        :type owner_id: unicode
        """
        self.__owner_id = owner_id

    def get_game_mode(self):
        """
        ゲームモード名を取得
        :return: ゲームモード名
        :rtype: unicode
        """
        return self.__game_mode

    def set_game_mode(self, game_mode):
        """
        ゲームモード名を設定
        :param game_mode: ゲームモード名
        :type game_mode: unicode
        """
        self.__game_mode = game_mode

    def get_asc(self):
        """
        ランキング計算に昇順を適用するかを取得
        :return: ランキング計算に昇順を適用するか
        :rtype: bool
        """
        return self.__asc

    def set_asc(self, asc):
        """
        ランキング計算に昇順を適用するかを設定
        :param asc: ランキング計算に昇順を適用するか
        :type asc: bool
        """
        self.__asc = asc

    def get_calc_interval(self):
        """
        集計間隔(分)を取得
        :return: 集計間隔(分)
        :rtype: int
        """
        return self.__calc_interval

    def set_calc_interval(self, calc_interval):
        """
        集計間隔(分)を設定
        :param calc_interval: 集計間隔(分)
        :type calc_interval: int
        """
        self.__calc_interval = calc_interval

    def get_calculating(self):
        """
        集計処理中か否かを取得
        :return: 集計処理中か否か
        :rtype: bool
        """
        return self.__calculating

    def set_calculating(self, calculating):
        """
        集計処理中か否かを設定
        :param calculating: 集計処理中か否か
        :type calculating: bool
        """
        self.__calculating = calculating

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
        self.__put_score_trigger_script = put_score_trigger_script

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
        self.__put_score_done_trigger_script = put_score_done_trigger_script

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
        self.__calculate_ranking_done_trigger_script = calculate_ranking_done_trigger_script

    def get_create_at(self):
        """
        作成日時(エポック秒)を取得
        :return: 作成日時(エポック秒)
        :rtype: int
        """
        return self.__create_at

    def set_create_at(self, create_at):
        """
        作成日時(エポック秒)を設定
        :param create_at: 作成日時(エポック秒)
        :type create_at: int
        """
        self.__create_at = create_at

    def get_update_at(self):
        """
        更新日時(エポック秒)を取得
        :return: 更新日時(エポック秒)
        :rtype: int
        """
        return self.__update_at

    def set_update_at(self, update_at):
        """
        更新日時(エポック秒)を設定
        :param update_at: 更新日時(エポック秒)
        :type update_at: int
        """
        self.__update_at = update_at

    def get_last_calc_at(self):
        """
        最終集計日時(エポック秒)を取得
        :return: 最終集計日時(エポック秒)
        :rtype: int
        """
        return self.__last_calc_at

    def set_last_calc_at(self, last_calc_at):
        """
        最終集計日時(エポック秒)を設定
        :param last_calc_at: 最終集計日時(エポック秒)
        :type last_calc_at: int
        """
        self.__last_calc_at = last_calc_at

    def to_dict(self):
        return {
            "gameModeId": self.__game_mode_id,
            "rankingTableId": self.__ranking_table_id,
            "ownerId": self.__owner_id,
            "gameMode": self.__game_mode,
            "asc": self.__asc,
            "calcInterval": self.__calc_interval,
            "calculating": self.__calculating,
            "putScoreTriggerScript": self.__put_score_trigger_script,
            "putScoreDoneTriggerScript": self.__put_score_done_trigger_script,
            "calculateRankingDoneTriggerScript": self.__calculate_ranking_done_trigger_script,
            "createAt": self.__create_at,
            "updateAt": self.__update_at,
            "lastCalcAt": self.__last_calc_at,
        }
