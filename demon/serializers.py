from rest_framework import serializers
from .models import Personaje, Arma, UsuarioPersonalizado

class ArmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arma
        fields = ('id','personaje','nombre','precio','danho','crit','alcance','tiros','especial','ammoPrice')
        read_only = ('id')


class PJSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personaje
        fields = ('id','usuario','nombre','estado','clase','fuerza','velocidad','intelig','combat','sanity','fear','cuerpo','maxHP','maxWounds','stress','traumaRes','dinero','armorPoints','extras')
        read_only = ('id')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioPersonalizado
        fields = ("id","username","biografia")
