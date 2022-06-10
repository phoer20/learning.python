import time, sys
indent = 0
indentIncreasing = True

try:
    while True:
        print(' ' * indent, end='') # end= is so we dont print a new blank line
        print('********')
        time.sleep(0.1)

        if indentIncreasing:
            indent = indent + 1
            if indent == 20:
                indentIncreasing = False

        else:
            indent = indent - 1
            if indent == 0:
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()
