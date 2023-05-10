def CHX(st):
    st = st.title()
    st = st.strip()
    kt = "  "
    while kt in st:
        st = st.replace("  "," ")
    return st
s = str(input())
print(CHX(s))