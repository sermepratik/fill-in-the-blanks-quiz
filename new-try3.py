#IPND stage 2 Project

print "\nHello! Lets play a game?\n"
print "Lets see how well you know Game of Thrones.\n "
print "You can choose noob, easy, medium, hard or master.\n"

#this is the list of blanks that appear in the paragraphs.
blanks = ["___1___","___2___","___3___","___4___"]

#all paragraphs have 4 main blanks. we ask for user input till all the blanks get filled. also we limit the number of guesses user gets to 5.

#These are the individual strings for noob easy medium hard and master.
questions_noob = '''Game of Thrones premieres every ___1___ night on HBO. ___2___ is the author of this expansive book series.
___3___ was the most sought after casting decision for the creators. When they cast ___4___ for the role of ___3___ Lannister, they
felt like they were on to someThing.'''

questions_easy = '''The Starks have their castle at ___1___ in the North. Lord ___2___ Stark is the current head of the family.
Lord ___2___ and the King Robert Baratheon are old friends. Lady Catelyn and Lord ___2___ have ___3___ trueborn children and there is also
one bastard at the ___1___ castle named Jon Snow. ___4___ is the eldest and heir to ___1___.'''

questions_medium = '''The Starks and the Lannisters are great rivals in the Seven Kingdoms. Ser ___1___ Lannister was the youngest Kingsguard
in history. Ned and ___1___ respect and despise each other at the same time. The coolest character of all time is ___2___ Lannister who is
also known as the ___3___. The ___3___ is infamous for being a dwarf but a tall and clever talker. Queen ___4___ Baratheon is wife to
King Robert but not the mother of his children.'''

questions_hard = '''Across the Narrow Sea, we have the exiled, formerly royal, family - the last surviving ___1___s. ___2___ is mocked by all
as the Beggar King. ___3___ ___1___ who is his baby sister, just wants to go back to the house with the red door.
But, ___3___ is being married off to a ___4___ warlord - Khal Drogo who commands a huge army of 50,000 ___4___ screamers. ___2___ hopes that
Khal Drogo will help him to invade Westeros since he sold the Khal a beautiful bride: his sister ___3___.'''

questions_master = '''After the tragic incident befalling her son, ___1___ Stark arrests Tyrion the Imp Lannister based on ___2___ evidence.
This leads to ___3___ Lannister summoning his armies to set fire to her homeland of ___4___. In King's Landing, the Small Council is already plotting
to remove Ned Stark as the Hand of the King. Ned Stark sends Beric Dondarion to ___4___ to bring to the false knight Gregor Clegane, the
King's Justice.'''

#These are the individual lists for correct answers. We compare user input answer to These lists.
answers_list_noob = ["Sunday","GRRM","Tyrion","Peter Dinklage"]
answers_list_easy = ["Winterfell", "Eddard", "five", "Robb"]
answers_list_medium = ["Jamie", "Tyrion", "Imp", "Cersei"]
answers_list_hard = ["Targaryen", "Viserys", "Daenerys", "Dothraki"]
answers_list_master = ["Catelyn", "circumstantial", "Tywin", "Riverrun"]

#this is the list of the difficulty levels we have available to play.
user_level_list = ["noob", "easy","medium","hard", "master"]

user_level = raw_input("Type in your difficulty level: ")

#This function takes in the input string from user for the difficulty level and returns corresponding list as output.
def difficulty_level(user_level):
    '''
    Takes in user input for the level and gives the corresponding string or paragraphs.
    '''

    if user_level not in user_level_list:
        print "Not a valid input. Please enter a valid input."
    else:
        if user_level == "noob":
            return questions_noob
        elif user_level == "easy":
            return questions_easy
        elif user_level == "medium":
            return questions_medium
        elif user_level == "hard":
            return questions_hard
        elif user_level == "master":
            return questions_master
        pass

#print difficulty_level(user_level)

#This function takes difficulty level string as input and returns corresponding list of answers for that level.
def relate_answer(user_level):
    '''
    Takes in user input for level and gives the corresponding list of answers.
    '''
    if difficulty_level(user_level) == questions_noob:
        return answers_list_noob
    if difficulty_level(user_level) == questions_easy:
        return answers_list_easy
    if difficulty_level(user_level) == questions_medium:
        return answers_list_medium
    if difficulty_level(user_level) == questions_hard:
        return answers_list_hard
    if difficulty_level(user_level) == questions_master:
        return answers_list_master
    pass

#print relate_answer(user_level)

#This function has inputs for the given answers by user, the correct answers from our corresponding list and the index in that list.
#It gives output right or wrong depending on the answers.
def check_answer(user_answer, answers_list, answers_index):
    '''
    This is used to validate user answers with our correct answers list.
    '''

    if user_answer == answers_list[answers_index]:
        return "Correct"
    return "Wrong"
    pass


#print check_answer(user_answer,another_variable,answers)

#This is our play function which doesn't take any inputs. It calls the other functions and uses their input-output to give the results.
def play():
    '''
    This is the main function which allows to play the game/quiz.
    It calls the previous functions we have written.
    '''
    quiz = difficulty_level(user_level)         #gives the correct paragraph according to user input.
    print 
    print quiz
    print "\nYou will get maximum 5 guesses for each blank. Good luck.\n"
    answers_list = relate_answer(user_level)    #ensures we work in the proper list of answers.
    blanks_index = 0                            #initialize variables so it doesn't give error later on.
    answers_index = 0                           #initialize variables so it doesn't give error later on.
    number_of_guesses = 5                       #initialize variables so it doesn't give error later on.
    guesses_limit = 0                           #initialize variables so it avoids magic numbers.

    while blanks_index < len(blanks):   #This loop executes so long as number of blanks are not replaced.
        user_answer = raw_input("type in your answer for " + blanks[blanks_index] + ": ")
        if check_answer(user_answer,answers_list,answers_index) == "Correct":
            print "nice job! that is the right answer!\n"
            quiz = quiz. replace(blanks[blanks_index],user_answer)
            blanks_index += 1
            answers_index += 1
            number_of_guesses = 5
            print quiz
            if blanks_index == len(blanks):
                print "Congratulations! You win!"
        else:
            number_of_guesses -= 1
            if number_of_guesses == guesses_limit:
                print "Game over!"
                break
            elif number_of_guesses < guesses_limit:
                print "invalid"
                #raise IOError('refusenik user')
                break
            else:
                print "please try again."
                print "You have " + str(number_of_guesses) + " guesses left."

    #print "Congratulations! You win."

play()
