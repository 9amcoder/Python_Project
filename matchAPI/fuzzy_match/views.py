from django.shortcuts import render
from fuzzy_match.models import Shopify_db,Tasteguru_db,SP_TS_Bridge
from fuzzy_match.serializers import Shopify_dbSerializer,Tasteguru_dbSerializer,SP_TS_Bridge_Serializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


#TODO
class FuzzyMatch(APIView):
    def get(self, request):
        matchList = SP_TS_Bridge.objects.all()
        serializer = SP_TS_Bridge_Serializer(matchList, many=True)
        tasteguru_list = self.tg_list()
        shopList = self.sp_list()
        for (f, b) in (tasteguru_list, shopList):
            fuzz.ratio('f','b')
            break
        return Response(serializer.data)

    def tg_list(self):
        tg_list = Tasteguru_db.objects.all()
        serializer = Tasteguru_dbSerializer(tg_list, many=True)
        return serializer.data
    def sp_list(self):
        shopifyList = Shopify_db.objects.all()
        serializer = Shopify_dbSerializer(shopifyList, many=True)
        return serializer.data
