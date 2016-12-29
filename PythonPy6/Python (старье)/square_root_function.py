def my_square_root(input_number):
    x=input_number
    guess=x/2
    accuracy=0.001
    while abs(x-guess**2)>accuracy:
        guess=(guess+(x/guess))/2
    return (guess)
