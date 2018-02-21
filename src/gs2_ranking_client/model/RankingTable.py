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

class RankingTable(object):

    def __init__(self, params=None):
        if params is None:
            self.__ranking_table_id = None
            self.__owner_id = None
            self.__name = None
            self.__description = None
            self.__put_score_trigger_script = None
            self.__put_score_done_trigger_script = None
            self.__calculate_ranking_done_trigger_script = None
            self.__create_at = None
            self.__update_at = None
        else:
            self.set_ranking_table_id(params['rankingTableId'] if 'rankingTableId' in params.keys() else None)
            self.set_owner_id(params['ownerId'] if 'ownerId' in params.keys() else None)
            self.set_name(params['name'] if 'name' in params.keys() else None)
            self.set_description(params['description'] if 'description' in params.keys() else None)
            self.set_put_score_trigger_script(params['putScoreTriggerScript'] if 'putScoreTriggerScript' in params.keys() else None)
            self.set_put_score_done_trigger_script(params['putScoreDoneTriggerScript'] if 'putScoreDoneTriggerScript' in params.keys() else None)
            self.set_calculate_ranking_done_trigger_script(params['calculateRankingDoneTriggerScript'] if 'calculateRankingDoneTriggerScript' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)
            self.set_update_at(params['updateAt'] if 'updateAt' in params.keys() else None)


    def get_ranking_table_id(self):
        """
        ランキングテーブルGRNを取得
        :return: ランキングテーブルGRN
        :rtype: unicode
        """
        return self.__ranking_table_id

    def set_ranking_table_id(self, ranking_table_id):
        """
        ランキングテーブルGRNを設定
        :param ranking_table_id: ランキングテーブルGRN
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

    def get_name(self):
        """
        ランキングテーブル名を取得
        :return: ランキングテーブル名
        :rtype: unicode
        """
        return self.__name

    def set_name(self, name):
        """
        ランキングテーブル名を設定
        :param name: ランキングテーブル名
        :type name: unicode
        """
        self.__name = name

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
        最終更新日時(エポック秒)を取得
        :return: 最終更新日時(エポック秒)
        :rtype: int
        """
        return self.__update_at

    def set_update_at(self, update_at):
        """
        最終更新日時(エポック秒)を設定
        :param update_at: 最終更新日時(エポック秒)
        :type update_at: int
        """
        self.__update_at = update_at

    def to_dict(self):
        return { 
            "rankingTableId": self.__ranking_table_id,
            "ownerId": self.__owner_id,
            "name": self.__name,
            "description": self.__description,
            "putScoreTriggerScript": self.__put_score_trigger_script,
            "putScoreDoneTriggerScript": self.__put_score_done_trigger_script,
            "calculateRankingDoneTriggerScript": self.__calculate_ranking_done_trigger_script,
            "createAt": self.__create_at,
            "updateAt": self.__update_at,
        }