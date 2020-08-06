intro = 'Welcome to the super super cool Pyton Class'

print(intro.upper())
print(intro.lower())
print(intro.replace(' ', '-' ))
print(len(intro))



q = input('Does the intro start with Welcome? (y/n)')
ask = q.upper().startswith('Y')
print(ask)

#Another Way:
print(intro.startswith('Welcome'))
