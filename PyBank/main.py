import os
import csv

# I've set up an input_files folder and an output_files folder
# The input_files folder will hold the input .csv files
# The program will create a summary with each input file
# The summary .txt files will be written to the output_files folder

# Work on each file in the input_files folder
for filename in os.listdir("input_files"):
    
    csv_path = os.path.join("input_files", filename)
    with open(csv_path, newline="") as csv_file:
        
        # Turn the .csv file into a csv reader
        file_reader = csv.reader(csv_file, delimiter=",")
    
        # Skip header row
        next(file_reader)
    
        # I haven't found a way to work with index of rows in a csv reader
        # So I will convert the csv reader to a list of lists to work on it
        working_file = list(file_reader)
    
        # Keep running tallies of summary values
        total_months = 0
        total_rev = 0
        greatest_inc = 0
        greatest_dec = 0

        # Record the revenue changes in a list to calculate average
        delta_rev = []

        for item in working_file:

            # Update tallies of months and revenue
            total_months += 1
            total_rev += float(item[1])

            # Record the monthly change for each month
            # Update monthly change list, but no for the first month
            (working_file.index(item) + 1)
            if working_file.index(item) == 0:
                item.append(0)
            else:
                item.append(float(item[1]) - float(working_file[working_file.index(item) - 1][1]))
                delta_rev.append(item[2])
        
            # Check to see if the month's change is the new greatest increase
            # If it is, update it
            if float(item[2]) > greatest_inc:
                inc_summary = item[0] + " ($" + str(item[2])

            # Check to see if the month's change is the new greatest decrease
            # If it is, update it
            if float(item[2]) < greatest_dec:
                dec_summary = item[0] + " ($" + str(item[2])

        # Calculate the average revenue change
        avg_rev_change = sum(delta_rev)/len(delta_rev)

        # Now print everything
        print("Financial Analysis")
        print("-------------------------------")
        print("Total Months: " + str(total_months))
        print("Total Revenue: $" + str(total_rev))
        print("Average Revenue Change: $" + str(avg_rev_change))
        print("Greatest Increase in Revenue: " + inc_summary + ")")
        print("Greatest Decrease in Revenue: " + dec_summary + ")") 
        print("")
        print("")
    
    # Write the output .txt file for each input file
    output_file_name = filename + "_summary.txt"
    output_path = os.path.join("output_files", output_file_name)
    summary_file = open(output_path, "w")
    summary_file.write(
        "Financial Analysis" + "\n"
        + "-------------------------------" + "\n"
        + "Total Months: " + str(total_months) + "\n"
        + "Total Revenue: $" + str(total_rev) + "\n"
        + "Average Revenue Change: $" + str(avg_rev_change) + "\n"
        + "Greatest Increase in Revenue: " + inc_summary + ")" + "\n"
        + "Greatest Decrease in Revenue: " + dec_summary + ")"
    )
    summary_file.close()