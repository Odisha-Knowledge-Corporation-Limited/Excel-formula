import pprint
import google.generativeai as palm
import streamlit as st

palm.configure(api_key='AIzaSyCSu5dfNhIfyMDaF_CC8yQz0S_SngWTiqQ')

def generate_excel_formula(query):
    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name

#a = input("Enter your query for excel - ")
    prompt = query+",give answer as excel formula."

    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0,
        # The maximum length of the response
        max_output_tokens=800,
    )
    return completion.result

def main():
    st.title("Excel Formula")
    query =st.text_input("Enter your query for excel: ")

    if st.button("Generate Formula"):
        excel_formula = generate_excel_formula(query)
        st.success("Generate Formula:")
        st.write(excel_formula)

st.sidebar.markdown("### Usage Instructions")
st.sidebar.markdown("1. Enter your question in the input box.")
st.sidebar.markdown("2. Click on the Generate Formula Button to generate the Answer.")   

if __name__ =="__main__":
    main()