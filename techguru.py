from subprocess import Popen


dict = {
    "subject": ["maths", "coding", "english"],
    "maths": ["logic","geometry","number"],
    "coding": ["html","css","python"],
    "english": ["models","tense","part_of_speech"],
    "songs": ["sad","party","romantic"],
    "movies": ["action", "drama", "comedy"]
}

user = raw_input("Hello\n")
user = raw_input("how are you?\n")
user1 = raw_input("Are you a student?['yes', 'no']\n")
if user1 == "no":
    user8 = raw_input("Would you like to try?\n['song','movies','literature']\n")
    if user8 == "song":
        user8 = raw_input("Which Category of songs you want to listen?\n['hollywood','bollywood']\n")
        if user8 == "hollywood":
            user9 = raw_input("How is your mood?\n['sad', 'party', 'romantic']\n")
            if user9 == dict["songs"][0]:
                Popen(['google-chrome', "https://www.youtube.com/watch?v=0G3_kG5FFfQ"])
            if user9 == dict["songs"][1]:
                Popen(['google-chrome', "https://www.youtube.com/watch?v=4XpDdIISlYo"])
            if user9 == dict["songs"][2]:
                Popen(['google-chrome', 'https://www.youtube.com/watch?v=AJtDXIazrMo'])
        elif user8 == "bollywood":
            user9 = raw_input("How is your mood?\n['sad', 'party', 'romantic']\n")
            if user9 == dict["songs"][0]:
                Popen(['google-chrome', "https://www.youtube.com/watch?v=o5K_S1wd_CE"])
            elif user9 == dict["songs"][1]:
                Popen(['google-chrome', "https://www.youtube.com/watch?v=Wr2NN4VQ1nI"])
            elif user9 == dict["songs"][2]:
                Popen(['google-chrome', 'https://www.youtube.com/watch?v=wqoPZnreeSE'])
        else:
            user_p = raw_input("Are you looking for something else, let me show you google page?['yes','no']\n")
            if user_p == "yes":
                Popen(['google-chrome', "https://www.google.co.in/?gfe_rd=cr&ei=uDI9WdCfD43z8AfdzrPQAQ&gws_rd=ssl"])
            exit()


    elif user8 == "movies":
        user8 = raw_input("Which Category of movies you would like to watch?\n['hollywood','bollywood']\n")
        if user8 == "hollywood":
            user9 = raw_input("Category of movies?\n['action', 'drama', 'comedy']\n")
            if user9 == dict["movies"][0]:
                Popen(['google-chrome', "https://www.youtube.com/watch?v=1eEV6Dv_B20"])
            elif user9 == dict["movies"][1]:
                Popen(['google-chrome', "https://www.youtube.com/watch?v=ErPvMNUG4DE"])
            elif user9 == dict["movies"][2]:
                Popen(['google-chrome', 'https://www.youtube.com/watch?v=9cQN3abDaK4'])
        elif user8 == "bollywood":
            user9 = raw_input("How is your mood?\n['action', 'drama', 'comedy']\n")
            if user9 == dict["songs"][0]:
                Popen(['google-chrome', "https://www.youtube.com/watch?v=g8xTqJe9_jQ"])
            elif user9 == dict["songs"][1]:
                Popen(['google-chrome', "https://www.youtube.com/watch?v=imcYJdy_5fQ"])
            elif user9 == dict["songs"][2]:
                Popen(['google-chrome', 'https://www.youtube.com/watch?v=WIasaidimGI'])
        else:
            user_p = raw_input("Are you looking for something else, let me show you google page?['yes','no']\n")
            if user_p == "yes":
                Popen(['google-chrome', "https://www.google.co.in/?gfe_rd=cr&ei=uDI9WdCfD43z8AfdzrPQAQ&gws_rd=ssl"])
            exit()

    elif user8 == "literature":
        user8 = raw_input("Which Category of literature you want to study?\n['novel','story','blog']\n")
        if user8 == "novel":
            Popen(['google-chrome', "https://www.theguardian.com/books/2015/aug/17/the-100-best-novels-written-in-english-the-full-list"])
        elif user8 == "story":
            Popen(['google-chrome', "https://mic.com/articles/90453/14-brilliant-pieces-of-literature-you-can-read-in-the-time-it-takes-to-eat-lunch#.mcKN5TtWx"])
        elif user8 == "blog":
            Popen(['google-chrome', "https://medium.com/@CyanideBlue/why-im-so-afraid-of-my-own-body-7f2b1755a9df"])
        else:
            user_p = raw_input("Are you looking for something else, let me show you google page?['yes','no']\n")
            if user_p == "yes":
                Popen(['google-chrome', "https://www.google.co.in/?gfe_rd=cr&ei=uDI9WdCfD43z8AfdzrPQAQ&gws_rd=ssl"])
            exit()

    else:
        print "Are you looking for something else, let me show you google page?"
        Popen(['google-chrome', "https://www.google.co.in/?gfe_rd=cr&ei=uDI9WdCfD43z8AfdzrPQAQ&gws_rd=ssl"])
        exit()

user2 = raw_input("Do you need help in study['yes', 'no']\n")
if user2 == "no":
    print "Are you looking for something else, let me show you google page?"
    Popen(['google-chrome', "https://www.google.co.in/?gfe_rd=cr&ei=uDI9WdCfD43z8AfdzrPQAQ&gws_rd=ssl"])
    exit()
user3 =raw_input("you need to select one subject\n['Maths', 'English', 'Coding']\n")

if user3 == dict["subject"][0]:
    user4 = raw_input("Which topic you want to learn?\n['Logic','Geometry','Number']\n")
    if user4 == dict["maths"][0]:
       user5 = raw_input("You want to learn from theory or videos?\n")
       if user5 == "theory":
           print Popen(['google-chrome', 'http://www.personal.psu.edu/t20/papers/philmath/'])
       elif user5 == "videos":
           Popen(['google-chrome', 'https://www.youtube.com/watch?v=xlUFkMKSB3Y'])


    elif user4 == dict["maths"][1]:
        user5 = raw_input("You would like to learn from theory or videos?\n")
        if user5 == "theory":
            print Popen(['google-chrome', "https://revisionmaths.com/gcse-maths-revision/number"])
        elif user5 == "videos":
            Popen(['google-chrome', "https://www.youtube.com/watch?v=9-OOER1VAjU"])


    elif user4 == dict["maths"][2]:
        user5 = raw_input("You would like to learn from theory or videos?\n")
        if user5 == "theory":
            Popen(['google-chrome', "https://revisionmaths.com/gcse-maths-revision/number"])
        elif user5 == "videos":
            Popen({'google-chrome', "https://www.youtube.com/results?search_query=Geometry_theory"})
    else:
        print "Are you looking for something else, let me show you google page?"
        Popen(['google-chrome', "https://www.google.co.in/?gfe_rd=cr&ei=uDI9WdCfD43z8AfdzrPQAQ&gws_rd=ssl"])
        exit()



if user3 == dict["subject"][1]:
    user4 = raw_input("Which topic you want to learn\n['html', 'css', 'python']\n")
    if user4 == dict["coding"][0]:
        user5 = raw_input("You would like to learn from theory or videos?\n")
        if user5 == "theory":
            print Popen(['google-chrome', "https://www.w3schools.com/html/html_intro.asp" ])
        elif user5 == "videos":
            Popen(['google-chrome', "https://www.youtube.com/watch?v=6kycPB7RMnY"])

    elif user4 == dict["coding"][1]:
       user5 = raw_input("You would like to learn from theory or videos?\n")
       if user5 == "theory":
           print Popen(['google-chrome',"https://www.w3schools.com/css/css_intro.asp"])
       elif user5 == "videos":
           Popen(['google-chrome',"https://www.youtube.com/watch?v=zrNuHCiptQo"])


    elif user4 == dict["coding"][2]:
        user5 = raw_input("Would you like to learn from theory or videos?\n")
        if user5 == "theory":
            print Popen(['google-chrome', "https://www.python.org/doc/essays/blurb/"])
        elif user5 == "videos":
            Popen(['google-chrome', "https://www.youtube.com/watch?v=uyjd3pBPiU8"])
    else:
        print "Are you looking for something else, let me show you google page?"
        Popen(['google-chrome', "https://www.google.co.in/?gfe_rd=cr&ei=uDI9WdCfD43z8AfdzrPQAQ&gws_rd=ssl"])
        exit()



if user3 == dict["subject"][2]:
    print "You should read 1 chapter everyday and try to speak in english daily, you can downlaod Helloenglish aap also"
    user4 = raw_input("Which topic you want to learn?\n['models', 'tense', 'part_of_speech']\n")
    if user4 == dict["english"][0]:
       user5 = raw_input("Would you like to learn from throry or videos?\n")
       if user5 == "theory":
           print Popen(['google-chrome', "http://www.myenglishpages.com/site_php_files/grammar-lesson-modals.php"])
       elif user5 == "videos":
           Popen(['google-chrome', "https://www.youtube.com/watch?v=TfrE2ECoVQc"])

    if user4 == dict["english"][1]:
        user5 = raw_input("Would you like to learn from throry or videos?\n")
        if user5 == "theory":
            print Popen(['google-chrome', "https://www.englishclub.com/grammar/tense-what.htm"])
        elif user5 == "videos":
            Popen(['google-chrome', "https://www.youtube.com/watch?v=HdBozp4gHpQ"])


    if user4 == dict["english"][2]:
        user5 = raw_input("Would you like to learn from throry or videos?\n")
        if user5 == "theory":
            print  Popen(['google-chrome', "http://www.myenglishpages.com/site_php_files/grammar-lesson-parts-of-speech.php"])
        elif user5 == "videos":
            Popen(['google-chrome', "https://www.youtube.com/watch?v=XcnjYaHPiNw"])

    else:
        print "Are you looking for something else, let me show you google page?"
        Popen(['google-chrome', "https://www.google.co.in/?gfe_rd=cr&ei=uDI9WdCfD43z8AfdzrPQAQ&gws_rd=ssl"])
        exit()
