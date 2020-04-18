#importing the libraries
import pandas as pd
import math
import random

#reading test records
test_records = pd.read_csv('train.csv')

print("\nAttributes Under Consideration :")
for i in test_records:
    if(i != 'Survived'):
        print(i,end=" , ")

print("\nTarget Attribute  : Survived")

print("\n\nTesting Record Details\n\n")


#total number of records
total_number_of_records = test_records.shape[0]
print("Total Number of Records for Training : "+ str(total_number_of_records))


#replacing missing values of 'Age'
#the missing 'Age' Parameter is replaced by taking the mean of existing values and between the range (mean-standard_deviation, mean+standard_deviation)
number_of_missing_records = test_records['Age'].isna().sum()
sum_of_records =  test_records['Age'].sum()
mean_of_records = sum_of_records /(total_number_of_records - number_of_missing_records)
numerartor_in_standard_deviation = 0

print("Average Age of records :" + str(mean_of_records))
for i in range(len(test_records['Age'])):
    if not math.isnan(test_records['Age'][i]):
        numerartor_in_standard_deviation = numerartor_in_standard_deviation + (test_records['Age'][i] - mean_of_records)**2

standard_deviation = (numerartor_in_standard_deviation/(total_number_of_records-number_of_missing_records))**(1/2)


count = 0
for i in range(len(test_records['Age'])):
    if math.isnan(test_records['Age'][i]):
        test_records.loc[i,'Age'] = random.randint(int(mean_of_records-standard_deviation),int( mean_of_records+standard_deviation))
        count = count + 1





#replacing missing values of 'Pclass'
#The  missing 'Pclass' attribute is replaced by Most frequent Pclass.
dictionary_for_count = {1: 0 , 2:0 , 3:0 }
for i in test_records['Pclass']:
    if not math.isnan(i):
        dictionary_for_count[i] = dictionary_for_count[i]+1;


if dictionary_for_count[1] > dictionary_for_count[2]:
    if dictionary_for_count[1] > dictionary_for_count[3]:
        most_frequent_class = 1
    else:
        most_frequent_class  = 3
else:
    if dictionary_for_count[2] > dictionary_for_count[3]:
        most_frequent_class= 2
    else:
        most_frequent_class = 3

print("Most Frequent Class : "+ str(most_frequent_class))

for i in range(len(test_records['Pclass'])):
    if math.isnan(test_records['Pclass'][i]):
        test_records.loc[i,'Pclass'] = most_frequent_class




#replacing missing values in 'Sex' Column
#The  missing 'Sex' attribute is replaced by Most frequent gender.
dictionary_for_count = {'male' : 0 , 'female' : 0}
for i in test_records['Sex']:
    if i == 'male' or i =='female':
        dictionary_for_count[i] = dictionary_for_count[i]+1;


if dictionary_for_count['male']  > dictionary_for_count['female']:
    most_frequent_gender = 'male'
else:
    most_frequent_gender = 'female'

print("Most Frequent Gender : "+str(most_frequent_gender))


for i in range(len(test_records['Sex'])):
    if  i == 'male' and i =='female':
        test_records.loc[i,'Sex'] = most_frequent_gender







#replacing missing values of 'Embarked'
#The  missing 'Embarked' attribute is replaced by Most frequent port.
dictionary_for_count = {'S': 0 , 'C':0 , 'Q':0 }
for i in test_records['Embarked']:
    if i =='S' or i == 'C' or i == 'Q':
        dictionary_for_count[i] = dictionary_for_count[i]+1;


if dictionary_for_count['S'] > dictionary_for_count['C']:
    if dictionary_for_count['S'] > dictionary_for_count['Q']:
        most_frequent_port = 'S'
    else:
        most_frequent_port  = 'Q'
else:
    if dictionary_for_count['C'] > dictionary_for_count['Q']:
        most_frequent_port= 'C'
    else:
        most_frequent_port = 'Q'

print("Most Frequent Port : "+str(most_frequent_port))


for i in range(len(test_records['Embarked'])):
    if i == '':
        test_records.loc[i,'Embarked'] = most_frequent_port




#The 'Age' Parameter is separated into 2 groups to make it a binary attribute
#Segregation of 'Age' class into 2 groups;
for i in range(len(test_records['Age'])):
    if test_records['Age'][i] <= 3:
        test_records.loc[i,'Age'] = 0
    else :
        test_records.loc[i,'Age'] = 1




#Gini Index for all Attributes

#Gini Index for 'Gender' Column is Calculated
gender_dictionary = {'male-survived' : 0 , 'male-died' : 0 ,'female-survived' : 0,'female-died' : 0}

for i in range(len(test_records['Sex'])):
    if test_records['Sex'][i] == 'male' and test_records['Survived'][i] == 1:
        gender_dictionary['male-survived'] = gender_dictionary['male-survived'] + 1
    elif test_records['Sex'][i] == 'male' and test_records['Survived'][i] == 0:
        gender_dictionary['male-died'] = gender_dictionary['male-died'] + 1
    elif test_records['Sex'][i] == 'female' and test_records['Survived'][i] == 1:
        gender_dictionary['female-survived'] = gender_dictionary['female-survived'] + 1
    else:
        gender_dictionary['female-died'] = gender_dictionary['female-died'] + 1


number_of_male = gender_dictionary['male-survived'] + gender_dictionary['male-died']
number_of_female = gender_dictionary['female-survived'] + gender_dictionary['female-died']


probability_of_male = (number_of_male)/total_number_of_records
probability_of_female = (number_of_female)/total_number_of_records

probability_of_male_and_survived = gender_dictionary['male-survived']/ number_of_male
probability_of_male_and_died = gender_dictionary['male-died']/ number_of_male

gini_index_for_male = 1 - ((probability_of_male_and_survived)**2 + (probability_of_male_and_died)**2)


probability_of_female_and_survived = gender_dictionary['female-survived']/ number_of_female
probability_of_female_and_died = gender_dictionary['female-died']/ number_of_female

gini_index_for_female = 1 - ((probability_of_female_and_survived)**2 + (probability_of_female_and_died)**2)

gini_index_for_gender = probability_of_male*gini_index_for_male + probability_of_female*gini_index_for_female

print("\nGini Index for Gender Coloumn : "+str(gini_index_for_gender))




print("\n Gini Index for Pclass Column :")

#Gini Index for 'Pclass'
pclass_dictionary= {'1-survived':0,'2-survived':0,'3-survived':0,'1-died':0,'2-died':0,'3-died':0}
for i in range(len(test_records['Pclass'])):
    if test_records['Pclass'][i] == 1:
        if test_records['Survived'][i] == 1:
            pclass_dictionary['1-survived'] = pclass_dictionary['1-survived']+1
        else:
            pclass_dictionary['1-died'] = pclass_dictionary['1-died']+1
    elif test_records['Pclass'][i] == 2:
        if test_records['Survived'][i] == 1:
            pclass_dictionary['2-survived'] = pclass_dictionary['2-survived']+1
        else:
            pclass_dictionary['2-died'] = pclass_dictionary['2-died']+1
    else:
        if test_records['Survived'][i] == 1:
            pclass_dictionary['3-survived'] = pclass_dictionary['3-survived']+1
        else:
            pclass_dictionary['3-died'] = pclass_dictionary['3-died']+1


total_class_1 = pclass_dictionary['1-survived'] + pclass_dictionary['1-died']
total_class_2 = pclass_dictionary['2-survived'] + pclass_dictionary['2-died']
total_class_3 = pclass_dictionary['3-survived'] + pclass_dictionary['3-died']

#gini index for different combinations
gini_for_individual = (total_class_1/total_number_of_records)*(1 - ((pclass_dictionary['1-survived'])/total_class_1)**2 - ((pclass_dictionary['1-died'])/total_class_1)**2) + (total_class_2/total_number_of_records)*(1 - ((pclass_dictionary['2-survived'])/total_class_2)**2 - ((pclass_dictionary['2-died'])/total_class_2)**2) + (total_class_3/total_number_of_records)*(1 - ((pclass_dictionary['3-survived'])/total_class_3)**2 - ((pclass_dictionary['3-died'])/total_class_3)**2)
print("Gini Index when Individual Class is Considered : "+str(gini_for_individual))

gini_for_1_2_combined_class = ((total_class_1+total_class_2)/total_number_of_records)*(1 - ((pclass_dictionary['1-survived']+pclass_dictionary['2-survived'])/(total_class_1+total_class_2))**2 - ((pclass_dictionary['1-died']+pclass_dictionary['2-died'])/(total_class_1+total_class_2))**2) + (total_class_3/total_number_of_records)*(1 - ((pclass_dictionary['3-survived'])/total_class_3)**2 - ((pclass_dictionary['3-died'])/total_class_3)**2)
print("Gini Index when class 1 and 2 are combined : "+str(gini_for_1_2_combined_class))

gini_for_1_3_combined_class = ((total_class_1+total_class_3)/total_number_of_records)*(1 - ((pclass_dictionary['1-survived']+pclass_dictionary['3-survived'])/(total_class_1+total_class_3))**2 - ((pclass_dictionary['1-died']+pclass_dictionary['3-died'])/(total_class_1+total_class_3))**2) + (total_class_2/total_number_of_records)*(1 - ((pclass_dictionary['2-survived'])/total_class_2)**2 - ((pclass_dictionary['2-died'])/total_class_2)**2)
print("Gini Index when class 1 and 3 are combined : "+str(gini_for_1_3_combined_class))

gini_for_2_3_combined_class = ((total_class_2+total_class_3)/total_number_of_records)*(1 - ((pclass_dictionary['2-survived']+pclass_dictionary['2-survived'])/(total_class_2+total_class_3))**2 - ((pclass_dictionary['2-died']+pclass_dictionary['3-died'])/(total_class_2+total_class_3))**2) + (total_class_1/total_number_of_records)*(1 - ((pclass_dictionary['1-survived'])/total_class_1)**2 - ((pclass_dictionary['1-died'])/total_class_1)**2)
print("Gini Index when class 2 and 3 are combined : "+str(gini_for_2_3_combined_class))



#Gini index for 'Age' Coloumn
age_dictionary = {'0-survived' : 0 , '0-died' : 0 ,'1-survived' : 0,'1-died' : 0}

for i in range(len(test_records['Age'])):
    if test_records['Age'][i] == 0  and test_records['Survived'][i] == 1:
        age_dictionary['0-survived'] = age_dictionary['0-survived'] + 1
    elif test_records['Age'][i] == 0 and test_records['Survived'][i] == 0:
        age_dictionary['0-died'] = age_dictionary['0-died'] + 1
    elif test_records['Age'][i] == 1 and test_records['Survived'][i] == 1:
        age_dictionary['1-survived'] = age_dictionary['1-survived'] + 1
    else:
        age_dictionary['1-died'] = age_dictionary['1-died'] + 1


number_of_class_0 = age_dictionary['0-survived'] + age_dictionary['0-died']
number_of_class_1 = age_dictionary['1-survived'] + age_dictionary['1-died']

probability_of_class_0 = (number_of_class_0)/total_number_of_records
probability_of_class_1 = (number_of_class_1)/total_number_of_records

probability_of_class_0_and_survived = age_dictionary['0-survived']/ number_of_class_0
probability_of_class_0_and_died = age_dictionary['0-died']/ number_of_class_0

gini_index_for_class_0 = 1 - ((probability_of_class_0_and_survived)**2 + (probability_of_class_0_and_died)**2)


probability_of_class_1_and_survived = age_dictionary['1-survived']/ number_of_class_1
probability_of_class_1_and_died = age_dictionary['1-died']/ number_of_class_1

gini_index_for_class_1 = 1 - ((probability_of_class_1_and_survived)**2 + (probability_of_class_1_and_died)**2)

gini_index_for_age = probability_of_class_0*gini_index_for_class_0 + probability_of_class_1*gini_index_for_class_1

print("\nGini Index for Age Coloumn : "+str(gini_index_for_age))





print("\nGini Index for Embarked Column : ")

#Gini Index for 'Embarked'
embarked_dictionary= {'S-survived':0,'Q-survived':0,'C-survived':0,'S-died':0,'Q-died':0,'C-died':0}
for i in range(len(test_records['Embarked'])):
    if test_records['Embarked'][i] == 'S':
        if test_records['Survived'][i] == 1:
            embarked_dictionary['S-survived'] = embarked_dictionary['S-survived']+1
        else:
            embarked_dictionary['S-died'] = embarked_dictionary['S-died']+1
    elif test_records['Embarked'][i] == 'Q':
        if test_records['Survived'][i] == 1:
            embarked_dictionary['Q-survived'] = embarked_dictionary['Q-survived']+1
        else:
            embarked_dictionary['Q-died'] = embarked_dictionary['Q-died']+1
    else:
        if test_records['Survived'][i] == 1:
            embarked_dictionary['C-survived'] = embarked_dictionary['C-survived']+1
        else:
            embarked_dictionary['C-died'] = embarked_dictionary['C-died']+1


total_class_S = embarked_dictionary['S-survived'] + embarked_dictionary['S-died']
total_class_Q = embarked_dictionary['Q-survived'] + embarked_dictionary['Q-died']
total_class_C = embarked_dictionary['C-survived'] + embarked_dictionary['C-died']


#gini index for different combinations
gini_for_individual_embarked = (total_class_S/total_number_of_records)*(1 - ((embarked_dictionary['S-survived'])/total_class_S)**2 - ((embarked_dictionary['S-died'])/total_class_S)**2) + (total_class_Q/total_number_of_records)*(1 - ((embarked_dictionary['Q-survived'])/total_class_Q)**2 - ((embarked_dictionary['Q-died'])/total_class_Q)**2) + (total_class_C/total_number_of_records)*(1 - ((embarked_dictionary['C-survived'])/total_class_C)**2 - ((embarked_dictionary['C-died'])/total_class_C)**2)
print("Gini Index when Individual Embarked Port is Considered : "+str(gini_for_individual))

gini_for_S_Q_combined_class = ((total_class_S+total_class_Q)/total_number_of_records)*(1 - ((embarked_dictionary['S-survived']+embarked_dictionary['Q-survived'])/(total_class_S+total_class_Q))**2 - ((embarked_dictionary['S-died']+embarked_dictionary['Q-died'])/(total_class_S+total_class_Q))**2) + (total_class_C/total_number_of_records)*(1 - ((embarked_dictionary['C-survived'])/total_class_C)**2 - ((embarked_dictionary['C-died'])/total_class_C)**2)
print("Gini Index when class S and Q are combined : "+str(gini_for_S_Q_combined_class))

gini_for_S_C_combined_class = ((total_class_S+total_class_C)/total_number_of_records)*(1 - ((embarked_dictionary['S-survived']+embarked_dictionary['C-survived'])/(total_class_S+total_class_C))**2 - ((embarked_dictionary['S-died']+embarked_dictionary['C-died'])/(total_class_S+total_class_C))**2) + (total_class_Q/total_number_of_records)*(1 - ((embarked_dictionary['Q-survived'])/total_class_Q)**2 - ((embarked_dictionary['Q-died'])/total_class_Q)**2)
print("Gini Index when class S and C are combined : "+str(gini_for_S_C_combined_class))

gini_for_Q_C_combined_class = ((total_class_Q+total_class_C)/total_number_of_records)*(1 - ((embarked_dictionary['Q-survived']+embarked_dictionary['Q-survived'])/(total_class_Q+total_class_C))**2 - ((embarked_dictionary['Q-died']+embarked_dictionary['C-died'])/(total_class_Q+total_class_C))**2) + (total_class_S/total_number_of_records)*(1 - ((embarked_dictionary['S-survived'])/total_class_S)**2 - ((embarked_dictionary['S-died'])/total_class_S)**2)
print("Gini Index when class Q and C are combined : "+str(gini_for_Q_C_combined_class))


count = 0

for i in range(len(test_records['Age'])):
    if(test_records['Sex'][i] =='male'):
        if(test_records['Age'][i] == 0):
            if(test_records['Pclass'][i] == 3):
                survived = 0
            else:
                survived = 1
        else:
            survived = 0
    else:
        if(test_records['Pclass'][i]==3):
            if(test_records['Embarked'][i] == 'S'):
                survived = 1
            else:
                survived = 0
        else:
            survived = 1

    if survived == test_records['Survived'][i]:
        count = count+1

print("\nAccuracy for approach 1 : "+ str(count*100/(total_number_of_records)))

count = 0

for i in range(len(test_records['Age'])):
    if(test_records['Sex'][i] =='male'):
        if(test_records['Age'][i] == 1):
            survived = 0
        else:
            survived = 1
    else:
        if(test_records['Pclass'][i] == 3):
            survived = 0
        else:
            survived =1
    if survived == test_records['Survived'][i]:
        count = count+1

print("Accuracy for approach 2 : "+str(count*100/(total_number_of_records)))






print("\n\n\n\n\n\nTesting Record Details\n")
#reading test records
test_records = pd.read_csv('test.csv')




#total number of records
total_number_of_records = test_records.shape[0]
print("Total Number of Records for Training : "+ str(total_number_of_records))


#replacing missing values of 'Age'
number_of_missing_records = test_records['Age'].isna().sum()
sum_of_records =  test_records['Age'].sum()
mean_of_records = sum_of_records /(total_number_of_records - number_of_missing_records)
numerartor_in_standard_deviation = 0

print("Average Age of records :" + str(mean_of_records))
for i in range(len(test_records['Age'])):
    if not math.isnan(test_records['Age'][i]):
        numerartor_in_standard_deviation = numerartor_in_standard_deviation + (test_records['Age'][i] - mean_of_records)**2

standard_deviation = (numerartor_in_standard_deviation/(total_number_of_records-number_of_missing_records))**(1/2)


count = 0
for i in range(len(test_records['Age'])):
    if math.isnan(test_records['Age'][i]):
        test_records.loc[i,'Age'] = random.randint(int(mean_of_records-standard_deviation),int( mean_of_records+standard_deviation))
        count = count + 1



#replacing missing values of 'Pclass'
dictionary_for_count = {1: 0 , 2:0 , 3:0 }
for i in test_records['Pclass']:
    if not math.isnan(i):
        dictionary_for_count[i] = dictionary_for_count[i]+1;


if dictionary_for_count[1] > dictionary_for_count[2]:
    if dictionary_for_count[1] > dictionary_for_count[3]:
        most_frequent_class = 1
    else:
        most_frequent_class  = 3
else:
    if dictionary_for_count[2] > dictionary_for_count[3]:
        most_frequent_class= 2
    else:
        most_frequent_class = 3

print("Most Frequent Class : "+ str(most_frequent_class))

for i in range(len(test_records['Pclass'])):
    if math.isnan(test_records['Pclass'][i]):
        test_records.loc[i,'Pclass'] = most_frequent_class




#replacing missing values in 'Sex' Column
dictionary_for_count = {'male' : 0 , 'female' : 0}
for i in test_records['Sex']:
    if i == 'male' or i =='female':
        dictionary_for_count[i] = dictionary_for_count[i]+1;


if dictionary_for_count['male']  > dictionary_for_count['female']:
    most_frequent_gender = 'male'
else:
    most_frequent_gender = 'female'

print("Most Frequent Gender : "+str(most_frequent_gender))


for i in range(len(test_records['Sex'])):
    if  i == 'male' and i =='female':
        test_records.loc[i,'Sex'] = most_frequent_gender







#replacing missing values of 'Embarked'
dictionary_for_count = {'S': 0 , 'C':0 , 'Q':0 }
for i in test_records['Embarked']:
    if i =='S' or i == 'C' or i == 'Q':
        dictionary_for_count[i] = dictionary_for_count[i]+1;


if dictionary_for_count['S'] > dictionary_for_count['C']:
    if dictionary_for_count['S'] > dictionary_for_count['Q']:
        most_frequent_port = 'S'
    else:
        most_frequent_port  = 'Q'
else:
    if dictionary_for_count['C'] > dictionary_for_count['Q']:
        most_frequent_port= 'C'
    else:
        most_frequent_port = 'Q'

print("Most Frequent Port : "+str(most_frequent_port))


for i in range(len(test_records['Embarked'])):
    if i == '':
        test_records.loc[i,'Embarked'] = most_frequent_port



#Segregation of 'Age' class into 2 groups;
for i in range(len(test_records['Age'])):
    if test_records['Age'][i] <= 3:
        test_records.loc[i,'Age'] = 0
    else :
        test_records.loc[i,'Age'] = 1



count = 0

for i in range(len(test_records['Age'])):
    if(test_records['Sex'][i] =='male'):
        if(test_records['Age'][i] == 0):
            if(test_records['Pclass'][i] == 3):
                survived = 0
            else:
                survived = 1
        else:
            survived = 0
    else:
        if(test_records['Pclass'][i]==3):
            if(test_records['Embarked'][i] == 'S'):
                survived = 1
            else:
                survived = 0
        else:
            survived = 1

    if survived == test_records['Survived'][i]:
        count = count+1

print("\nAccuracy for approach 1 : "+ str(count*100/(total_number_of_records)))

count = 0

for i in range(len(test_records['Age'])):
    if(test_records['Sex'][i] =='male'):
        if(test_records['Age'][i] == 1):
            survived = 0
        else:
            survived = 1
    else:
        if(test_records['Pclass'][i] == 3):
            survived = 0
        else:
            survived =1
    if survived == test_records['Survived'][i]:
        count = count+1

print("Accuracy for approach 2 : "+ str(count*100/(total_number_of_records))+"\n\n\n\n\n")
