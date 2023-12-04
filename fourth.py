input_string = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''


#---------------------------------------------------------------------------------------------------
# Part 1:
#---------------------------------------------------------------------------------------------------

def points_of_cards(string_of_games):
    card_list, n_match_lst = string_of_games.splitlines(), []

    for card in card_list:
        
        #removes 'game x:' and whitespaces
        card = card[card.find(':')+1:].strip().split('|')
    
        #create two lists for each game
        numbers, winning_numbers = card[0].strip().split(' '), card[1].strip().split(' ')
        winning_numbers = [element for element in winning_numbers if element]
        
        #count similar items in both lists and calculate score
        n_match_lst.append(len(set(numbers) & set(winning_numbers)))
        card_point_lst = [2**(n-1) if n>0 else 0 for n in n_match_lst]
    
    return n_match_lst, card_point_lst

sum_all_points = sum(points_of_cards(input_string)[1])
print('Pt. 1) Sum of points', sum_all_points)

#---------------------------------------------------------------------------------------------------
# Part 2:
#---------------------------------------------------------------------------------------------------

def all_games(n_matches_lst):
    
    new_lst = [1] * len(count_lst) #list to fill dictionary
    duplicate_dict = {k: v for k, v in enumerate(new_lst)} #dictioinary to store number of each game

    for idx, count in enumerate(count_lst):
        for k in range(idx, idx+count):
            duplicate_dict[k+1] += 1*duplicate_dict[idx]
         
    return duplicate_dict

count_lst = points_of_cards(input_string)[0] #list of wins in original cards
duplicate_dict = all_games(count_lst)
print('Pt. 2) Sum of all games:', sum(duplicate_dict.values()))
