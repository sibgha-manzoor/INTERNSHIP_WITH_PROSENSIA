def s_r_str(i_str, search_term, replacement_term):
    m_str = i_str.replace(search_term, replacement_term)
    return m_str
    
result = s_r_str("hello world, hello everyone", "hello", "hi")
print(result)
