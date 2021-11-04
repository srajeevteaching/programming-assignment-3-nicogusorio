#if quidditch chosen, inputs are: goals of team A and B, and whether or not a team caught snitch
                #if quarterback chosen, inputs are: attempts, completions, touchdown passes, interceptions, passing yards
                #if gymnast score chosen, inputs are: 5 execution scores and a difficulty score.
# Program Outputs:
                #if quidditch chosen: total score of each team and overall total
                #if quaterback chosen: rating
                #if gymnast chosen: score

# Comments have been added explaining each step (algorithm)

#FUNCTIONS DECOMPOSITION
#quidditch scoring
#parameters will be obtained in quidditch handler. It returns the score for team A and team B.
def quidditch_score(goals_A, goals_B, snitchA, snitchB):
    team_A = (goals_A * 10) + snitchA
    team_B = (goals_B * 10) + snitchB
    return team_A, team_B

#football rating
#full, simplified equation, takes 5 parameters that will be obtained in football handler
def quarterback_rating(attempts, completions, touchdown_passes, interceptions, passing_yards):
    rating = 100*((5*((completions/attempts)-0.3) + 0.25*((passing_yards/attempts)-3) + 20*(touchdown_passes/attempts)+ (2.375 - (25*(interceptions/attempts))))/6)
    return rating

#gymnast scoring
#Gymnastic scores will be stored in a list. To calculate average, sum function will add integers in list. It will then
# be divided by the length of the list.
# final result will be the average plus the difficulty score
def gymnastic_score(gymnastic_scores, difficulty):
    average = sum(gymnastic_scores) / len(gymnastic_scores)
    final = difficulty + average
    return final

# checking if value inputted is an integer. Function isnumeric is utilized.
# float values are not meant to be used. If it is an int, the variable will be converted from string to int. If not, it
# is assigned a value of -1.
def is_int(a):
    if a.isnumeric():
        a = int(a)
        return a
    else:
        return -1

#quidditch handler
def quidditch_handler():
    print("\u0332".join("Quidditch Score Total"))
    teamAgoals = input("+ Please enter the number of goals scored by first team (Team A): ")
    # Input is verified to check if it is an int.
    teamAgoals = is_int(teamAgoals)
    teamBgoals = input("+ Please enter the number of goals scored by second team (Team B): ")
    # Input is verified to check if it is an int.
    teamBgoals = is_int(teamBgoals)
    # if the value is less than 0, it means that it is either a non integer value entered, or that it is a negative
    # value. Either are not allowed.
    if teamBgoals < 0 or teamAgoals < 0:
        print("An erroneous value was entered!")
    # If not, it is asked for user to input if the team caught snitch
    else:
        snitchA = input("+ Did Team A catch the snitch? Please enter yes or no: ")
        snitchA = snitchA.strip().lower()
        if snitchA == 'yes':
            snitch_caughtA = 30
            snitch_caughtB = 0
        elif snitchA == 'no':
            # If team A did not catch it, then team B might have.
            snitch_caughtA = 0
            snitchB = input("+ Did Team B catch the snitch? Please enter yes or no: ")
            snitchB = snitchB.strip().lower()
            if snitchB == 'yes':
                snitch_caughtB = 30
            elif snitchB == 'no':
                snitch_caughtB = 0
            # If an input that is not 'yes' or 'no' is entered, snitch_caught = 0
            else:
                print("Erroneous answer for Snitch was entered. Final score will not include snitch.")
                snitch_caughtB = 0
        else:
            print("Erroneous answer for Snitch was entered. Final scored will not include snitch.")
            snitch_caughtA = 0
            snitch_caughtB = 0
        # function quidditch_score is called
        scores = quidditch_score(teamAgoals, teamBgoals, snitch_caughtA, snitch_caughtB)
        print ("-> Team A score = ", scores[0], "\n-> Team B score = ", scores[1], "\n-> Total = ", sum(scores))

#football handler
def football_handler():
    print("\u0332".join("Quarterback Rating"))
    attempts = input("+ Input the number of passing attempts: ")
    # What follows is a series of lines validating whether or not the input is an integer or not using function is_int
    attempts = is_int(attempts)
    completions = input("+ Input the number of completed passing attempts: ")
    completions = is_int(completions)
    touchdown_passes = input("+ Input the number of passes for a touchdown: ")
    touchdown_passes = is_int(touchdown_passes)
    interceptions = input("+ Input the number of times ball was intercepted: ")
    interceptions = is_int(interceptions)
    passing_yards = input("+ Input how long a pass was: ")
    passing_yards = is_int(passing_yards)
    # if they are not integers, function is_int return value of -1, so program outputs message saying value was wrongly
    # entered
    if attempts == -1 or completions == -1 or touchdown_passes == -1 or interceptions == -1 or passing_yards == -1:
        print("An erroneous value was entered. Quarterback rating is 0.")
    # in calculation that will be used from function quarterback_rating, everything is being divided by attempts.
    # Divisions by 0 are not possible, so program outputs that input is not valid.
    elif attempts == 0:
        print("Calculation cannot be done. Division by 0 is not possible, so quarterback rating is 0.")
    else:
        # everything is entered correctly, so function quarter_back rating is called.
        rating = quarterback_rating(attempts, completions, touchdown_passes, interceptions, passing_yards)
        print ("Quarterback Rating = ", round(rating,2))
        # 158.3 is a perfect passer.
        if rating == 158.3:
            print ("Rating = 158.3. Perfect Passer!")

#gymnast handler
def gymnastic_handler():
    print("\u0332".join("Gymnast Score"))
    # list is created
    gymnastic_scores = list()
    print("Please enter the 5 given execution numbers")
    # for loop so user enters the 5 execution scores
    for i in range(5):
        execution = input(" -> ")
        # input validation
        if execution.isnumeric():
            execution = int(execution)
            # input validation ensuring value is between 0 and 10
            while execution < 0 or execution > 10:
                execution = int(input("Input a valid execution. It must be from 0 to 10! \n -> "))
            # score added to list
            gymnastic_scores.append(execution)
        # if input is not an integer, error message outputted
        else:
            print("Error. Value entered above will not be included as one of the gymnastic scores.")
    # if more than two scores were correctly entered, then the highest and lowest values are removed from list.
    if len(gymnastic_scores) > 2:
        gymnastic_scores.remove(min(gymnastic_scores))
        gymnastic_scores.remove(max(gymnastic_scores))
        print("The gymnast's scores that will be used to obtain final score are: ", gymnastic_scores)
        # difficulty score input
        difficulty = input("Please enter the difficulty score: ")
        # input validation
        if difficulty.isnumeric():
            difficulty = int(difficulty)
            # once again, checking if it is between 0 and 10
            while difficulty < 0 or difficulty > 10:
                difficulty = int(input("Please enter a valid the difficulty score. Must be from 0 to 10!: "))
                if difficulty >= 0 and difficulty <= 10:
                    print("Score was ", gymnastic_score(gymnastic_scores, difficulty))
                    # score of gymnast output, calling function gymnastic_score.
                else:
                    continue
                    # loop will keep running unless a correct value is entered, meaning between 0 and 10.
            else:
                print("Gymnast score was ", gymnastic_score(gymnastic_scores, difficulty))
        else:
            print("Erroneous value. Score of gymnast is 0.")
    # Since many erroneous values of execution scores where entered, removing max and min would lead to an empty list,
    # meaning no values to evaluate gymnast.
    else:
        print("Too many erroneous values entered. Score of gymnast is 0.")

#menu
def menu():
    selection = 0
    #Table to show user the options to choose from
    while selection <1 or selection > 3:
        print("\t\tSports Rating and Scoring\n"
              "\t\t=========================\n"
              "\t\t1. Quidditch Score Total\n"
              "\t\t2. Quarterback Rating\n"
              "\t\t3. Gymnast Score\n")
        selection = int(input("\tEnter your numerical selection: "))
    return selection

#main(): driver
def main():
    option = menu()
    #call appropriate sport handler based on the value of option entered by user
    if option == 1:
        quidditch_handler()
    elif option == 2:
        football_handler()
    else:
        gymnastic_handler()
    print("Thank you!")
main()
# calling main function, which drives program.