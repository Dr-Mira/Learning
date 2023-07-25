# work with these variables
violinists = set(input().split(', '))
german_speakers = set(input().split(', '))
german_violinists = violinists & german_speakers
print(german_violinists)
