import streamlit as st
st.header('Temperature conversion') 
a=st.number_input('Please enter the temparature')
b=['F','C','K']
c=st.radio('Input your base temperature',b )
conv=st.radio('Input temperatue you want to convert to',b)
if c=='F'and conv=='C':
    d=round(((a-32)*5)/9,1)
    if st.button('Calculate'):
        st.write (f'{d}C')
elif  c=='C' and conv=='F':
    d=round((a*9/5)+32,1)
    if st.button('Calculate'):
        st.write (f'{d}F')
elif c=='C' and conv=='K':
    d=a+273
    if st.button('Calculate'):
        st.write (f'{d}K')
elif  c=='K' and conv=='C':
    d=a-273
    if st.button('Calculate'):
        st.write (f'{d}C')
elif c=='F'and conv=='K':
    first=round(((a-32)*5)/9,1)
    d=first+273
    if st.button('Calculate'):
        st.write (f'{d}K')
elif c=='K'and conv=='F':
    first=273-a
    d=round(((first-32)*5)/9,1)
    if st.button('Calculate'):
        st.write (f'{d}F')
elif c=='K'and conv=='K':
    d=a
    if st.button('Calculate'):
        st.write (f'{a}K')
elif c=='C'and conv=='C':
    d=a
    if st.button('Calculate'):
        st.write (f'{a}C')
elif c=='F'and conv=='F':
    d=a
    if st.button('Calculate'):
        st.write (f'{a}F')
else:
     if st.button('Calculate'):
        st.write('Error')
