# ---------Challenge One-----------
def sum_to(n):
   total = 0
   for number in range(int(n)):
      number += 1
      # print(str(number) + ' this is number')
      total += number
      # print(str(total) + ' this is current total')
   return total

# print(sum_to(6))

# ----------Challenge Two------------
def largest(list):
   largest_num = 0
   for n in list:
      if int(n) > int(largest_num):
         largest_num = n
   return largest_num

print(largest([10, 4, 2, 231, 91, 54]))

# ----------Challenge Three-----------
def section_string(start, end, str1):
   # get the specific start and end string if str1 is length more than one
   string = []
   for n in range(start, end):
      string.append(str1[n])
   return ''.join(string)

def occurrences(str1, str2):
   total = 0
   # print(range(len(str1)))
   for i in range(len(str1)):
      x = section_string(i, i + len(str2), str1)
      # ayo what is this doing bruh
      if i + len(str2) > len(str1) - 1:
         return total
      if x == str2:
         total += 1
   return total

# print(occurrences('fleep floop', 'fl'))