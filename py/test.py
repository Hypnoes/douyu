from functools import partial
import colors as c

print(c.color('my string', fg='blue'))
print(c.color('some text', fg='red', bg='yellow', style='underline'))
print()

for i in range(256):
    if i % 8 != 7:
        print('|', c.color('Color #{0}'.format(i).ljust(11), fg=i), end='')
    else:
        print('|', c.color('Color #{0}'.format(i).ljust(11), fg=i), end='|\n')

print()
print(c.color('orange on gray', 'orange', 'gray'))
print(c.color('nice color', 'white', '#8a2be2'))

print(c.red('This is red'))
print(c.green('This is green'))
print(c.blue('This is blue'))

print(c.red('red on blue', bg='blue'))
print(c.green('green on black', bg='black', style='underline'))

print(c.red('very important', style='bold+underline'))


important = partial(c.color, fg='red', style='bold+underline')
print(important('this is very important!'))

print("\n-----------\n")
print(c.color("gYw", style="none"))
print(c.color("gYw", style="bold"))
print(c.color("gYw", style="faint"))
print(c.color("gYw", style="italic"))
print(c.color("gYw", style="underline"))
print(c.color("gYw", style="blink"))
print(c.color("gYw", style="blink2"))
print(c.color("gYw", style="negative"))
print(c.color("gYw", style="concealed"))
print(c.color("gYw", style="crossed"))
print()
