from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .datas.dataheapmap import dataheatmap
from .datas.databarchart import databarchart
from .datas.datascatterchart import datascatter
from .datas.datapiechart import datapiechart
from .datas.datageomap import datageomap
def getData(chart_type):
    data = []
    if(chart_type == "bar"):
        data = databarchart
    elif(chart_type == "heatmap"):
        data = dataheatmap
    elif(chart_type == "scatter"):
        data = datascatter
    elif(chart_type == "pie"):
        data = datapiechart
    elif(chart_type == "geo"):
        data = datageomap
    output = [{
        "type": "chart",
        "chart_type": chart_type,
        "data": data
    }]
    return output

class GetData(APIView):
    def get(self, request):
        chart_type = request.GET.get('chart_type')
        print(chart_type)
        data = getData(chart_type)
        serializer = getDataSerializer(data, many=True)
        return Response(serializer.data)

