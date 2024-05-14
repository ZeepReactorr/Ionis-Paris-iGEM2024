import streamlit as st
import os
import main
from io import StringIO

#change into the desired directory to store the results of the sorting
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

st.set_page_config(layout="wide")

st.markdown("Upload loong-hairpin RNA files here. 200MB max. Fasta format required.")

upfile = st.file_uploader("Upload")

file_queue = 0

if upfile is not None:
    # To convert to a string based IO:
    stringio = StringIO(upfile.getvalue().decode("utf-8"))
    with open("seq_origin.fasta", 'w', encoding='utf-8') as origin:
        origin.write(stringio.read())

    liste_origin = main.load_seq("seq_origin.fasta")
    file_list = main.sep_seq(liste_origin)
    
    st.write(f"{len(file_list)} files to be downloaded")

    for index, file in enumerate(file_list):
        downfile = st.download_button(f"Download file number {index}", open(file).read(), file)

