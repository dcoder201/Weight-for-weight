def order_weight(strng):
    # your code
    weights = strng.strip().split()
    weights.sort(key=lambda x: (sum(map(int, x)), x))
    return " ".join(weights)
  
 
import codewars_test as test
    
@test.describe("Weight for weight")
def tests():
    @test.it("basic tests")
    def basics1():
        test.assert_equals(order_weight("103 123 4444 99 2000"), "2000 103 123 4444 99")
        test.assert_equals(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"), "11 11 2000 10003 22 123 1234000 44444444 9999")
        test.assert_equals(order_weight(""), "")
        


  
