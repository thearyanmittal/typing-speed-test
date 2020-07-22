#import modules
import random
import keyboard
import textwrap
from matplotlib import pyplot as plt
import datetime
import time
import os
from termcolor import cprint, colored
import colorama

# initialize colorama so colored text will work
colorama.init()

# define function that picks a random passage from list and counts its characters
def rand_pass(lst):
    word = random.choice(lst)
    strip_word = word.strip(" ")
    length = len(strip_word)
    first_char = word[0]
    word_info = [word, length, first_char]
    return word_info

# define function that prints a certain number of blank lines
def blank_lines(lines):
    i = 0
    while i < lines + 1:
        print("\n")
        i = i + 1

# define Stopwatch class
class Stopwatch:

    def __init__(self):
        pass

    def start(self):
        self.start_time = datetime.datetime.now()
    
    def stop(self):
        self.end_time = datetime.datetime.now()
    
    def elapsed(self):
        elapsed_time = self.end_time - self.start_time
        elapsed_secs = elapsed_time.total_seconds()
        return elapsed_secs

#possible passages
word_1 = ("Word processors evolved dramatically once they became software programs rather than dedicated machines. " + 
"They can usefully be distinguished from text editors, the category of software they evolved from. " +
"Word processing added to the text editor the ability to control type style and size, to manage lines (word wrap), " +
"to format documents into pages, and to number pages. Functions now taken for granted were added incrementally, " +
"sometimes by purchase of independent providers of add-on programs. Spell checking, grammar checking and mail merge " +
"were some of the most popular add-ons for early word processors. Word processors are also capable of hyphenation, " +
"and the management and correct positioning of footnotes and endnotes. Later desktop publishing programs were specifically " +
"designed with elaborate pre-formatted layouts for publication, offering only limited options for changing the layout, while " + 
"allowing users to import text that was written using a text editor or word processor, or type the text in themselves.")

word_2 = ("The American Civil War was fought in the United States from 1861 to 1865. The result of a long-standing controversy over slavery, " +
"war broke out in April 1861, when Confederates attacked Fort Sumter in South Carolina, shortly after President Abraham Lincoln was inaugurated. " +
"The nationalists of the Union proclaimed loyalty to the U.S. Constitution. They faced secessionists of the Confederate States, who advocated " +
"for states' rights to expand slavery. Among the 34 U.S. states in February 1861, seven Southern slave states individually declared their " +
"secession from the U.S. to form the Confederate States of America, or the South. The Confederacy grew to include eleven slave states. " +
"The Confederacy was never diplomatically recognized by the United States government, nor was it recognized by any foreign country " +
"(although the United Kingdom and France granted it belligerent status). The states that remained loyal to the U.S. (including the border " +
"states where slavery was legal) were known as the Union or the North.")

word_3 = ("An ever-growing number of complex and rigid rules plus hard-to-cope-with regulations are now being legislated from state to state. " +
"Key federal regulations were formulated by the FDA, FTC, and the CPSC. Each of these federal agencies serves a specific mission. One example: " +
"Laws sponsored by the Office of the Fair Debt Collection Practices prevent an agency from purposefully harassing clients in serious debt. The " +
"Fair Packaging and Labeling Act makes certain that protection from misleading packaging of goods is guaranteed to each buyer of goods carried " +
"in small shops as well as in large supermarkets. Products on the market must reveal the names of all ingredients on the label. Language must " +
"be in clear and precise terms that can be understood by everyone. This practice is very crucial for the lives of many people. It is prudent " +
"that we recall that the FDA specifically requires that all goods are pure, safe, and wholesome. The FDA states that all goods be produced " +
"under highly sanitary conditions. Drugs must be completely safe and must also be effective for their stated purpose. This policy applies " +
"to cosmetics that must be both safe and pure. Individuals are often totally unappreciative of the FDA's great dedication.")

word_4 = ("The recent emergence of several competitive typing websites has allowed several fast typists on computer keyboards to emerge " +
"along with new records, though these are unverifiable for the most part. Two of the most notable online records that are considered genuine " +
"are 241.82 wpm on an English text on typingzone.com by Brazilian Guilherme Sandrini (equivalent to 290.184 wpm using the traditional definition " +
"for words per minute since this site defines a word as six characters rather than five) and 256 wpm (a record caught on video) on TypeRacer " +
"by American Sean Wrona, the inaugural Ultimate Typing Championship winner, which was considered the highest ever legitimate score ever set " +
"on the site, until Wrona claimed it has been surpassed. Both of these records are essentially sprint speeds on short text selections lasting " +
"much less than one minute and were achieved on the QWERTY keyboard. Wrona also maintained 174 wpm on a 50-minute test taken on hi-games.net, " +
"another online typing website to unofficially displace Blackburn as the fastest endurance typist, although disputes might still arise over " +
"differences in the difficulty of the texts as well as Wrona's use of a modern computer keyboard as opposed to the typewriter used by Blackburn.")

word_5 = ("Self-confidence is a tricky subject for many people. For some, it’s impossible to feel good about themselves without outside " +
"validation. When you’re in a situation where the people in your life aren’t helping you to feel better about yourself, this can become a " +
"problem in your day to day life. Most insecurity stems from feelings of not being attractive or feelings of loneliness. If your insecurity " +
"doesn’t necessarily stem from a lack of interaction, but more a lack of feeling attractive, there are other options that will help you online. " +
"Sometimes the best way to put your insecurities to rest can simply be to get an honest opinion. There are multiple support groups online where " +
"you can share a picture of yourself with other members and they will give honest feedback on your appearance. In most cases, they will point " +
"out good qualities that you may have missed in yourself. But you can trust them to be honest and many members give very valuable style and " +
"posture advice to increase your attractiveness. These practical tips and unbiased opinions from supportive strangers will immediately help " +
"you feel better about yourself, and if the tips are implemented it will also improve your self-esteem in the long-run.")

word_6 = ('The scientific method is a body of techniques for investigating phenomena, acquiring new knowledge, or correcting and integrating ' +
'previous knowledge. To be termed scientific, a method of inquiry is commonly based on empirical or measurable evidence subject to specific ' +
'principles of reasoning. The Oxford Dictionaries Online defines the scientific method as "a method or procedure that has characterized ' +
'natural science since the 17th century, consisting in systematic observation, measurement, and experiment, and the formulation, testing, ' +
'and modification of hypotheses". Experiments are a procedure designed to test hypotheses. Experiments are an important tool of the scientific ' + 
'method. The method is a continuous process that begins with observations about the natural world. People are naturally inquisitive, so they ' +
'often come up with questions about things they see or hear, and they often develop ideas or hypotheses about why things are the way they are. ' +
'The best hypotheses lead to predictions that can be tested in various ways. The strongest tests of hypotheses come from carefully controlled ' +
'experiments that gather empirical data. Depending on how well additional tests match the predictions, the original hypothesis may require ' +
'refinement, alteration, expansion or even rejection. If a particular hypothesis becomes very well supported, a general theory may be developed.')

word_7 = ("The study of the cell is done on a molecular level; however, most of the processes within the cell are made up of a mixture of " +
"small organic molecules, inorganic ions, hormones, and water. Approximately 75–85% of the cell's volume is due to water making it an " +
"indispensable solvent as a result of its polarity and structure. These molecules within the cell, which operate as substrates, provide a " + 
"suitable environment for the cell to carry out metabolic reactions and signalling. The cell shape varies among the different types of " +
"organisms, and are thus then classified into two categories: eukaryotes and prokaryotes. In the case of eukaryotic cells – which are made " + 
"up of animal, plant, fungi, and protozoa cells – the shapes are generally round and spherical, while for prokaryotic cells – which are " +
"composed of bacteria and archaea – the shapes are: spherical (cocci), rods (bacillus), curved (vibrio), and spirals (spirochetes).")

word_8 = ("Limited liability companies (LLC), limited liability partnerships, and other specific types of business organization protect their " +
"owners or shareholders from business failure by doing business under a separate legal entity with certain legal protections. In contrast, " +
"unincorporated businesses or persons working on their own are usually not as protected. Corporation: The owners of a corporation have limited " +
"liability and the business has a separate legal personality from its owners. Corporations can be either government-owned or privately owned. " +
"They can organize either for profit or as nonprofit organizations. A privately owned, for-profit corporation is owned by its shareholders, " +
"who elect a board of directors to direct the corporation and hire its managerial staff. A privately owned, for-profit corporation can be " +
"either privately held by a small group of individuals, or publicly held, with publicly traded shares listed on a stock exchange.")

word_9 = ("In one study of average computer users, the average rate for transcription was 33 words per minute, and 19 words per minute for " +
"composition. In the same study, when the group was divided into \"fast\", \"moderate\" and \"slow\" groups, the average speeds were 40 wpm, " +
"35 wpm, and 23 wpm respectively. An average professional typist reaches 50 to 80 wpm, while some positions can require 80 to 95 wpm (usually " +
"the minimum required for dispatch positions and other typing jobs), and some advanced typists work at speeds above 120 wpm. Two-finger " +
"typists, sometimes also referred to as \"hunt and peck\" typists, commonly reach sustained speeds of about 37 wpm for memorized text and 27 " + 
"wpm when copying text, but in bursts may be able to reach speeds of 60 to 70 wpm. From the 1920s through the 1970s, typing speed (along " +
"with shorthand speed) was an important secretarial qualification and typing contests were popular and often publicized by typewriter " +
"companies as promotional tools.")

word_10 = ("Historically, the fundamental role of pharmacists as a healthcare practitioner was to check and distribute drugs to doctors " +
"for medication that had been prescribed to patients. In more modern times, pharmacists advise patients and health care providers on the " +
"selection, dosages, interactions, and side effects of medications, and act as a learned intermediary between a prescriber and a patient. " +
"Pharmacists monitor the health and progress of patients to ensure the safe and effective use of medication. Pharmacists may practice " +
"compounding; however, many medicines are now produced by pharmaceutical companies in a standard dosage and drug delivery form. In some " +
"jurisdictions, pharmacists have prescriptive authority to either independently prescribe under their own authority or in collaboration " +
"with a primary care physician through an agreed upon protocol.")

#put them all into a list
passages = [word_1, word_2, word_3, word_4, word_5, word_6, word_7, word_8, word_9, word_10]

# initialize variable lists for matplotlib analysis: [accuracy_list], [gross_wpm_list], [net_wpm_list], test_count
accuracy_list = []
gross_wpm_list = []
net_wpm_list = []
session_count = 0

#start the test loop
while True:
    # add one to session count
    session_count += 1

    #choose a random passage from the list and save its number of characters and first and last character
    passage, chars, first_char = rand_pass(passages)

    # welcome user and explain rules if first time (speed through if not first time)
    if session_count > 1:
        sleep = 0.5
    else:
        sleep = 3

    print("Welcome to WPM Typing Test, a test created in Python 3.7.4. Simply type the following passage and see your results!")
    time.sleep(sleep)

    print("Your WPM speed will be adjusted to correctly represent your accuracy and raw typing speed.")
    time.sleep(sleep)

    print("The time will start when you correctly type the first key.")
    time.sleep(sleep)

    print("Any extraneous characters that you type prior to correctly typing the first character will not be counted against you.")
    time.sleep(sleep)

    print("Hit 'ENTER' when you are finished to stop the time.")
    time.sleep(sleep)

    print("Good Luck! Press SPACEBAR to continue.")

    keyboard.wait('space')
    time.sleep(1)

    # separate the instructions from the passage
    blank_lines(200)

    # print the passage AND WRAP TEXT
    wrapper = textwrap.TextWrapper(width=150)
    text = wrapper.fill(text=passage)
    print(text)
    
    # start stopwatch when first key is pressed
    stopwatch = Stopwatch()

    blank_lines(2)
    cprint("—" * 150, 'cyan')
    blank_lines(2)
    
    while True:
        if keyboard.is_pressed(f"shift + {first_char}"):
            colored_arrow = colored("————>", 'magenta')
            cprint("", 'green', end= colored_arrow)
            stopwatch.start()
            break

    # get user input and stop stopwatch when user types his/her last key and hits enter
    user_input = input()
    char = str(user_input).index(first_char)
    user_input = user_input[char:]

    stopwatch.stop()

    if user_input != "":  

        # compare user input to original for accuracy rate
        blank_lines(10)

        pass_words = passage.split(" ")
        user_words = str(user_input).split(" ")
        
        errors = []

        if len(user_words) == len(pass_words):
            for i in range(len(user_words)):
                if user_words[i] != pass_words[i]:
                    errors.append(user_words[i])

        elif len(user_words) < len(pass_words):
            for i in range(len(user_words)):
                if user_words[i] != pass_words[i]:
                    errors.append(user_words[i])

            char_diff = len(pass_words) - len(user_words)
            for j in range(char_diff):
                errors.append("!")

        elif len(user_words) > len(pass_words):
            for i in range(len(pass_words)):
                if pass_words[i] != user_words[i]:
                    errors.append(user_words[i])

            char_diff = len(user_words) - len(pass_words)
            for j in range(char_diff):
                errors.append("!")

        # gross_wpm = (characters_typed / 5) / (seconds_on_stopwatch / 60) — calculate speed
        a = float(len(str(user_input).strip(" ")) / 5)
        b = float(float(stopwatch.elapsed()) / 60)
        gross_wpm = float(a / b)
        gross_wpm_round = round(gross_wpm, 0)

        # accuracy = ((words_typed - incorrect_words_typed) / words_typed) * 100) + "%"
        correct_words = len(user_words) - len(errors)

        if correct_words < 0:
            correct_words = len(pass_words) - len(errors)
            accuracy = correct_words / len(pass_words)
        elif correct_words >= 0:
            accuracy = correct_words / len(user_words)
        
        accuracy_round = round(accuracy * 100, 1)

        # net_wpm = accuracy * gross_wpm — factor in errors to speed calculation
        net_wpm = (accuracy_round / 100) * gross_wpm_round
        net_wpm_round = round(net_wpm, 1)

        # if one does not exist, create file and save results by line
        with open("stats_file.txt", "a+") as stats_file:
            stats_file.write(f"{gross_wpm_round} {accuracy_round} {net_wpm_round}")
            stats_file.write('\n')

        # define gross_wpm_list, accuracy_list, net_wpm_list as respective indices of file lines
        stats_file = open('stats_file.txt', 'r')
        for i in range(len(open('stats_file.txt').readlines())):
            line = stats_file.readline(i + 100).strip('\n')

            g = line.split(' ')[0]
            a = line.split(' ')[1]
            n = line.split(' ')[2]

            gross_wpm_list.append(round(float(g), 1))
            accuracy_list.append(round(float(a), 1))
            net_wpm_list.append(round(float(n), 1))

        # display results
        blank_lines(100)
        
        cprint("Your gross (raw) WPM typing speed (not adjusted for accuracy) was:", attrs= ['underline'], end= " ")
        
        time.sleep(2)

        if gross_wpm_round <= 35:
            cprint(f"{gross_wpm_round}", 'red')
        elif gross_wpm_round >= 36 and gross_wpm_round <= 59:
            cprint(f"{gross_wpm_round}", 'yellow')
        elif gross_wpm_round >= 60:
            cprint(f"{gross_wpm_round}", 'green')

        time.sleep(1)
        blank_lines(1)

        cprint("Your accuracy was:", attrs= ['underline'], end= " ")

        time.sleep(2)

        if accuracy_round <= 69:
            cprint(f"{accuracy_round}" + "%", 'red')
        elif accuracy_round >= 70 and accuracy_round <= 89:
            cprint(f"{accuracy_round}" + "%", 'yellow')
        elif accuracy_round >= 90:
            cprint(f"{accuracy_round}" + "%", 'green')
        
        time.sleep(1)
        blank_lines(1)

        cprint("YOUR ADJUSTED WPM TYPING SPEED IS:", attrs= ['underline', 'bold', 'blink'], end=" ")

        time.sleep(2)

        if net_wpm <= 35:
            cprint(f"{round(net_wpm, 0)}", 'red')
        elif net_wpm >= 36 and net_wpm <= 59:
            cprint(f"{round(net_wpm, 0)}", 'yellow')
        elif net_wpm >= 60:
            cprint(f"{round(net_wpm, 0)}", 'green')

        time.sleep(1)
        blank_lines(10)

        # ask to show graph of results over time if two or more tests have been taken (overall)
        test_count = len(open('stats_file.txt').readlines())

        if test_count >= 2: #if the number of lines (i.e. entries) in the .txt file is more than 1 test
            while True:
                graph_response = input("Would you like to see a graph of your stats over time? Enter 'y' for yes or 'n' for no.\n")
                if graph_response in ('y', 'n'):
                    break
                print("Please enter either y or n.")
            if graph_response == 'y':
                # define function to view graph stats
                def view_graph(graph_number):
                    if graph_number == '1':
                        x_axis = []
                        for i in range(len(gross_wpm_list)):
                            x_axis.append(i + 1)
                        
                        plt.plot(x_axis, gross_wpm_list, 'b^:')
                        plt.title("Gross WPM Over Time")
                        plt.xlabel("Test Number")
                        plt.ylabel("Gross WPM")

                        plt.show()
                    elif graph_number == '2':
                        x_axis = []
                        for i in range(len(accuracy_list)):
                            x_axis.append(i + 1)

                        plt.plot(x_axis, accuracy_list, 'ro--')
                        plt.title("Accuracy Rate Over Time")
                        plt.xlabel("Test Number")
                        plt.ylabel("Accuracy Rate (%)")

                        plt.show()
                    elif graph_number == '3':
                        x_axis = []
                        for i in range(len(net_wpm_list)):
                            x_axis.append(i + 1)

                        plt.plot(x_axis, net_wpm_list, 'ks-')
                        plt.title("Net WPM Over Time")
                        plt.xlabel("Test Number")
                        plt.ylabel("Net WPM")

                        plt.show()
                    elif graph_number == '4':
                        # continue to next part of program
                        pass

        
                while True:
                    which_graph = input("Which stat would you like to observe? Enter '1' for gross WPM, '2' for accuracy, or '3' for net WPM.\n")
                    if which_graph in ('1', '2', '3'):
                        break
                    print("Please enter either 1, 2, or 3.")
                
                view_graph(which_graph)

                while True:
                    which_graph = input("Would you like to view another stat? Enter 1 for gross WPM, 2 for accuracy, 3 for net WPM, or 4 to continue. \n")
                    if which_graph in ('1', '2', '3', '4'):
                        break
                
                view_graph(which_graph)

                if which_graph != '4':
                    while True:
                        which_graph = input("Would you like to view another stat? Enter 1 for gross WPM, 2 for accuracy, 3 for net WPM, or 4 to continue. \n")
                        if which_graph in ('1', '2', '3', '4'):
                            break
                    
                    view_graph(which_graph)

        # ask to test again
        while True:
            run_again = input("Would you like to test again? Enter 'y' for yes or 'n' for no.\n")
            if run_again in ('y', 'n'):
                break
            print("Please enter either y or n.")
        if run_again == 'y':
            blank_lines(200)
            continue
        else:
            while True:
                mad_libs = input("Would you like to play another Python game called Mad Libs? Enter 'y' for yes or 'n' for no.\n")
                if mad_libs in ('y', 'n'):
                    break
                print("Please enter either 'y' or 'n'.")
            if mad_libs == 'y':
                os.startfile("C:\\Users\\Aryan Mittal\\Documents\\Python\\mad_libs.py")
            else:
                input()
                break
    else:
        while True:
            restart_input = input("You did not enter any text. Please enter 'y' to restart or 'n' to end the application.\n")
            if restart_input in ('y', 'n'):
                break
            print("Please enter either 'y' or 'n'.")
        if restart_input == 'y':
            continue
        else:
            break