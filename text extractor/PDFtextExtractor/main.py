from PyPDF2 import PdfReader
# from sentence_transformers import SentenceTransformer
#
# # Initialize the SentenceTransformer model
# model = SentenceTransformer('bert-base-nli-mean-tokens')


def extract_text_from_pdf(pdf_path, output_file):
    """
    Extract text content from a PDF file using PdfReader and save it to a text file.

    Parameters:
    - pdf_path (str): Path to the PDF file.
    - output_file (str): Path to the output text file.

    Returns:
    - None
    """
    text = ''
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()

    # Write extracted text to output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)

def chunk_text(text, max_chunk_size=500):
    """
    Break the text into smaller chunks without splitting sentences.

    Parameters:
    - text (str): The text to be chunked.
    - max_chunk_size (int): The maximum size of each chunk (default is 500 characters).

    Returns:
    - list[str]: List of text chunks.
    """
    sentences = text.split('. ')
    chunks = []
    current_chunk = ''

    for sentence in sentences:
        if len(current_chunk) + len(sentence) + 2 <= max_chunk_size:  # 2 for the '. ' separator
            current_chunk += sentence + '. '
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + '. '

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

# def embed_text(text):
#     """
#     Embed text into vector representation using SentenceTransformer.
#
#     Parameters:
#     - text (str): The text to be embedded.
#
#     Returns:
#     - numpy.ndarray: Vector representation of the text.
#     """
#     # Generate embeddings
#     embeddings = model.encode([text])
#     return embeddings[0]

# Example usage:
pdf_path = 'Greek_God_Pantheon.pdf'  # Replace with your PDF file path
output_file = 'extracted_text.txt'  # Output text file path

extract_text_from_pdf(pdf_path, output_file)
print(f"Text extracted from {pdf_path} and saved to {output_file}")


output_file = 'extracted_text.txt'  # Replace with your output text file path

# Read the extracted text from the output file
with open(output_file, 'r', encoding='utf-8') as file:
    extracted_text = file.read()

# Chunk the extracted text
text_chunks = chunk_text(extracted_text)

# Print the number of chunks and the first chunk as a sample
print(f"Number of chunks: {len(text_chunks)}")
print("Sample chunk:")
print(text_chunks[1])

embedded_text_chunks = [embed_text(chunk) for chunk in text_chunks]

# Print the embeddings for the first chunk as a sample
print("Embedding for the first chunk:")
print(embedded_text_chunks[0])
