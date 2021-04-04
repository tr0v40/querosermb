from datetime import datetime, timedelta
from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from .serializers import CriptoValores20Serializer, CriptoValores50Serializer, CriptoValores200Serializer
from .models import CriptoValores
from .functions import converter_to_timestamp
from .choices import TYPE_CRIPTO

class CriptoValoresViewSet(generics.ListAPIView):
        def get_serializer_class(self):
            if int(self.kwargs.get("mms")) == 20:
                return CriptoValores20Serializer
            elif int(self.kwargs.get("mms")) == 50:
                return CriptoValores50Serializer
            elif int(self.kwargs.get("mms")) == 200:
                return CriptoValores200Serializer
            raise PermissionDenied({"Mensagem": "Valor de mms não permitido"})

            
        def get_queryset(self):
            from_url = self.request.query_params.get('from')
            to_url = self.request.query_params.get('to') or converter_to_timestamp(datetime.now() - timedelta(1))
            pair_choice = [
                cripto for cripto in TYPE_CRIPTO 
                    if cripto[1] == self.kwargs.get("pair").upper() 
                ]
            if pair_choice:
                qs = CriptoValores.objects.filter(pair=pair_choice[0][0])
                if from_url:
                    qs = qs.filter(mms_timestamp__range=[from_url, to_url])
                else:
                    qs = qs.filter(mms_timestamp__lte=to_url).order_by('-mms_timestamp')[:1]
                return qs
            raise PermissionDenied({"Mensagem": "Criptomoeda indisponivel"})
            