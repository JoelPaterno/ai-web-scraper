import streamlit as st
from scrape import scrape_website, split_dom_content, clean_body_content, extract_body_content
from parse import parse_with_ollama

st.title("AI Web Scraper")
url = st.text_input("Enter a website url")

if st.button("Scrape Site"):
    st.write("Scraping the website")
    result = scrape_website(url)
    body_content = extract_body_content(result)
    #print(body_content)
    cleaned_content = clean_body_content(body_content)
    #print(cleaned_content)
    st.session_state.dom_content = cleaned_content

    with st.expander("View DOM content"):
        st.text_area("DOM Content", cleaned_content, height=300)

    if "dom_content" in st.session_state:
        parse_description = st.text_area("Describe what you want to parse")

        if st.button("Parse Content"):
            if parse_description:
                st.write("Parsing the content")

                dom_chuncks = split_dom_content(st.session_state.dom_contnent)
                result = parse_with_ollama(dom_chuncks, parse_description)
                st.write(result)