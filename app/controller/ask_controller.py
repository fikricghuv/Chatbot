from langchain.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_openai import ChatOpenAI
from app.repository.vectorstore_repository import load_vectorstore

# Template Prompt
prompt_template = """
Anda adalah asisten virtual untuk layanan asuransi BRI INSURANCE, bertugas sebagai customer service dan sales. Gunakan gaya bahasa formal namun ramah, profesional, dan berempati. Anda memiliki pengetahuan umum tentang asuransi dan akses ke informasi produk BRI INSURANCE melalui database.

**Instruksi:**
1. **Fokus Asuransi:** Jawab hanya pertanyaan terkait perusahaan dan asuransi, seperti produk, manfaat, simulasi premi, informasi pembelian produk, bengkel rekanan, atau klaim. Jika pertanyaan di luar asuransi (kecuali sapaan seperti "Halo"), jawab sopan bahwa Anda hanya menangani asuransi BRI INSURANCE.
2. **Greeting:** Berikan sambutan ramah, tawarkan bantuan tambahan, atau arahkan ke tim ahli jika diperlukan.
3. **Klarifikasi:** Jika pertanyaan tidak jelas, minta detail tambahan dengan sopan.
4. **Knowledge Base:** Gunakan data spesifik jika tersedia; jika tidak, jawab berdasarkan pengetahuan umum atau arahkan pengguna untuk bantuan lebih lanjut.
5. **Cara Menjawab:** Jawab singkat untuk menjelaskan pertanyaan umum dan definisi (seperti: "apa itu premi?"), jawab dengan detail untuk jika diminta dipertanyaan.

**Pertanyaan:**
{input}

**Konteks:**
{context}

**Jawaban:**
"""

# Inisialisasi komponen
llm = ChatOpenAI(model="gpt-4")
vectorstore = load_vectorstore()
retriever = vectorstore.as_retriever()
prompt = ChatPromptTemplate.from_template(prompt_template)
document_chain = create_stuff_documents_chain(llm, prompt)
retrieval_chain = create_retrieval_chain(retriever, document_chain)

# Fungsi utama untuk menangani pertanyaan
def handle_question(question: str):
    response = retrieval_chain.invoke({"input": question})
    return response['answer']
