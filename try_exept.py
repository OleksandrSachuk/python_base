while True:
    try:
        number = int(input('Your number?'))
        print(18 / number)
        break
    except ValueError:
        print('Need number')
    except ZeroDivisionError:
        print('Zero error')
    except:
        break
    finally:
        print('loop complete')
