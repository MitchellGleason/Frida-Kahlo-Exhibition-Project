"""
*This is a cumulative project apart of Codecademy curriculum
Overview:
Put together an audio tour for a retrospective of Frida Kahlo's work at a museum.
Need to: create a list of each painting that is featured, the date it was painted
and its spot within the tour.
"""

#Create a list of the included painting using their given titles
paintings = ["The Two Fridas", "My Dress Hangs There", "Tree of Hope",
    "Self Portrait With Monkeys"
    ]

#Create a list of dates the included paintings were completed in
dates = [1939, 1933, 1946, 1940]

#Append newly added paintings
paintings.extend(["The Broken Column", "The Wounded Deer",
    "Me and My Doll"])

dates.extend([1944, 1946, 1937])

#Create a dictionary by zipping the 'paintings' and 'dates' lists together
paintings_info = list(zip(paintings, dates))

#Find the length of the 'paintings' list and assign primary id numbers to each in a dictionary
#Find the number of paintings
num_of_paintings = len(paintings)

#Create an empty dictionary
paintings_info_w_id = {}

#Create variable to iterate and store to dictionary in while loop
id = 1

#Iterate through the 'paintings_info' list and through a range from 1 to the number of paintings
#First loop gets and stores each painting name and date to then add to the dictionary
for painting in paintings_info:
    #Second loop iterates through 1 to the number of paintings and assigns the number as the
    #dictionary key, then uses the previously stored painting and date (as a list) as value
    while id <= (num_of_paintings + 1):
        paintings_info_w_id.update({id: painting})
        break
    id += 1

#Creates a variable to store a user input
user_input = input("Which painting would you like to learn about: ")

#Creates a function to output the correct information about a painting chosen by the user
def painting_audio(input):
    #Allows the 'paintings' list to be used within the function
    global paintings
    
    #If statement to check if the user input is in the 'paintings' list, else returns error message
    if input in paintings:
        #Information from: https://artincontext.org/the-two-fridas-by-frida-kahlo/
        if input == "The Two Fridas":
            print("""\nThe Two Fridas painting, titled Las dos Fridas in Spanish, was one of Kahlo’s 
largest paintings. It was a poignant presentation of her inner emotional world 
depicted by two images of herself.\n
There is a lot that can be said about The Two Fridas by Frida Kahlo; it is a key to 
the inner recesses of Kahlo’s heart and heritage. Whether or not the artist intentionally 
left it open to interpretation for us, the viewers, or simply just painted what she felt 
due to her heartbreak and pain, nonetheless, it holds many meanings, and maybe Kahlo 
painted it with many meanings in mind.\n
“The Two Fridas” meaning could possibly be allocated to four different explanations 
that the artist incorporated in her painting, namely and most importantly, the hurt 
and sadness from her divorce from Diego Rivera.\n
The other three meanings could be around the chronic pain she always experienced due 
to the near-fatal accident when she was younger, her indigenous Mexican and European 
heritage, and the schism this may have formed within her identity as a woman, and lastly, 
some sources state that Kahlo referred to her imaginary friend when she was growing up, 
which the artist could be alluding to in her painting here.\n
            """)
        #Information from: https://www.fridakahlo.org/my-dress-hangs-there.jsp
        elif input == "My Dress Hangs There":
            print("""\nAfter more than three years of staying in America, Frida started wanting to 
go back to Mexico desperately. But her husband, Diego Rivera, was enjoying the fame 
and popularity he got from this country and didn't want to go back. This painting is 
the result of this conflict. Frida Kahlo was trying to depict the superficiality of 
American capitalism.\n
This painting is filled with the icons of the modern industrial 
society of the United States but implied that society is decaying and the fundamental 
human values are destructed. In contrast to this painting, her husband Diego Rivera was 
working on a mural in the Rockefeller Center to prove his approval of the industrial 
progress in America.\n
Not like her other paintings with her face always shows up, this painting is missing 
the focal point of Frida Kahlo. She only draws her dresses hanging there empty and alone 
with the chaos in the background. It seems she was saying "I may be in America but only 
my dress hangs there my life is in Mexico."\n
            """)
        #Information from: https://www.fridakahlo.org/tree-of-hope.jsp
        elif input == "Tree of Hope":
            print("""\nAfter Frida returned to Mexico from the United States, she was staying in 
bed for a while and then wearing a steel corset for eight months. But her health 
condition has been worsening instead of improving. She got sharp pains in her spine 
and lost her appetite due to the long-lasting pain. But she still paints and in a 
letter she wrote to her friend, she mentioned this painting, Tree of Hope, 1946 as 
"nothing but the result of the damned operation!"\n
In this painting, under the gloomy sky, the sun and moon divided the background into 
two halves of light and dark. In the middle, Frida was sitting there and weeping in 
a read Tehuana costume. Nevertheless she seems strong and confident. Behind her on a 
hospital trolley, lying a second Frida, who is anesthetized and her surgical incisions 
still open and dripping with blood. Frida was holding a pink orthopedic corset while 
sitting in the wooden chair. On her other hand, she was holding a flag which has words 
from a song ""Cielito Lindo" - "Tree of Hope, Remain Strong."\n
            """)
        #Information from: https://www.fridakahlo.org/self-portrait-with-monkey-1940.jsp
        elif input == "Self Portrait With Monkeys":
            print("""\nSeveral of Frida's 1940 paintings are dominated by a yellow that only 
exacerbates the dour mood. This yellow is not sunny, it is glaring. The yellow 
background in the Self-Portrait commissioned by the American engineer Sigmund 
Firestone, for example, makes Frida's black veil even more funereal. The yellow 
bedspread in The Dream is hallucinatory, and the yellow kitchen chair in the bleak 
Self-Portrait with Cropped Hair has the inappropriate gaiety of the yellow bed and 
chair in The Bedroom At Arles by Van Gogh.\n
The darkness in the interstices of a wall of leaves in a nocturne entitled Self-Portrait with 
Monkey, 1940, seems a more straightforward expression of Frida's gloom. Here a blood-red ribbon 
braided through her hair winds around her neck four times and around her pet monkeys once. The 
mood is claustrophobic; beginning in the year of her divorce, Frida began to encircle her neck 
in self-portraits with ribbons, necklaces, veins, vines, or a monkey's long arms that threaten 
to choke her. To identify the monkey as her close relative, Frida made his left arm continuous 
with her braid. Although she may have wanted to show her feeling of connectedness, the effect is sinister.\n
            """)
        #Information from: https://www.fridakahlo.org/the-broken-column.jsp
        elif input == "The Broken Column":
            print("""\nPain and suffering is a constant topic in Frida's painting. In this painting, 
The Broken Column, Frida expressed her anguish and suffering in the most straightforward 
and horrifying way. The nails are stuck into her face and whole body. A split in her 
torso looks like an earthquake fissure. In the background is the earth with dark ravines. 
In the beginning she paints herself nude but later covered her lower part up with 
something the looks like a hospital sheet. A broken column is put in place of her spine. 
The column appears to be on the verge of collapsing into rubble. Penetrating from loins 
to chin, the column looks phallic, and the sexual connotation is all the more obvious 
because of the beauty of Frida's breasts and torso.\n
This painting Frida looks pretty and strong. Although her whole body is supported by the corset, she 
is conveying a message of spiritual triumph. She has tears on her face but she look straight ahead 
and is challenging both herself and her audience to face her situation. The style of this painting 
is very unique. She laid down each stoke firmly to build a simple and clear image. There are no virtuoso 
flourishes of the brush and the colors are as neatly contained within contours.\n 
            """)
        #Information from: https://www.fridakahlo.org/the-wounded-deer.jsp
        elif input == "The Wounded Deer":
            print("""\nIn this painting, Frida used a young deer with the head of herself and was 
fatally wounded by a bunch of arrows. The background is the forest with dead trees 
and broken branches, which implied the feeling of fear and desperation. Far away is 
the stormy, lightning-lit sky which brings some hope but the dear will never be 
able to reach it.\n
In 1946 Frida Kahlo had an operation on her spine in New York. She was hoping this 
surgery would free her from the severe back pain but it failed. This painting 
expressed her disappointment towards the operation. After she went back to Mexico, 
she suffered both physical pain and emotional depression. In this painting she 
depicted herself as a young stag with her own head crowned with antlers. This 
young stag is pierced by arrows and bleeding. At the lower-left corner, the 
artist wrote down the word "Carma", which means "destiny" or "fate". Just like 
her other self-portraits, in this painting Frida expressed the sadness that 
she cannot change her own fate.\n
            """)
        #Information from: https://www.fridakahlo.org/me-and-my-doll.jsp
        elif input == "Me and My Doll":
            print("""\nFrida was known to be not able to bear children due to the bus accident that 
happened in the year of 1925. And at the time this painting was painted, she has lost 
three unborn children. She has been collecting dolls and keeping pets on which 
she gave her love to.\n
This portrait depicts Frida sitting on a bed with a doll. But she seems distant 
and disconnected with the substitute of her baby. She seems to be posing for 
the camera and doesn't care about the doll at all. Also. she was smoking a 
cigarette, which people usually don't do while a baby is around. It seems she 
knows the doll is not her own real child and she shows no attachment to it at all.\n
She has an expression of sadness and loneliness on her face, maybe due to the 
fact that she is childless. Her room is empty and add a feeling of emptiness. 
Also her skin tone id darker than in her other paintings to match her Mexican clothes.\n
            """) 
    else:
        print("Error - Please enter the name of a painting. Exact spelling and capitalization is required. Your options are:\n")
        #Prints all items in 'paintings' list
        for name in paintings:
            print(name + "\n")

#Call on the function with the user input string as an argument to determine which painting info to print
painting_audio(user_input)