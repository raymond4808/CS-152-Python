# Assignment 9 due 11/16/2022
# Raymond Cheung
# Given a list strings containing
# team1, slash, team2, space, score1, dash, score2
# Print a series of tables in different formats
# There is always a space between team2 and the first score
# There may or may not be any spaces between the other six items
def get_first_team(score_line):
    # Step 1 Part 1 Fruitful function that returns function stated name in str form with 1 parameter passed
    # returns first team name with no extra spaces or other characters
    # Note this doesn't currently work #Edited to work
    pos = score_line.find('/')
    spaceRemoval = score_line[:pos].strip()
    return spaceRemoval


def get_second_team(secondScore_line):
    # Step 1 Part 2 Fruitful function that returns function stated name in str form with 1 parameter passed
    slashPos = secondScore_line.find('/')
    dashPos = secondScore_line.find('-')
    secondTeamSpaceRemover = secondScore_line[slashPos + 1:dashPos].strip()
    spacefinder = secondTeamSpaceRemover.rfind(" ")
    secondTeamScoreRemover = secondTeamSpaceRemover[:spacefinder]
    return secondTeamScoreRemover


def get_first_score(firstScore):
    # Step 1 Part 3 Fruitful function that returns function stated name in str form with 1 parameter passed
    slashPosFirstScore = firstScore.find('/')
    dashPosFirstS = firstScore.find("-")
    firstScoreStrip = firstScore[slashPosFirstScore:dashPosFirstS].strip()
    midSpaceFinder = firstScoreStrip.rfind(" ")
    finalFirstScoreStripe = firstScoreStrip[midSpaceFinder:]
    return finalFirstScoreStripe


def get_second_score(secondScore):
    # Step 1 Part 4 Fruitful function that returns function stated name in str form with 1 parameter passed
    pos = secondScore.find("-")
    secondScoreStrip = secondScore[pos + 1:].strip()
    return secondScoreStrip


def main():
    score_lines = ['Atlanta / Chicago 24-10',
                   'Chicago /Cincinnati   6-9 ',
                   'Cleveland/  Seattle 14-3',
                   '   Seattle/Miami 17 - 14',
                   'Kansas City / Miami 33-28',
                   'Tampa Bay / Kansas City 21-9',
                   ' Green Bay / Tampa Bay 12 -3',
                   'Las Vegas/ Green Bay 44- 28',
                   'Dallas/Houston 27    -   30',
                   'Buffalo    /New England 19-16']
    # Print the table without formatting

    for cycleTeamLeft in score_lines:
        print(get_first_team(cycleTeamLeft).ljust(0))
    # Step 2 Print just the first teams, all left justified

    for cycleTeamRight in score_lines:
        print(get_first_team(cycleTeamRight).rjust(15))
    # Step 3 Print just the first teams, all right justified with additional print statement for spacing
    print()


    for a_score_line in score_lines:
        # below are function calls for me to check appropriate values
        # print(a_score_line) #prints element in prompt
        # print(get_first_team(a_score_line)) #print first team
        # print(get_second_team(a_score_line)) #print second team
        # print(get_first_score(a_score_line)) #print first part of score
        # print(get_second_score(a_score_line)) #print second half of score
        # print() #leaves spacing between values
        lengthSecondTeam = len(get_second_team(a_score_line))
        lengthFirstTeam = len(get_first_team(a_score_line))

        print(get_first_team(a_score_line).ljust(0), get_first_score(a_score_line).rjust(lengthSecondTeam), " ")
        print(get_second_team(a_score_line).ljust(0), get_second_score(a_score_line).rjust(lengthFirstTeam), " ")
        print()
        # Step 4 Prints first and second team name left justified and their scores right justified with blank print statement at the end for spacer

        if int(get_first_score(a_score_line)) > int(get_second_score(a_score_line)):
            print("Winner: " + get_first_team(a_score_line))
        else:
            print("Winner: " + get_second_team(a_score_line))
        # Step 5 Print which team won each game
        print()

    # Extra Credit | Compute and print the teams with the highest and lowest scores, and their corresponding scores.
    highscore = 0
    scorecomparer = 0
    for highestScore in score_lines:
        if scorecomparer > highscore:
            highscore = scorecomparer
        elif int(get_first_score(highestScore)) > int(get_second_score(highestScore)):
            scorecomparer = int(get_first_score(highestScore))
        elif int(get_first_score(highestScore)) < int(get_second_score(highestScore)):
            scorecomparer = int(get_second_score(highestScore))
        elif highscore > scorecomparer:
            highscore = highscore
    for team in score_lines:
        if str(highscore) in team:
            highScoreTeam = (get_first_team(team))
    print("The highest scoring team was " + highScoreTeam + " with a score of " + str(highscore))
    # highest score function Extra Credit (Working)

    """lowestScore = 999
    scorecomparer = 999
    for lowestScores in score_lines:
        if scorecomparer < lowestScore:
            lowestScore = scorecomparer
        elif int(get_first_score(lowestScores)) < int(get_second_score(lowestScores)):
            scorecomparer = int(get_first_score(lowestScores))
        elif int(get_first_score(lowestScores)) > int(get_second_score(lowestScores)):
            scorecomparer = int(get_second_score(lowestScores))
        elif lowestScore < scorecomparer:
            lowestScore = lowestScore

    for teams in score_lines:
        if str(lowestScore) in teams:
            lowScoreTeam = (get_second_team(teams))
            print("The lowest scoring team was " + lowScoreTeam + " with a score of " + str(lowestScore))"""
    # Lowest score function Extra Credit (DOESN'T WORK)


main()
