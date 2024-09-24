
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import recepie, Ingredient, Instruction
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email','phone_number']


class registerSerializer(serializers.ModelSerializer):
    class meta:
        model= User
        fields = ['username', 'email', 'password','phone_number']


        def create(self,validated_data):
            user=User.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],
                password=validated_data['password'],
                phone_number=validated_data['phone_number']
            )
            return user
        

class IngridientSerilaizer(serializers.ModelSerializer):

    class Meta:
        model=Ingredient
        fields=('ingrideint_name','ingrideint_qnt')

class InstructionSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=Instruction
        fields=('no_of_steps','description_of_step')


class RecepieSerializer(serializers.ModelSerializer):
    ingr=IngridientSerilaizer(many=True)
    instructions=InstructionSerilaizer(many=True)

    class Meta:
        model=recepie
        fields=('name','desc','user','ingr','instructions')

        def create(self,validated_data):
            ingr=validated_data.pop('ingr',[])
            instructions=validated_data.pop('instructions',[])

            recepie_obj=recepie.objects.create(**validated_data)

            for i in ingr:
                Ingredient.objects.create(recepie_name=recepie_obj, **i)

            for i in instructions:
                Instruction.objects.create(recepie_name=recepie_obj, **i)

            return recepie_obj
        

        def update(self,instance,validated_data):
            ingr=validated_data.pop('ingr')
            instructions=validated_data.pop('instructions')

            instance.name=validated_data.get('name',instance.name)
            instance.desc=validated_data.get('desc',instance.desc)
            instance.save()

            instance.ingredients.all().delete()
            for i in ingr:
                Ingredient.objects.create(recepie_name=instance, **i)
            instance.instructions.all().delete()
            for i in instructions:
                Instruction.objects.create(recepie_name=instance, **i)    
