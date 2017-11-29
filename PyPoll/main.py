import os
import csv

# I've set up a raw data folder and a results folder
# The raw data folder will hold the input .csv files
# The program will create a summary with each input file
# The summary .txt files will be written to the results folder

# Work on each file in the input_files folder
for filename in os.listdir("raw data"):
    
    csv_path = os.path.join("raw data", filename)
    with open(csv_path, newline="") as csv_file:
        
        # Turn the .csv file into a csv reader
        file_reader = csv.reader(csv_file, delimiter=",")
    
        # Skip header row
        next(file_reader)
    
        # I haven't found a way to work with index of rows in a csv reader
        # So I will convert the csv reader to a list of lists to work on it
        # Each row in the csv reader represents a single ballot
        ballot_box = list(file_reader)

        # Keep candidate names and respective votes in lists, keyed on index
        candidate_names = []
        candidate_votes = []

        # Check each ballot
        for ballot in ballot_box:

            # If the candidate is not on the scoreboard yet
                # Add the candidate's name to the scoreboard
                # Give the candidate his or her first vote
            # If the candidate is already on the scoreboard
                # Find the index of his/her name in the name list
                    # Find the corresponding index in the vote count list
                        # Add one more vote to that corresponding vote count
            if ballot[2] not in candidate_names:
                candidate_names.append(ballot[2])
                candidate_votes.append(1)
            else:
                candidate_votes[candidate_names.index(ballot[2])] += 1

        # Total votes is just the count of all ballots in ballot_box
            # i.e. length of the outer list
            # which also equals the sum of all the votes
        tot_votes = len(ballot_box)

        # We can make the scoreboard a list of dictionaries for organization
        scoreboard = []

        for i in range(1, 1 + len(candidate_names)):
            scoreboard.append({
                "name": candidate_names[i - 1],
                "vote count": candidate_votes[i - 1],
                "percentage": str(round(float(candidate_votes[i - 1]) / tot_votes * 100, 2)) + "%"
            })

        # Find the winner
        winner = candidate_names[candidate_votes.index(max(candidate_votes))]

        # Now print it out
        print("Election Results from ")
        print(filename)
        print("---------------------------")
        print("Total Votes: " + str(tot_votes))
        print("---------------------------")

        for candidate in scoreboard:
            print(candidate["name"] + ": " 
                  + candidate["percentage"] + " ("
                  + str(candidate["vote count"]) + ")"
                 )

        print("---------------------------")
        print("Winner: " + winner)
        print("---------------------------")
        print("")
        print("")
        
        # Write the output .txt file for each input file
        output_file_name = filename + "_results.txt"
        output_path = os.path.join("results", output_file_name)
        summary_file = open(output_path, "w")
        summary_file.write(
            "Election Results from " + "\n"
            + filename + "\n"
            + "---------------------------" + "\n"
            + "Total Votes: " + str(tot_votes) + "\n"
            + "---------------------------" + "\n"
        )
        for candidate in scoreboard:
            summary_file.write(candidate["name"] + ": " 
                    + candidate["percentage"] + " ("
                    + str(candidate["vote count"]) + ")" + "\n"
                    )
        summary_file.write(
            "---------------------------" + "\n"
            + "Winner: " + winner + "\n"
            + "---------------------------" + "\n"
        )
        summary_file.close()