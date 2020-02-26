# *********** PYBANK SECTION STARTS HERE ******************
#importing dependencies
import csv
import os

file_budget = ('budget_data.csv')
header_bank = []

#opening the file 
with open(file_budget) as revenue_data:
    reader = csv.reader(revenue_data)
#storing header row
    header_bank = next(open(file_budget))
#skipping header row
    next(reader)

#creating containers to store values
    Profit = []
    Date = []
    Profit_Change = []

#finding total profit and number of months
    for row in reader:
        Profit.append(float(row[1]))
        Date.append(row[0])
#printing 2 of 5 results
    print(" ")
    print("Financial Analysis")
    print("--------------------")
    print("Total Months:"+ str(len(Date)))
    print("Sum of Profit/Loss: $", sum(Profit))


#finding profit change, profit max and profit min values, as well as corresponding dates for the max and min values
    for i in range(1, len(Date)):
        Profit_Change.append(Profit[i] - Profit[i-1])
        Profit_Change_Average = sum(Profit_Change)/len(Profit_Change)
        Profit_Change_Max = max(Profit_Change)
        Profit_Change_Min = min(Profit_Change)

        Profit_Change_Max_Date = str(Date[Profit_Change.index(max(Profit_Change))])
        Profit_Change_Min_Date = str(Date[Profit_Change.index(min(Profit_Change))])

#printing remaining 3 of 5 values, 5 of 5
    print("Average Revenue Change: $", round(Profit_Change_Average))
    print("Greatest Increase in Revenue:", Profit_Change_Max_Date, "($", Profit_Change_Max, ")")
    print("Greatest Decrease in Revenue:", Profit_Change_Min_Date, "($", Profit_Change_Min, ")")

#define output path and name output file
output_path_bank = os.path.join("PyBank_Output.csv")

with open(output_path_bank, 'w', newline="") as output_data_bank:
#activate csv.writer
    csvwriter = csv.writer(output_data_bank, delimiter=',')
#writing results printed in terminal to new csv file
    csvwriter.writerow(["Total Months:","" ,"", "", str(len(Date))])
    csvwriter.writerow(["Sum of Profit/Loss:","","","", sum(Profit)])
    csvwriter.writerow(["Average Revenue Change:","", "","", round(Profit_Change_Average)])
    csvwriter.writerow(["Greatest Increase in Revenue:","", "", Profit_Change_Max_Date, Profit_Change_Max])
    csvwriter.writerow(["Greatest Decrease in Revenue:", "", "", Profit_Change_Min_Date, Profit_Change_Min])


#  **************** PYPOLLS SECTION STARTS HERE *************


#csv library is necessary to build the code
file_polls = 'election_data.csv'
header_polls = []

#Building pathway to election data file
with open(file_polls) as polls:
    reader_polls = csv.reader(polls, delimiter=',')
#Store header row
    header_polls = next(open(file_polls))
#skipping the header row in file

    next(reader_polls)
    
#Building containers to store values   
    votes_cast = []
    county = []
    candidates = []
    candidate1 = []
    candidate2 = []
    candidate3 = []
    candidate4 = []
    

    for row in reader_polls:
        #creating a count of voter results
        votes_cast.append(float(row[0]))
        #building my list of candidates, if one is already counted then it skips
        if row[2] not in candidates:
            candidates.append(str(row[2]))
        #if the vote in column C was cast for a candidate, add 1 to their container
        if row[2] == "Khan":
            candidate1.append(1)
        #count how many items are in their container to reach the votes casted for candidate
            candidate1_votes = len(candidate1)
        if row[2] == "Correy":
            candidate2.append(1)
            candidate2_votes = len(candidate2)
        if row[2] == "Li":
            candidate3.append(1)
            candidate3_votes = len(candidate3)
        if row[2] == "O'Tooley":
            candidate4.append(1)
            candidate4_votes = len(candidate4)
            
#calculating the percentage of votes for each candidate
(candidate1_Percentage) = candidate1_votes/len(votes_cast)
(candidate2_Percentage) = candidate2_votes/len(votes_cast)
(candidate3_Percentage) = candidate3_votes/len(votes_cast)
(candidate4_Percentage) = candidate4_votes/len(votes_cast)

#using a conditional function, if a candidate has more items in their container(votes) than the next, they become winner
with open(file_polls) as polls:
    reader_polls = csv.reader(polls, delimiter=',')
    #I began the winner as candidate 4, O'Tooley, who will be replaced as a candidates votes are compared via conditional function
    winner = candidates[3]
    if candidate4 < candidate3:
    #winner is replaced only if the next candidate has more than the previous
        winner = candidates[2]
    if candidate3 < candidate2:
        winner = candidates[1]
    if candidate2 < candidate1:
    #the winner of the election will be under value 'winner' since I have compared all results against each other
        winner = candidates[0]

#print out all the results
print(" ")
print("Election Results")
print("------------------------------------------")
print("Total Votes Casted: ", len(votes_cast))
print("------------------------------------------")
print(candidates[0],":", '{:.1%}'.format(candidate1_Percentage),"(",candidate1_votes,")")  
print(candidates[1],":", '{:.1%}'.format(candidate2_Percentage),"(",candidate2_votes,")")
print(candidates[2],":", '{:.1%}'.format(candidate3_Percentage),"(",candidate3_votes,")")
print(candidates[3],":", '{:.1%}'.format(candidate4_Percentage),"(",candidate4_votes,")")
print("-------------------------------------------")
print("The winner of the election is ",winner, "!!!")
print("Congratulations representative ",winner,".")

#Writing output file with results
output_path_polls = os.path.join("PyPolls_Output.csv")

with open(output_path_polls, 'w', newline='') as output_data_polls:
    csvwriter_polls = csv.writer(output_data_polls, delimiter=',')
    csvwriter_polls.writerow(["Total Votes Casted: ","" , len(votes_cast)])
    csvwriter_polls.writerow([""])
    csvwriter_polls.writerow([candidates[0], '{:.1%}'.format(candidate1_Percentage),candidate1_votes])
    csvwriter_polls.writerow([candidates[1], '{:.1%}'.format(candidate2_Percentage),candidate2_votes])
    csvwriter_polls.writerow([candidates[2], '{:.1%}'.format(candidate3_Percentage),candidate3_votes])
    csvwriter_polls.writerow([candidates[3], '{:.1%}'.format(candidate4_Percentage),candidate4_votes])
    csvwriter_polls.writerow([""])
    csvwriter_polls.writerow(["The winner of the election is " + winner])
