from django.test import TestCase
from store.models import Category, Product

class TestCategoriesModel (TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name='django',Slug= 'django')
    
    def test_category_modle_entry(self):
        #test category model data insertion\type\field\attribute
        data= self.data1
        self.assertTrue(isinstance(data,Category))
    
    def test_category_modle_return(self):
        data = self.data1
        self.assertEqual(str(data),'phone')