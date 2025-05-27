import os
from typing import List, Dict
import psycopg2
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def get_db_connection():
    """Create a connection to the PostgreSQL database."""
    return psycopg2.connect(
        dbname=os.getenv('POSTGRES_DB', 'postgres'),
        user=os.getenv('POSTGRES_USER', 'postgres'),
        password=os.getenv('POSTGRES_PASSWORD', 'password'),
        host=os.getenv('POSTGRES_HOST', 'localhost'),
        port=os.getenv('POSTGRES_PORT', '5432')
    )

def get_embedding(text: str) -> List[float]:
    """Get embedding for a text using OpenAI's API."""
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

def similarity_search(query: str, limit: int = 5) -> List[Dict]:
    """
    Perform similarity search using the query text.
    
    Args:
        query: The search query text
        limit: Maximum number of results to return
        
    Returns:
        List of dictionaries containing matching documents
    """
    query_embedding = get_embedding(query)
    
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute('''
                SELECT content, metadata, 
                       1 - (embedding <=> %s) as similarity
                FROM documents
                ORDER BY embedding <=> %s
                LIMIT %s
            ''', (query_embedding, query_embedding, limit))
            
            results = []
            for row in cur.fetchall():
                results.append({
                    'content': row[0],
                    'metadata': row[1],
                    'similarity': row[2]
                })
            
            return results

if __name__ == "__main__":
    # Example search
    query = "Tell me about machine learning"
    results = similarity_search(query)
    
    print(f"\nSearch results for query: '{query}'\n")
    for i, result in enumerate(results, 1):
        print(f"Result {i}:")
        print(f"Content: {result['content']}")
        print(f"Similarity: {result['similarity']:.4f}")
        print(f"Metadata: {result['metadata']}")
        print("---")
