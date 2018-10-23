from django.test import TestCase
from .models import Post
from django.utils import timezone

class PostTestCase( TestCase ):

    def test_postPublish( self ):
        #Arrange
        expected = size + 1
        result = 0
        #Act
        
        #Assert
        self.assertEqual( expected, result)


# Create your tests here.
