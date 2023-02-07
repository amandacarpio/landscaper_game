# State

game = {'tool': 0, 'money': 0}

tools = [
    {'name': 'Teeth', 'profit': 1, 'cost': 0},
    {'name': 'Rusty Scissors', 'profit': 5, 'cost': 5},
    {'name': 'Old-Timey Lawnmower', 'profit': 50, 'cost': 25},
    {'name': 'Battery-Powered Lawnmower', 'profit': 100, 'cost': 250},
    {'name': 'Starving Students', 'profit': 250, 'cost': 500},
]

# Game Option Function

def mow_lawn():
    tool = tools[game['tool']]
    print(f"You can use {tool['name']} to cut grass and make {tool['profit']}")
    game['money'] += tool['profit']
    
def check_stats():
    tool = tools[game['tool']]
    print(f"You currently have {game['money']} and are using a {tool['name']}")
    
def upgrade():
    if (game['tool'] >= len(tools) -1):
        print('No more upgrades')
        return 0
    print('You are upgrading your tool')
    next_tool = tools[game["tool"]+1]
    if(next_tool == None):
        print("There is no more tools")
        return 0
    if(game['money'] < next_tool['cost']):
        print("Not enough money to buy tool")
        return 0
    game['money'] -= next_tool['cost']
    game['tool'] += 1
    
def win_check():
    if(game['tool'] == 4 and game['money'] >= 1000):
        print("You've Won")
        return True
    return False

while(True):
    i = input('[1] Be a landscaper [2] Check Stats [3] Upgrade [4] Quit')
    
    i = int(i)
    
    if(i == 1):
        mow_lawn()
    if(i == 2):
        check_stats()
    if(i == 3):
        upgrade()
    if(i == 4):
        print('You quit the game')
        break
    if(win_check()):
        break