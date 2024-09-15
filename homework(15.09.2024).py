# 1. Simple Abstraction and Function Creation
def calculate_area(length,width):
    return length * width

print(
      f"{calculate_area(100,200)}",
      f"{calculate_area(500,600)}",
      f"{calculate_area(900,200)}",
      f"{calculate_area(200,1000)}")

# 2. Modularity with Separate Functions

def calculate_perimeter(length,width):
    return (length + width) * 2
def calculate_area_and_perimeter(length,width):
    return {'area':calculate_area(length,width),
            'perimeter':calculate_perimeter(length,width)}

print(calculate_area_and_perimeter(500,900))

# 3. Function with Default Arguments

def calculate_discount(price,discount=10):
    return int(price - (price/100 * discount))

print(calculate_discount(900))


# 4. Keyword vs. Positional Arguments
def display_person_info(name,age):
    return f"The person called {name} is {age} years"
#tests
print(display_person_info("Tame",19))
print(display_person_info(name="Impala",age=42))
print(display_person_info("Mary",age=18))

#5. Abstraction through Function Composition

def convert_to_celsius(kelvin):
    return float(kelvin) - 273.15
def convert_to_kelvin(celsius):
    return float(celsius) + 273.15

#test
print(convert_to_celsius((convert_to_kelvin(20))))

#6. Variable-Length Arguments (Args and Kwargs)

def summarize_numbers(*args):
    return sum(args)

print(summarize_numbers(3,4,5,6,7,8,9,10,11))


def describe_person(**kwargs):
    result = "His "
    for key, value in kwargs.items():
        result += f"{key} is {value}, "
    return result

print(describe_person(name="Tame",surname="Impala",age=42,hair="black",height="medium",weight="normal"))

#Higher-Order Functions

def apply_discount(prices):
    result = [calculate_discount(i) for i in prices]
    return result

print(apply_discount([10,25,35,455]))

#8. Modularity with Multiple Files
from math_operations import add, subtract, multiply, divide
print(add(15,15,30))
print(subtract(100,20,50))
print(multiply(100,100))
print(divide(9000,90,20))

#9. Reusable Code with Object-Oriented Programming


class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_started = False
    def show_details(self):
        print(f"Год выпуска: {self.year} Сделано в:{self.make} Название модели: {self.model} Заведена: {self.is_started}")
    def start_car(self):
        self.is_started = True
        print( f"Машина {self.model} была заведена.")
def main():
    car1 = Car("Japan", "Toyota Supra MkII", 2003)
    car2 = Car("Germany","BMW M5 F10 COMPETITION", 2022)

    car1.show_details()
    car1.start_car()
    car1.show_details()

    car2.show_details()
    car2.start_car()
    car2.show_details()

if __name__ == "__main__":
    '''
     Данная кострунция обеспечивает правильное выполнение кода если
     этот файл будет импортирован в других файлах
     она проверяет если файл выполнен как основной (__main__)
     если этот файл будет импортирован функция main() не будет выполнена'''
    main()
