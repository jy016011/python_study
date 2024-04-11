from rest_framework import serializers
from polls.models import Question, Choice
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class QuestionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Question
        fields = ['id', 'question', 'pub_date', 'owner']

class UserSerializer(serializers.ModelSerializer):
    """
    User의 해당하는 Question 레코드를 가져오기 위해서는 User의 PK를 통해 가져와야하므로
    PrimaryKeyRelatedField로 Question 모델을 지정해줌
    """
    questions = serializers.PrimaryKeyRelatedField(many=True, queryset=Question.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'questions']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "두 패스워드가 불일치"})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ['username', 'password', 'password2']