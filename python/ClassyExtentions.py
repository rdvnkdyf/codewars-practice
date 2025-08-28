from preloaded import Animal

class Cat(Animal):
    def speak(self):
        return f'{self.name} meows.'
    

"""
from preloaded import Animal
from solution import Cat
import codewars_test as test

@test.describe('Fixed Tests')
def fixed_tests():
    @test.it("Testing for Mr Whiskers")
    def mr_whiskers():
        cat = Cat('Mr Whiskers')
        test.assert_equals(cat.speak(),'Mr Whiskers meows.')
        test.expect(isinstance(cat, Animal), "Your Cat class should extend Animal")
    @test.it("Testing for Lamp")
    def lamp():
        cat = Cat('Lamp')
        test.assert_equals(cat.speak(),'Lamp meows.')
    @test.it("Testing for $$Money Bags$$")
    def money_bags():
        cat = Cat('$$Money Bags$$')
        test.assert_equals(cat.speak(),'$$Money Bags$$ meows.')
        
"""