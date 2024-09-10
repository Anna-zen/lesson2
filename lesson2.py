#Практическое задание по уроку "Строки и индексация строк"
example = 'just a randomise string'
print(example[0])#возвращает 1й символ строки
print(example[-1])#возвращает последний символ строки
len_of_string = len (example) #возвращает длину строки
#проверка print (len_of_string)
half_len=len_of_string //2 #половина длины строки
#проверка print(half_len)
print(example[half_len:]) #печатает все символы, начиная с половины строки
print(example[::-1]) #печатает строку наоборот
print(example[1::2]) #печатает каждый второй символ