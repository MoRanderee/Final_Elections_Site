from django.db import models

# Create your models here.
class Question(models.Model):
    """This class is the model for the questions that are in the polls application

    :param question_text: The wording of the question
    :type question_text: str

    :param pub_date: The date that the question was piublished
    :type pub_date: Date and Time format
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """This function returns a string of the question

        :return: The question 
        :rtype: str
        
        """
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

