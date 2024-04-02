import streamlit as st
import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyDl48GZuA4O9AAhEGTDC6Ml5K28N3ut-0U"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')
st.title("SQL Querry Generator 🤖")

def main():
    # st.set_page_config(page_title="SQL Querry Generator", page_icon=":robot:")
    st.markdown(
        """
        <div>
          <h3>This is a tool to generate SQL querries from text with explanation as well 

        """,
        unsafe_allow_html=True,


    )
    text_input = st.text_area("Enter your Querry as a plain text here:")
    
    submit = st.button("Generate SQL Querry")
    
    if submit:
        with st.spinner("Generating SQL Querry"):
            template="""

            Create a sQL querry snippet using the below text:
            ```
                {text_input}
            ```
            I just want a SQL Querry
            
        """
        formatted_template = template.format(text_input=text_input)
        # st.write(formatted_template)
        response = model.generate_content(formatted_template )
        sql_q = (response.text)

        with st.container():
            st.success("SQL Querry Generated Successfully!")

            st.write(sql_q)

        ## expected output 
        expected_output = """
            What would be the expected response  of this querry snippet:
               ```
                {sql_q}
               ```
            Provide sample tabular** response with no explanation:
        """

        expected_output_formatted = expected_output.format(sql_q=sql_q)
        eoutput = model.generate_content(expected_output_formatted)
        eoutput = eoutput.text

        with st.container():
            st.success("Expected output of your querry will be:")
        st.write(eoutput)

        explanation = """
            Explain this SQL Querry:
               ```
                {sql_q}
               ```
            Provide with simplest but lil detail of explanation:
        """
        explanation_formatted = explanation.format(sql_q=sql_q)
        exp = model.generate_content(explanation_formatted)
        exp = exp.text
        with st.container():
            st.success("Here is the brief explanation of your querry 👇")
        st.write(exp)

       
            # st.code(sql_q, language="sql")



main() 
    
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://repository-images.githubusercontent.com/275336521/20d38e00-6634-11eb-9d1f-6a5232d0f84f");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
add_bg_from_url()