import streamlit as st
from addition import add
from  subtraction import sub
from multiplication import mul
from division import div
st.title('-----Calculator-----')
first = st.number_input("Enter first number")
operator = st.text_input("Enter   +  or  -  or  *  or  / ")
second = st.number_input("Enter second number")
result1=0.0
if operator=="+":
    result1=add(first,second)
elif operator == "-":
    result1=sub(first,second)
elif operator == "*":
    result1=mul(first,second)
elif operator == "/":
    result1=div(first,second)
if(st.button('Calculate')):
    st.success(result1)

