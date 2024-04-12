from django.test import TestCase
from polls_api.serializers import QuestionSerializer, VoteSerializer
from django.contrib.auth.models import User
from polls.models import Question, Choice, Vote
# Create your tests here.

class VoteSerializerTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username='testuser')
        self.question = Question.objects.create(
            question='abc',
            owner=self.user
        )
        self.choice = Choice.objects.create(
            question=self.question,
            choice_text='1'
        )
    def test_vote_serializer_with_valid_data(self):
        data = {
            'question': self.question.id,
            'choice': self.choice.id,
            'voter': self.user.id
        }
        serializer = VoteSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        vote = serializer.save()
        self.assertEqual(vote.question, self.question)
        self.assertEqual(vote.choice, self.choice)
        self.assertEqual(vote.voter, self.user)

    # UniqueTogetherValidator 테스트
    def test_vote_serializer_with_duplicated_vote(self):
        choice1 = Choice.objects.create(
            question=self.question,
            choice_text='2'
        )
        Vote.objects.create(question=self.question, choice=self.choice, voter=self.user)

        data = {
            'question': self.question.id,
            'choice': choice1.id,
            'voter': self.user.id
        }

        serializer = VoteSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    # valid() 테스트
    def test_vote_serializer_with_unmatched_question_and_choice(self):
        question2 = Question.objects.create(
            question='abc',
            owner=self.user
        )
        choice2 = Choice.objects.create(
            question=question2,
            choice_text='1'
        )
        data = {
            'question': self.question.id,
            'choice': choice2.id,
            'voter': self.user.id
        }
        serializer = VoteSerializer(data=data)
        self.assertFalse(serializer.is_valid())



class QuestionSerializerTest(TestCase):
    def test_with_valid_data(self):
        serializer = QuestionSerializer(data={"question": "cdf"})
        self.assertEqual(serializer.is_valid(),True)
        new_question = serializer.save()
        self.assertIsNotNone(new_question.id)

    def test_with_invalid_data(self):
        serializer = QuestionSerializer(data={"question": ""})
        self.assertEqual(serializer.is_valid(), False)
