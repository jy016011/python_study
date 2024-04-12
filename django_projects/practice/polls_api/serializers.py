from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from polls.models import Question, Choice, Vote
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class VoteSerializer(serializers.ModelSerializer):

    """
    투표시 질문과 선택 항목이 서로 맞지 않으면 오류를 일으킴
    Serializer.validate() 오버라이딩하여 구현
    """
    def validate(self, attrs):
        if attrs['choice'].question.id != attrs['question'].id:
            raise serializers.ValidationError('Question과 Choice가 조합이 안 맞음')
        return attrs

    class Meta:
        model = Vote
        fields = ['id', 'question', 'choice', 'voter']
        # serializer.is_valid()하는 부분을 재정의
        validators = [
            # vote레코드가 question, voter 쌍으로 유니크한지 검증하는 기능
            UniqueTogetherValidator(
                queryset=Vote.objects.all(),
                fields=['question', 'voter']
            )
        ]

class ChoiceSerializer(serializers.ModelSerializer):
    votes_count = serializers.SerializerMethodField()

    class Meta:
        model = Choice
        fields = ['choice_text', 'votes_count']

    # for votes_count, param obj == Choice object to be serialized
    def get_votes_count(self, obj):
        return obj.vote_set.count()


class QuestionSerializer(serializers.ModelSerializer):
    # Question의 owner필드는 아무나 쓸 수 있는 필드가 되면 안되므로 읽기 전용으로 설정
    owner = serializers.ReadOnlyField(source='owner.username')
    # 각 Question마다 Choice 데이터들을 불러오기위해 추가
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'question', 'pub_date', 'owner', 'choices']


class UserSerializer(serializers.ModelSerializer):
    """
    User의 해당하는 Question 레코드를 가져오기 위해서는 User의 PK를 통해 가져와야하므로
    PrimaryKeyRelatedField로 Question 모델을 지정해줌
    혹은 다음의 RelatedField로 Question 레코드를 가져와 표현한다.
    """
    # questions = serializers.PrimaryKeyRelatedField(many=True, queryset=Question.objects.all())
    # questions = serializers.StringRelatedField(many=True, read_only=True)
    # questions = serializers.SlugRelatedField(many=True, read_only=True, slug_field='pub_date')
    # 해당하는 question의 링크를 보여줌
    questions = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='question-detail')

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
