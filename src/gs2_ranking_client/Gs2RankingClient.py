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

import json

from gs2_core_client.Gs2Constant import Gs2Constant
from gs2_core_client.AbstractGs2Client import AbstractGs2Client


class Gs2RankingClient(AbstractGs2Client):

    ENDPOINT = "ranking"

    def __init__(self, credential, region):
        """
        コンストラクタ
        :param credential: 認証情報
        :type credential: IGs2Credential
        :param region: GS2リージョン
        :type region: str
        """
        super(Gs2RankingClient, self).__init__(credential, region)


    def create_game_mode(self, request):
        """
        ゲームモードを作成します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_ranking_client.control.CreateGameModeRequest.CreateGameModeRequest
        :return: 結果
        :rtype: gs2_ranking_client.control.CreateGameModeResult.CreateGameModeResult
        """
        body = { 
            "asc": request.get_asc(),
            "gameMode": request.get_game_mode(),
            "calcInterval": request.get_calc_interval(),
        }

        headers = { 
        }
        from gs2_ranking_client.control.CreateGameModeRequest import CreateGameModeRequest

        from gs2_ranking_client.control.CreateGameModeResult import CreateGameModeResult
        return CreateGameModeResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/ranking/" + str(("null" if request.get_ranking_table_name() is None else request.get_ranking_table_name())) + "/mode",
            service=self.ENDPOINT,
            module=CreateGameModeRequest.Constant.MODULE,
            function=CreateGameModeRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))




    def create_ranking_table(self, request):
        """
        ランキングテーブルを新規作成します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_ranking_client.control.CreateRankingTableRequest.CreateRankingTableRequest
        :return: 結果
        :rtype: gs2_ranking_client.control.CreateRankingTableResult.CreateRankingTableResult
        """
        body = { 
            "name": request.get_name(),
            "description": request.get_description(),
        }

        headers = { 
        }
        from gs2_ranking_client.control.CreateRankingTableRequest import CreateRankingTableRequest

        from gs2_ranking_client.control.CreateRankingTableResult import CreateRankingTableResult
        return CreateRankingTableResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/ranking",
            service=self.ENDPOINT,
            module=CreateRankingTableRequest.Constant.MODULE,
            function=CreateRankingTableRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))



    def delete_game_mode(self, request):
        """
        ゲームモードを削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_ranking_client.control.DeleteGameModeRequest.DeleteGameModeRequest

        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_ranking_client.control.DeleteGameModeRequest import DeleteGameModeRequest

        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/ranking/" + str(("null" if request.get_ranking_table_name() is None else request.get_ranking_table_name())) + "/mode/" + str(("null" if request.get_game_mode() is None else request.get_game_mode())) + "",
            service=self.ENDPOINT,
            module=DeleteGameModeRequest.Constant.MODULE,
            function=DeleteGameModeRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )



    def delete_ranking_table(self, request):
        """
        ランキングテーブルを削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_ranking_client.control.DeleteRankingTableRequest.DeleteRankingTableRequest

        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_ranking_client.control.DeleteRankingTableRequest import DeleteRankingTableRequest

        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/ranking/" + str(("null" if request.get_ranking_table_name() is None else request.get_ranking_table_name())) + "",
            service=self.ENDPOINT,
            module=DeleteRankingTableRequest.Constant.MODULE,
            function=DeleteRankingTableRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )



    def describe_game_mode(self, request):
        """
        ゲームモードの一覧を取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_ranking_client.control.DescribeGameModeRequest.DescribeGameModeRequest
        :return: 結果
        :rtype: gs2_ranking_client.control.DescribeGameModeResult.DescribeGameModeResult
        """

        query_strings = {

            'pageToken': request.get_page_token(),

            'limit': request.get_limit(),

        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_ranking_client.control.DescribeGameModeRequest import DescribeGameModeRequest

        from gs2_ranking_client.control.DescribeGameModeResult import DescribeGameModeResult
        return DescribeGameModeResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/ranking/" + str(("null" if request.get_ranking_table_name() is None else request.get_ranking_table_name())) + "/mode",
            service=self.ENDPOINT,
            module=DescribeGameModeRequest.Constant.MODULE,
            function=DescribeGameModeRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def describe_ranking_table(self, request):
        """
        ランキングテーブルの一覧を取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_ranking_client.control.DescribeRankingTableRequest.DescribeRankingTableRequest
        :return: 結果
        :rtype: gs2_ranking_client.control.DescribeRankingTableResult.DescribeRankingTableResult
        """

        query_strings = {

            'pageToken': request.get_page_token(),

            'limit': request.get_limit(),

        }
        headers = { 
        }
        from gs2_ranking_client.control.DescribeRankingTableRequest import DescribeRankingTableRequest

        from gs2_ranking_client.control.DescribeRankingTableResult import DescribeRankingTableResult
        return DescribeRankingTableResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/ranking",
            service=self.ENDPOINT,
            module=DescribeRankingTableRequest.Constant.MODULE,
            function=DescribeRankingTableRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def get_estimate_rank(self, request):
        """
        指定したスコアを取った時のおおよその順位を取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_ranking_client.control.GetEstimateRankRequest.GetEstimateRankRequest
        :return: 結果
        :rtype: gs2_ranking_client.control.GetEstimateRankResult.GetEstimateRankResult
        """

        query_strings = {

            'score': request.get_score(),

        }
        headers = { 
        }
        from gs2_ranking_client.control.GetEstimateRankRequest import GetEstimateRankRequest

        from gs2_ranking_client.control.GetEstimateRankResult import GetEstimateRankResult
        return GetEstimateRankResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/ranking/" + str(("null" if request.get_ranking_table_name() is None else request.get_ranking_table_name())) + "/mode/" + str(("null" if request.get_game_mode() is None else request.get_game_mode())) + "/ranking/estimate",
            service=self.ENDPOINT,
            module=GetEstimateRankRequest.Constant.MODULE,
            function=GetEstimateRankRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def get_game_mode(self, request):
        """
        ゲームモードを取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_ranking_client.control.GetGameModeRequest.GetGameModeRequest
        :return: 結果
        :rtype: gs2_ranking_client.control.GetGameModeResult.GetGameModeResult
        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_ranking_client.control.GetGameModeRequest import GetGameModeRequest

        from gs2_ranking_client.control.GetGameModeResult import GetGameModeResult
        return GetGameModeResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/ranking/" + str(("null" if request.get_ranking_table_name() is None else request.get_ranking_table_name())) + "/mode/" + str(("null" if request.get_game_mode() is None else request.get_game_mode())) + "",
            service=self.ENDPOINT,
            module=GetGameModeRequest.Constant.MODULE,
            function=GetGameModeRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def get_my_rank(self, request):
        """
        現在の順位を取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_ranking_client.control.GetMyRankRequest.GetMyRankRequest
        :return: 結果
        :rtype: gs2_ranking_client.control.GetMyRankResult.GetMyRankResult
        """

        query_strings = {

        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_ranking_client.control.GetMyRankRequest import GetMyRankRequest

        from gs2_ranking_client.control.GetMyRankResult import GetMyRankResult
        return GetMyRankResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/ranking/" + str(("null" if request.get_ranking_table_name() is None else request.get_ranking_table_name())) + "/mode/" + str(("null" if request.get_game_mode() is None else request.get_game_mode())) + "/ranking/rank",
            service=self.ENDPOINT,
            module=GetMyRankRequest.Constant.MODULE,
            function=GetMyRankRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def get_ranking(self, request):
        """
        ランキングを取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_ranking_client.control.GetRankingRequest.GetRankingRequest
        :return: 結果
        :rtype: gs2_ranking_client.control.GetRankingResult.GetRankingResult
        """

        query_strings = {

            'offset': request.get_offset(),

            'limit': request.get_limit(),

        }
        headers = { 
        }
        from gs2_ranking_client.control.GetRankingRequest import GetRankingRequest

        from gs2_ranking_client.control.GetRankingResult import GetRankingResult
        return GetRankingResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/ranking/" + str(("null" if request.get_ranking_table_name() is None else request.get_ranking_table_name())) + "/mode/" + str(("null" if request.get_game_mode() is None else request.get_game_mode())) + "/ranking",
            service=self.ENDPOINT,
            module=GetRankingRequest.Constant.MODULE,
            function=GetRankingRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def get_ranking_table(self, request):
        """
        ランキングテーブルを取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_ranking_client.control.GetRankingTableRequest.GetRankingTableRequest
        :return: 結果
        :rtype: gs2_ranking_client.control.GetRankingTableResult.GetRankingTableResult
        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_ranking_client.control.GetRankingTableRequest import GetRankingTableRequest

        from gs2_ranking_client.control.GetRankingTableResult import GetRankingTableResult
        return GetRankingTableResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/ranking/" + str(("null" if request.get_ranking_table_name() is None else request.get_ranking_table_name())) + "",
            service=self.ENDPOINT,
            module=GetRankingTableRequest.Constant.MODULE,
            function=GetRankingTableRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))




    def put_score(self, request):
        """
        スコアを登録します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_ranking_client.control.PutScoreRequest.PutScoreRequest
        :return: 結果
        :rtype: gs2_ranking_client.control.PutScoreResult.PutScoreResult
        """
        body = { 
            "score": request.get_score(),
            "meta": request.get_meta(),
        }

        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_ranking_client.control.PutScoreRequest import PutScoreRequest

        from gs2_ranking_client.control.PutScoreResult import PutScoreResult
        return PutScoreResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/ranking/" + str(("null" if request.get_ranking_table_name() is None else request.get_ranking_table_name())) + "/mode/" + str(("null" if request.get_game_mode() is None else request.get_game_mode())) + "/ranking",
            service=self.ENDPOINT,
            module=PutScoreRequest.Constant.MODULE,
            function=PutScoreRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))



    def update_game_mode(self, request):
        """
        ゲームモードの設定を更新します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_ranking_client.control.UpdateGameModeRequest.UpdateGameModeRequest
        :return: 結果
        :rtype: gs2_ranking_client.control.UpdateGameModeResult.UpdateGameModeResult
        """
        body = { 
            "calcInterval": request.get_calc_interval(),
        }

        headers = { 
        }
        from gs2_ranking_client.control.UpdateGameModeRequest import UpdateGameModeRequest

        from gs2_ranking_client.control.UpdateGameModeResult import UpdateGameModeResult
        return UpdateGameModeResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/ranking/" + str(("null" if request.get_ranking_table_name() is None else request.get_ranking_table_name())) + "/mode/" + str(("null" if request.get_game_mode() is None else request.get_game_mode())) + "",
            service=self.ENDPOINT,
            module=UpdateGameModeRequest.Constant.MODULE,
            function=UpdateGameModeRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))



    def update_ranking_table(self, request):
        """
        ランキングテーブルを更新します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_ranking_client.control.UpdateRankingTableRequest.UpdateRankingTableRequest
        :return: 結果
        :rtype: gs2_ranking_client.control.UpdateRankingTableResult.UpdateRankingTableResult
        """
        body = { 
        }

        if request.get_description() is not None:
            body["description"] = request.get_description()
        headers = { 
        }
        from gs2_ranking_client.control.UpdateRankingTableRequest import UpdateRankingTableRequest

        from gs2_ranking_client.control.UpdateRankingTableResult import UpdateRankingTableResult
        return UpdateRankingTableResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/ranking/" + str(("null" if request.get_ranking_table_name() is None else request.get_ranking_table_name())) + "",
            service=self.ENDPOINT,
            module=UpdateRankingTableRequest.Constant.MODULE,
            function=UpdateRankingTableRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))


