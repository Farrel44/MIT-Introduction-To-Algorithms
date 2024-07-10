import math

#read the document 
with open("shakespeare1.txt", 'r') as content:
    d1 = content.read()
with open("shakespeare2.txt", 'r') as content:
    d2 = content.read()
    
#turn it to a list  
d1_list = [d1.split()]
d2_list = [d2.split()]


def count_word_frequencies(word_list):
    word_frequencies = {}
    
    flattenned_list = []
    for item in word_list:
        if isinstance(item, list):
            flattenned_list.extend(item)
        else:
            flattenned_list.append(item)
            
    for word in flattenned_list:
        if word in word_list:
            word_frequencies[word] += 1
        else:
            word_frequencies[word] = 1
    return word_frequencies

#count the frequencies 
d1_freq = count_word_frequencies(d1_list)
d2_freq = count_word_frequencies(d2_list)

#Sort into order
sorted_d1 = {key: d1_freq[key] for key in sorted(d1_freq)} #iterates through all the key in alphabeticall order, and then inser it into a new dictrionary with the value from the dictionary that is not sorted
sorted_d2 = {key: d2_freq[key] for key in sorted(d2_freq)}



def sum_dict(sorted_dict):
    valueSum : 0
    x = sorted_dict.values
    for i in range(x):
        valueSum = valueSum + x
    return valueSum

#then we will compute the distance metric
def distance_metric(d1, d2):
    total = 0.0
    for word in d1:
        if word in d2:
            total += d1[word] * d2[word]
    return total

#as the formula for the angle metric uses the magnitude of the vector, we need to make a function to calculate it first

def magnitude_vector(freq):
    total = 0.0
    for count in freq.values():
        total += count * count
    return math.sqrt(total)


def angle_metric(freq1, freq2):
    inner_product = distance_metric(freq1, freq2)
    vector1 = magnitude_vector(freq1)
    vector2 = magnitude_vector(freq2)
    
    if vector1 == 0 or vector2 == 0:
        return math.pi / 2
    return math.acos(inner_product/(vector1*vector2))

#now, we calculate the angle metric
result = angle_metric(sorted_d1, sorted_d2)
#now, lets print the answer
print(f"The angle metric of the text1.txt and text2.txt is : {result} radians") 