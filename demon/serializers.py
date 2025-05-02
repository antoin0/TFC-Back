from rest_framework import serializers
from .models import Personaje, Arma, UsuarioPersonalizado

class ArmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arma
        fields = ('id','personaje','nombre','precio','danho','crit','alcance','tiros','especial','ammoPrice')


class PJSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personaje
        fields = ('id','usuario','nombre','estado','clase','fuerza','velocidad','intelig','combat','sanity','fear','cuerpo','maxHP','maxWounds','stress','traumaRes','dinero','armorPoints','extras')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioPersonalizado
        read_only_fields = ('id','username','biografia')
