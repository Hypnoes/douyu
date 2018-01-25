from functools import partial
import colors as c

print(c.color('my string', fg='blue'))
print(c.color('some text', fg='red', bg='yellow', style='underline'))
print()

for i in range(256):
    if i % 8 != 7:
        print(c.color('Color #{0}'.format(i).ljust(10), fg=i), end='|')
    else:
        print(c.color('Color #{0}'.format(i).ljust(10), fg=i), end='\n')
print()

print(c.color('orange on gray', 'orange', 'gray'))
print(c.color('nice color', 'white', '#8a2be2'))

print(c.red('This is red'))
print(c.green('This is green'))
print(c.blue('This is blue'))

print(c.red('red on blue', bg='blue'))
print(c.green('green on black', bg='black', style='underline'))

print(c.red('very important', style='bold+underline'))


important = partial(c.color, fg='red', style='bold+negative+blink')
print(important('this is very important!'))
print()

print(c.color("none", style="none"))
print(c.color("bold", style="bold"))
print(c.color("faint", style="faint"))
print(c.color("italic", style="italic"))
print(c.color("underline", style="underline"))
print(c.color("blink", style="blink"))
print(c.color("blink2", style="blink2"))
print(c.color("negative", style="negative"))
print(c.color("concealed", style="concealed"))
print(c.color("crossed", style="crossed"))
print()
