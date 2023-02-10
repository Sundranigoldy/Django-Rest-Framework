from rest_framework import serializers
from .models import *

#Validators
def start_with_g(value):
    if value[0].lower()!='g':
        raise serializers.ValidationError('Name Should starts with g')
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[start_with_g])
    #here u add validator which created above
    roll = serializers.IntegerField()
    city=serializers.CharField(max_length=100)

    #now to create in same we need to add new function

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    
    #now to update data in same

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance
    

    #now for validation i.e we need to add validation that rollno should be 200 only not more than that

#Field Label Validation is used when we need to validation for single field

    def validate_roll(self,value):
        if value >=200:
            raise serializers.ValidationError('Seat is Full')
        return value

#object value validation is used when we need to validate multiple fields


    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'rohit' and ct.lower() != 'ranchi':
            raise serializers.ValidationError('City must be ranchi')
        return data

#here comes validators but it is defined above it is needed to be out of class function and 1st to execute


#model serializer class
'''
class studentserializers(serializers.Modelserializer):
#if we add readonly lie this

    #name = serializers.CharField(read_only=true)

#than name cannot be updated in any case.
    class meta:
        fields =['id','name','roll','city'] 

 to add multiple fields in read only than just add below

        read_only=['name','roll']

#now above 2 fields will be read only.

#another way to do this is using extra_kwargs fields

        extra_kwargs ={'name':{'read_only':True}}

#model serializer validation.. process is same as above even for validator too..


#Field Label Validation is used when we need to validation for single field

    def validate_roll(self,value):
        if value >=200:
            raise serializers.ValidationError('Seat is Full')
        return value

#object value validation is used when we need to validate multiple fields


    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'rohit' and ct.lower() != 'ranchi':
            raise serializers.ValidationError('City must be ranchi')
        return data
'''
#works same as above serializer by just adding 4  lines of code.. no need to add put,post,delete and other serializer
