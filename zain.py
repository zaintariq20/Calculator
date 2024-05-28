import streamlit as st
from mul import mul
from add import add
from sub import sub
from div import div

# Title
st.title("Calculator")


# Text Input number1
num1 = st.number_input('Enter first number : ')

# Text Input
num2 = st.number_input('Enter second number : ')

# radio button number2
status = st.radio("Select Operation: ", ('Addition', 'Subtraction', 'Multiplication', 'Division'))

st.button('Result: ')
if (status == 'Addition'):
    st.success(add(num1, num2))
elif (status == 'Subtraction'):
    st.success(sub(num1, num2))
elif (status == 'Multiplication'):
    st.success(mul(num1, num2))
else:
    if (num2 > 0):
        st.success(div(num1, num2))
    else:
        exp = ZeroDivisionError("Trying to divide by Zero")
        st.exception(exp)

st.success('Thank you to use me !')