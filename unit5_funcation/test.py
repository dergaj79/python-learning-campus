# animal = "rabbit"
#
# def water():
#     animal = "goldfish"
#     print(animal)
#
# water()
# print(animal)


# a = 0
#
#
# def my_function() :
#     a = 3
#     print(a)
#
#
# my_function()
# print(a)
# a=1
# def foo1():
#     print(a)
# foo1()
# print(a)
# def amount_of_oranges(small_cups=20, large_cups=10):
#     oranges_result=small_cups+large_cups*3
#     kg_result=oranges_result/5
#     print("Today you'll need",oranges_result,"oranges.")
#     print("Buy",kg_result,"kg of oranges.")
#     return oranges_result,kg_result
#
# results=amount_of_oranges(15,5)
# print(type(results))
# print(results)

def main():
  # City forcast generator program
  city_name = get_city_from_user()
  valid_city = is_city_valid(city_name)
  if not valid_city:
     print("Error! Wrong City!")
     return None
  temperature = get_current_weather(city_name)
  # Show forecast for the user
  show_weather(temperature, city_name)

if __name__ == "__main__":
  main()