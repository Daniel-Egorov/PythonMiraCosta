"""
{
    "File": "hw6project3.py",
    "Author": "Daniel Egorov",
    "Date": "03/03/21",
    "Desc": [
        "A program that prints out the lyrics",
        "of 'The Ants Go Marching'",
    ],
    "Algorithm": [
        "one function to return the marching lyric w/o hurrah",
        "second function to return marching lyric w/ hurrah",
        "third function to return the little one and his action",
        "fourth function to return the rest of the verse that is unchanging",
        "final function to put the previous ones together",
        "and the main function to call the final function 10 times with each parameter"
    ]
}

"""

# returns ants go marching lyric w/o the hurrah
def march(amount):
    return f'The ants go marching {amount} by {amount},'

# calls the previous function and adds the hurrah to the end
def marchHurrah(amount):
    return f'{march(amount)} hurrah! hurrah!'

# returns the little one's lyric along with his action
def littleOne(action):
    return f'The little one stops to {action},'

# returns the rest of the verse that is unchanging
def ending():
    return 'And they all go marching down...\nIn the ground...\nTo get out...\nOf the rain.\nBoom! Boom! Boom!'

# combines all the functions above to generate one verse
def song(amount, action):
    for i in range(2):
        print(marchHurrah(amount))
    print(march(amount))
    print(littleOne(action))
    print(ending())

# create all ten verses
def main():
    song('one', 'suck his thumb')
    song('two', 'tie his shoe')
    song('three', 'climb a tree')
    song('four', 'shut the door')
    song('five', 'take a dive')
    song('six', 'pick up sticks')
    song('seven', 'pray to heaven')
    song('eight', 'roller-skate')
    song('nine', 'check the time')
    song('ten', 'shout THE END')

main()