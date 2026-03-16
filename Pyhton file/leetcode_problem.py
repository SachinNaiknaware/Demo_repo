#1# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


# class Solution:
#     def twoSum(self, nums, target):
#         num_map = {}
#         for i, num in enumerate(nums):
#             complement = target - num
#             if complement in num_map:
#                 return [num_map[complement], i]
#             num_map[num] = i

# sol = Solution()
# print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]

# def av(data):
#     n = len(data)
#     avg = sum(data) / n
#     return avg

# print(av([10,10,20]))


#Check if Two Strings Are Anagrams

# def is_anagrams(s1,s2):
#     s1=s1.replace(" "," ").lower()
#     s2=s2.replace(" "," ").lower()
#     if len(s1) != len(s2):
#         return False
#     count={}
#     for ch in s1:
#         count[ch] = count.get(ch,0)+1
#     for ch in s2:
#         if ch not in count or count[ch] == 0:
#             return False
#         count[ch]-=1
#     return True
# print(is_anagrams('listen','silent'))

#Remove Duplicates From a List (Preserve Order)

# Input  = [1,2,3,2,4,1,5]
# Output = [1,2,3,4,5]


# def Remove_duplicate(lst):
#     new=set()
#     result=[]
#     for num in lst:
#         if num not in new:
#             new.add(num)
#             result.append(num)
            
#     return result
# nums=[1,2,3,2,4,1,5]
# print(Remove_duplicate(nums))
    
# new=set(nums)
# print(type(nums),nums)
        
# Two Numbers With Sum Closest to Zero
# Input: [-8, -3, -1, 2, 4, 10]
# Output: (-3, 2)

# def closest_to_zero(nums):
#     nums.sort()
#     left = 0
#     right = len(nums) - 1
#     closest_sum = float('inf')
#     pair = (0,0)
#     while left < right:
#         current_sum = nums[left] + nums[right]
#         if abs(current_sum) < abs(closest_sum):
#             closest_sum = current_sum
#             pair = (nums[left], nums[right])
#         if current_sum < 0:
#             left += 1
#         else:
#             right -= 1
#     return pair
# nums = [-8,-3,-1,2,4,10]
# print(closest_to_zero(nums))


#Reverse Words in a Sentence (No Built-in Reverse)

# Input:
# "I love python"
# Output:
# "python love I"
# def reverse_sentence(sentence):
#     words = sentence.split()
#     reversed_words = []
#     i = len(words) - 1
#    # print(len(words))
#     while i >= 0:
#         reversed_words.append(words[i])
#         i -= 1
#     return " ".join(reversed_words)
# print(reverse_sentence("I love python"))

#Employee Class with 10% Salary Hike
# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def calculate_hike(self):
#         hike=self.salary * 0.10
#         self.salary += hike
#         return self.salary
# emp=Employee("Sachin",5000)
# print("Old Salry",50000)
# print("new_Sallry",emp.calculate_hike())


# from flask import Flask, request, jsonify
# app = Flask(__name__)
# data = {
#     "python": "Programming language",
#     "flask": "Python web framework",
#     "ai": "Artificial Intelligence"
# }
# @app.route("/")
# def home():
#     return "Welcome! Try /search?q=python"

# @app.route("/search")
# def search():
#     query = request.args.get("q")
#     result = data.get(query, "Not found")
#     return jsonify({"query": query, "result": result})
# if __name__ == "__main__":
#     app.run(debug=True)

# Connect to PostgreSQL and Fetch Employees (Mock Code)
# import psycopg2
# connection = psycopg2.connect(
#     host="localhost",
#     database="company_db",
#     user="postgres",
#     password="password"
# )
# cursor = connection.cursor()
# query = "SELECT name, salary FROM employees WHERE salary > 50000"
# cursor.execute(query)
# results = cursor.fetchall()
# for row in results:
#     print(row)
# cursor.close()
# connection.close()


# import numpy as np

# def cosine_similarity(v1, v2):

#     dot_product = np.dot(v1, v2)

#     norm_v1 = np.linalg.norm(v1)
#     norm_v2 = np.linalg.norm(v2)

#     return dot_product / (norm_v1 * norm_v2)


# def retrieve_most_similar(query_vector, embeddings):

#     best_score = -1
#     best_vector = None

#     for vec in embeddings:

#         score = cosine_similarity(query_vector, vec)

#         if score > best_score:
#             best_score = score
#             best_vector = vec

#     return best_vector


# query = np.array([0.2, 0.1, 0.7])

# embeddings = [
#     np.array([0.1,0.2,0.7]),
#     np.array([0.9,0.1,0.1]),
#     np.array([0.2,0.1,0.6])
# ]

# print(retrieve_most_similar(query, embeddings))

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# def detect_cycle(head):
#     slow = head
#     fast = head
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#         if slow == fast:
#             return True
#     return False
         

# from flask import Flask

# app=Flask(__name__)

# @app.route("/")
# def home():
#     return "hiiiiiiiiiiiiiiiiiiiiiiiiiiii"


# if __name__ == "__main__":
#     app.run(debug=True)
    
    
