try:
    RESULT = 10 + "10"
except:
    print("some exception")
else:
    print("result is ", RESULT)
finally:
    print("It should execute any case")
